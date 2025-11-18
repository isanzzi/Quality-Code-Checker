import sys
from antlr4 import *
from grammar.CodeQualityDSLLexer import CodeQualityDSLLexer
from grammar.CodeQualityDSLParser import CodeQualityDSLParser
from grammar.CodeQualityDSLVisitor import CodeQualityDSLVisitor
from models.rule import Rule

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
    """Parse DSL file and return list of rules"""
    with open(file_path, 'r') as f:
        input_stream = InputStream(f.read())
    
    lexer = CodeQualityDSLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CodeQualityDSLParser(stream)
    tree = parser.program()
    
    visitor = DSLRuleVisitor()
    rules = visitor.visit(tree)
    
    return rules
