import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from grammar.CodeQualityDSLLexer import CodeQualityDSLLexer
from grammar.CodeQualityDSLParser import CodeQualityDSLParser
from grammar.CodeQualityDSLVisitor import CodeQualityDSLVisitor
from models.rule import Rule


class DSLErrorListener(ErrorListener):
    """Custom error listener for DSL syntax errors"""
    def __init__(self):
        super(DSLErrorListener, self).__init__()
        self.errors = []
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"DSL Syntax Error at line {line}:{column} - {msg}"
        self.errors.append(error_msg)
        print(f"❌ {error_msg}", file=sys.stderr)
    
    def has_errors(self):
        return len(self.errors) > 0

class DSLRuleVisitor(CodeQualityDSLVisitor):
    def __init__(self):
        self.rules = []
    
    def visitProgram(self, ctx):
        for rule_def in ctx.rule_definition():
            self.visit(rule_def)
        return self.rules
    
    def visitRule_definition(self, ctx):
        rule_name = ctx.STRING().getText().strip('"')
        
        # Extract attributes
        target = None
        condition = None
        severity = None
        message = ""
        
        for attr in ctx.rule_body().rule_attribute():
            if attr.target_type():
                target = attr.target_type().getText()
            elif attr.condition_expr():
                condition = attr.condition_expr()
            elif attr.severity_level():
                severity = attr.severity_level().getText()
            elif attr.STRING():
                message = attr.STRING().getText().strip('"')
        
        rule = Rule(
            name=rule_name,
            target=target,
            condition=condition,
            severity=severity,
            message=message
        )
        
        self.rules.append(rule)
        return rule

def parse_dsl_file(file_path):
    """Parse DSL file and return list of rules with error handling"""
    try:
        with open(file_path, 'r') as f:
            input_stream = InputStream(f.read())
    except FileNotFoundError:
        raise Exception(f"❌ DSL file not found: {file_path}")
    except Exception as e:
        raise Exception(f"❌ Error reading DSL file: {str(e)}")
    
    # Create lexer and parser with custom error listener
    lexer = CodeQualityDSLLexer(input_stream)
    error_listener = DSLErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    
    stream = CommonTokenStream(lexer)
    parser = CodeQualityDSLParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    
    # Parse the DSL
    tree = parser.program()
    
    # Check for syntax errors
    if error_listener.has_errors():
        error_summary = "\n".join(error_listener.errors)
        raise Exception(f"❌ DSL parsing failed due to syntax errors:\n{error_summary}")
    
    # Visit the parse tree
    visitor = DSLRuleVisitor()
    rules = visitor.visit(tree)
    
    # Validate rules
    validate_rules(rules)
    
    return rules


def validate_rules(rules):
    """Validate that all rules have required attributes"""
    for rule in rules:
        if not rule.target:
            raise Exception(f"❌ Rule '{rule.name}' missing required attribute: target")
        if rule.target not in ['function', 'class', 'variable', 'import']:
            raise Exception(f"❌ Rule '{rule.name}' has invalid target: '{rule.target}'. Must be: function, class, variable, or import")
        if not rule.condition:
            raise Exception(f"❌ Rule '{rule.name}' missing required attribute: condition")
        if not rule.severity:
            raise Exception(f"❌ Rule '{rule.name}' missing required attribute: severity")
        if rule.severity not in ['error', 'warning', 'info']:
            raise Exception(f"❌ Rule '{rule.name}' has invalid severity: '{rule.severity}'. Must be: error, warning, or info")
        if not rule.message:
            raise Exception(f"❌ Rule '{rule.name}' missing required attribute: message")

