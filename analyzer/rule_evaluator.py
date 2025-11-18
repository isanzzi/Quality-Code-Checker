import re
from grammar.CodeQualityDSLParser import CodeQualityDSLParser

class RuleEvaluator:
    def __init__(self, rules, metrics):
        self.rules = rules
        self.metrics = metrics
        self.violations = []
    
    def evaluate_all(self):
        """Evaluate all rules against metrics"""
        for rule in self.rules:
            if rule.target == 'function':
                self._evaluate_function_rules(rule)
            elif rule.target == 'variable':
                self._evaluate_variable_rules(rule)
            elif rule.target == 'class':
                self._evaluate_class_rules(rule)
        
        return self.violations
    
    def _evaluate_function_rules(self, rule):
        """Evaluate rules for functions"""
        for func in self.metrics.functions:
            if self._evaluate_condition(rule.condition, func):
                violation = {
                    'rule': rule.name,
                    'severity': rule.severity,
                    'target': 'function',
                    'name': func.name,
                    'line': func.line_number,
                    'message': self._format_message(rule.message, func)
                }
                self.violations.append(violation)
    
    def _evaluate_variable_rules(self, rule):
        """Evaluate rules for variables"""
        for var in self.metrics.variables:
            if self._evaluate_condition(rule.condition, var):
                violation = {
                    'rule': rule.name,
                    'severity': rule.severity,
                    'target': 'variable',
                    'name': var.name,
                    'line': var.line_number,
                    'message': self._format_message(rule.message, var)
                }
                self.violations.append(violation)
    
    def _evaluate_class_rules(self, rule):
        """Evaluate rules for classes"""
        for cls in self.metrics.classes:
            if self._evaluate_condition(rule.condition, cls):
                violation = {
                    'rule': rule.name,
                    'severity': rule.severity,
                    'target': 'class',
                    'name': cls.name,
                    'line': cls.line_number,
                    'message': self._format_message(rule.message, cls)
                }
                self.violations.append(violation)
    
    def _evaluate_condition(self, condition_ctx, metrics_obj):
        """Evaluate condition expression"""
        if isinstance(condition_ctx, CodeQualityDSLParser.ComparisonConditionContext):
            return self._evaluate_comparison(condition_ctx.comparison_expr(), metrics_obj)
        
        elif isinstance(condition_ctx, CodeQualityDSLParser.AndConditionContext):
            left = self._evaluate_condition(condition_ctx.condition_expr(0), metrics_obj)
            right = self._evaluate_condition(condition_ctx.condition_expr(1), metrics_obj)
            return left and right
        
        elif isinstance(condition_ctx, CodeQualityDSLParser.OrConditionContext):
            left = self._evaluate_condition(condition_ctx.condition_expr(0), metrics_obj)
            right = self._evaluate_condition(condition_ctx.condition_expr(1), metrics_obj)
            return left or right
        
        elif isinstance(condition_ctx, CodeQualityDSLParser.NotConditionContext):
            return not self._evaluate_condition(condition_ctx.condition_expr(), metrics_obj)
        
        elif isinstance(condition_ctx, CodeQualityDSLParser.ParenConditionContext):
            return self._evaluate_condition(condition_ctx.condition_expr(), metrics_obj)
        
        elif isinstance(condition_ctx, CodeQualityDSLParser.FunctionCallConditionContext):
            func_name = condition_ctx.IDENTIFIER().getText()
            arg = condition_ctx.STRING().getText().strip('"')
            return self._evaluate_function_call(func_name, arg, metrics_obj)
        
        elif isinstance(condition_ctx, CodeQualityDSLParser.IdentifierConditionContext):
            identifier = condition_ctx.IDENTIFIER().getText()
            return self._get_metric_value(identifier, metrics_obj)
        
        return False
    
    def _evaluate_comparison(self, comparison_ctx, metrics_obj):
        """Evaluate comparison expression"""
        identifier = comparison_ctx.IDENTIFIER().getText()
        operator = comparison_ctx.operator().getText()
        value = int(comparison_ctx.NUMBER().getText())
        
        metric_value = self._get_metric_value(identifier, metrics_obj)
        
        if operator == '>':
            return metric_value > value
        elif operator == '<':
            return metric_value < value
        elif operator == '>=':
            return metric_value >= value
        elif operator == '<=':
            return metric_value <= value
        elif operator == '==':
            return metric_value == value
        elif operator == '!=':
            return metric_value != value
        
        return False
    
    def _evaluate_function_call(self, func_name, arg, metrics_obj):
        """Evaluate function calls like matches_pattern()"""
        if func_name == "matches_pattern":
            pattern = arg
            name = getattr(metrics_obj, 'name', '')
            return bool(re.match(pattern, name))
        
        return False
    
    def _get_metric_value(self, metric_name, metrics_obj):
        """Get metric value from object"""
        return getattr(metrics_obj, metric_name, 0)
    
    def _format_message(self, message_template, metrics_obj):
        """Format message with metric values"""
        import re
        
        def replacer(match):
            var_name = match.group(1)
            return str(self._get_metric_value(var_name, metrics_obj))
        
        return re.sub(r'\{(\w+)\}', replacer, message_template)
