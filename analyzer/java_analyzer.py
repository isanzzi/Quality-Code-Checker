import javalang
from models.metrics import MethodMetrics, VariableMetrics, ClassMetrics, CodeMetrics

class JavaAnalyzer:
    def __init__(self, code):
        self.code = code
        self.tree = javalang.parse.parse(code)
        self.metrics = CodeMetrics()
    
    def analyze(self):
        """Analyze Java code and extract metrics"""
        self._analyze_classes()
        return self.metrics
    
    def _analyze_classes(self):
        """Analyze all classes in the code"""
        for path, node in self.tree.filter(javalang.tree.ClassDeclaration):
            class_metrics = ClassMetrics(
                name=node.name,
                line_number=node.position.line if node.position else 0,
                method_count=len([m for m in node.methods]) if node.methods else 0,
                attribute_count=len([f for f in node.fields]) if node.fields else 0
            )
            self.metrics.classes.append(class_metrics)
            
            # Analyze functions/methods in class
            if node.methods:
                for method in node.methods:
                    self._analyze_method(method)
            
            # Analyze fields (variables)
            if node.fields:
                for field in node.fields:
                    self._analyze_field(field)
    
    def _analyze_method(self, method_node):
        """Analyze a single function/method from Java code"""
        is_public = 'public' in [m for m in method_node.modifiers] if method_node.modifiers else False
        
        method_metrics = MethodMetrics(
            name=method_node.name,
            line_number=method_node.position.line if method_node.position else 0,
            parameter_count=len(method_node.parameters) if method_node.parameters else 0,
            is_public=is_public,
            has_docstring=method_node.documentation is not None
        )
        
        # Analyze method body
        if method_node.body:
            body_with_paths = [(None, n) for n in method_node.body]
            method_metrics.nesting_level = self._calculate_nesting_level(body_with_paths)
            
            all_nodes = list(method_node.filter(javalang.tree.Node))
            
            method_metrics.local_variable_count = self._count_local_variables(all_nodes)
            method_metrics.method_call_count = self._count_method_calls(all_nodes)
            method_metrics.return_count = self._count_returns(all_nodes)
            method_metrics.complexity = self._calculate_complexity(all_nodes)
        
        self.metrics.methods.append(method_metrics)
    
    def _analyze_field(self, field_node):
        """Analyze class fields (variables)"""
        for declarator in field_node.declarators:
            var_metrics = VariableMetrics(
                name=declarator.name,
                line_number=field_node.position.line if field_node.position else 0,
                is_constant='final' in field_node.modifiers if field_node.modifiers else False
            )
            self.metrics.variables.append(var_metrics)
    
    def _calculate_nesting_level(self, body, current_level=0):
        """Calculate maximum nesting level in method body"""
        max_level = current_level
        
        for path, node in body:
            if isinstance(node, (javalang.tree.IfStatement, 
                               javalang.tree.ForStatement,
                               javalang.tree.WhileStatement,
                               javalang.tree.DoStatement)):
                nested_level = current_level + 1
                max_level = max(max_level, nested_level)
                
                # Check nested statements
                if hasattr(node, 'then_statement') and node.then_statement:
                    if isinstance(node.then_statement, javalang.tree.BlockStatement):
                        for stmt in node.then_statement.statements:
                            level = self._calculate_nesting_level([(None, stmt)], nested_level)
                            max_level = max(max_level, level)
                
                if hasattr(node, 'else_statement') and node.else_statement:
                    if isinstance(node.else_statement, javalang.tree.BlockStatement):
                        for stmt in node.else_statement.statements:
                            level = self._calculate_nesting_level([(None, stmt)], nested_level)
                            max_level = max(max_level, level)
                
                if hasattr(node, 'body') and node.body:
                    if isinstance(node.body, javalang.tree.BlockStatement):
                        for stmt in node.body.statements:
                            level = self._calculate_nesting_level([(None, stmt)], nested_level)
                            max_level = max(max_level, level)
        
        return max_level
    
    def _count_local_variables(self, body):
        """Count local variable declarations"""
        count = 0
        for path, node in body:
            if isinstance(node, javalang.tree.LocalVariableDeclaration):
                count += len(node.declarators)
        return count
    
    def _count_method_calls(self, body):
        """Count method invocations"""
        count = 0
        for path, node in body:
            if isinstance(node, javalang.tree.MethodInvocation):
                count += 1
        return count
    
    def _count_returns(self, body):
        """Count return statements"""
        count = 0
        for path, node in body:
            if isinstance(node, javalang.tree.ReturnStatement):
                count += 1
        return count
    
    def _calculate_complexity(self, body):
        """Calculate cyclomatic complexity (simplified)"""
        complexity = 1  # Base complexity
        
        for path, node in body:
            if isinstance(node, (javalang.tree.IfStatement,
                               javalang.tree.ForStatement,
                               javalang.tree.WhileStatement,
                               javalang.tree.DoStatement,
                               javalang.tree.CatchClause)):
                complexity += 1
        
        return complexity

def analyze_java_file(file_path):
    """Analyze a Java file and return metrics"""
    with open(file_path, 'r') as f:
        code = f.read()
    
    analyzer = JavaAnalyzer(code)
    return analyzer.analyze()