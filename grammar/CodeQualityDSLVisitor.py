# Generated from CodeQualityDSL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CodeQualityDSLParser import CodeQualityDSLParser
else:
    from CodeQualityDSLParser import CodeQualityDSLParser

# This class defines a complete generic visitor for a parse tree produced by CodeQualityDSLParser.

class CodeQualityDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CodeQualityDSLParser#program.
    def visitProgram(self, ctx:CodeQualityDSLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeQualityDSLParser#rule_definition.
    def visitRule_definition(self, ctx:CodeQualityDSLParser.Rule_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeQualityDSLParser#rule_body.
    def visitRule_body(self, ctx:CodeQualityDSLParser.Rule_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeQualityDSLParser#rule_attribute.
    def visitRule_attribute(self, ctx:CodeQualityDSLParser.Rule_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeQualityDSLParser#target_type.
    def visitTarget_type(self, ctx:CodeQualityDSLParser.Target_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeQualityDSLParser#severity_level.
    def visitSeverity_level(self, ctx:CodeQualityDSLParser.Severity_levelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeQualityDSLParser#ComparisonCondition.
    def visitComparisonCondition(self, ctx:CodeQualityDSLParser.ComparisonConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeQualityDSLParser#IdentifierCondition.
    def visitIdentifierCondition(self, ctx:CodeQualityDSLParser.IdentifierConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeQualityDSLParser#NotCondition.
    def visitNotCondition(self, ctx:CodeQualityDSLParser.NotConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeQualityDSLParser#ParenCondition.
    def visitParenCondition(self, ctx:CodeQualityDSLParser.ParenConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeQualityDSLParser#FunctionCallCondition.
    def visitFunctionCallCondition(self, ctx:CodeQualityDSLParser.FunctionCallConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeQualityDSLParser#OrCondition.
    def visitOrCondition(self, ctx:CodeQualityDSLParser.OrConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeQualityDSLParser#AndCondition.
    def visitAndCondition(self, ctx:CodeQualityDSLParser.AndConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeQualityDSLParser#comparison_expr.
    def visitComparison_expr(self, ctx:CodeQualityDSLParser.Comparison_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeQualityDSLParser#operator.
    def visitOperator(self, ctx:CodeQualityDSLParser.OperatorContext):
        return self.visitChildren(ctx)



del CodeQualityDSLParser