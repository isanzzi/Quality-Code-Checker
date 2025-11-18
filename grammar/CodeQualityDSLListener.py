# Generated from CodeQualityDSL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CodeQualityDSLParser import CodeQualityDSLParser
else:
    from CodeQualityDSLParser import CodeQualityDSLParser

# This class defines a complete listener for a parse tree produced by CodeQualityDSLParser.
class CodeQualityDSLListener(ParseTreeListener):

    # Enter a parse tree produced by CodeQualityDSLParser#program.
    def enterProgram(self, ctx:CodeQualityDSLParser.ProgramContext):
        pass

    # Exit a parse tree produced by CodeQualityDSLParser#program.
    def exitProgram(self, ctx:CodeQualityDSLParser.ProgramContext):
        pass


    # Enter a parse tree produced by CodeQualityDSLParser#rule_definition.
    def enterRule_definition(self, ctx:CodeQualityDSLParser.Rule_definitionContext):
        pass

    # Exit a parse tree produced by CodeQualityDSLParser#rule_definition.
    def exitRule_definition(self, ctx:CodeQualityDSLParser.Rule_definitionContext):
        pass


    # Enter a parse tree produced by CodeQualityDSLParser#rule_body.
    def enterRule_body(self, ctx:CodeQualityDSLParser.Rule_bodyContext):
        pass

    # Exit a parse tree produced by CodeQualityDSLParser#rule_body.
    def exitRule_body(self, ctx:CodeQualityDSLParser.Rule_bodyContext):
        pass


    # Enter a parse tree produced by CodeQualityDSLParser#rule_attribute.
    def enterRule_attribute(self, ctx:CodeQualityDSLParser.Rule_attributeContext):
        pass

    # Exit a parse tree produced by CodeQualityDSLParser#rule_attribute.
    def exitRule_attribute(self, ctx:CodeQualityDSLParser.Rule_attributeContext):
        pass


    # Enter a parse tree produced by CodeQualityDSLParser#target_type.
    def enterTarget_type(self, ctx:CodeQualityDSLParser.Target_typeContext):
        pass

    # Exit a parse tree produced by CodeQualityDSLParser#target_type.
    def exitTarget_type(self, ctx:CodeQualityDSLParser.Target_typeContext):
        pass


    # Enter a parse tree produced by CodeQualityDSLParser#severity_level.
    def enterSeverity_level(self, ctx:CodeQualityDSLParser.Severity_levelContext):
        pass

    # Exit a parse tree produced by CodeQualityDSLParser#severity_level.
    def exitSeverity_level(self, ctx:CodeQualityDSLParser.Severity_levelContext):
        pass


    # Enter a parse tree produced by CodeQualityDSLParser#ComparisonCondition.
    def enterComparisonCondition(self, ctx:CodeQualityDSLParser.ComparisonConditionContext):
        pass

    # Exit a parse tree produced by CodeQualityDSLParser#ComparisonCondition.
    def exitComparisonCondition(self, ctx:CodeQualityDSLParser.ComparisonConditionContext):
        pass


    # Enter a parse tree produced by CodeQualityDSLParser#IdentifierCondition.
    def enterIdentifierCondition(self, ctx:CodeQualityDSLParser.IdentifierConditionContext):
        pass

    # Exit a parse tree produced by CodeQualityDSLParser#IdentifierCondition.
    def exitIdentifierCondition(self, ctx:CodeQualityDSLParser.IdentifierConditionContext):
        pass


    # Enter a parse tree produced by CodeQualityDSLParser#NotCondition.
    def enterNotCondition(self, ctx:CodeQualityDSLParser.NotConditionContext):
        pass

    # Exit a parse tree produced by CodeQualityDSLParser#NotCondition.
    def exitNotCondition(self, ctx:CodeQualityDSLParser.NotConditionContext):
        pass


    # Enter a parse tree produced by CodeQualityDSLParser#ParenCondition.
    def enterParenCondition(self, ctx:CodeQualityDSLParser.ParenConditionContext):
        pass

    # Exit a parse tree produced by CodeQualityDSLParser#ParenCondition.
    def exitParenCondition(self, ctx:CodeQualityDSLParser.ParenConditionContext):
        pass


    # Enter a parse tree produced by CodeQualityDSLParser#FunctionCallCondition.
    def enterFunctionCallCondition(self, ctx:CodeQualityDSLParser.FunctionCallConditionContext):
        pass

    # Exit a parse tree produced by CodeQualityDSLParser#FunctionCallCondition.
    def exitFunctionCallCondition(self, ctx:CodeQualityDSLParser.FunctionCallConditionContext):
        pass


    # Enter a parse tree produced by CodeQualityDSLParser#OrCondition.
    def enterOrCondition(self, ctx:CodeQualityDSLParser.OrConditionContext):
        pass

    # Exit a parse tree produced by CodeQualityDSLParser#OrCondition.
    def exitOrCondition(self, ctx:CodeQualityDSLParser.OrConditionContext):
        pass


    # Enter a parse tree produced by CodeQualityDSLParser#AndCondition.
    def enterAndCondition(self, ctx:CodeQualityDSLParser.AndConditionContext):
        pass

    # Exit a parse tree produced by CodeQualityDSLParser#AndCondition.
    def exitAndCondition(self, ctx:CodeQualityDSLParser.AndConditionContext):
        pass


    # Enter a parse tree produced by CodeQualityDSLParser#comparison_expr.
    def enterComparison_expr(self, ctx:CodeQualityDSLParser.Comparison_exprContext):
        pass

    # Exit a parse tree produced by CodeQualityDSLParser#comparison_expr.
    def exitComparison_expr(self, ctx:CodeQualityDSLParser.Comparison_exprContext):
        pass


    # Enter a parse tree produced by CodeQualityDSLParser#operator.
    def enterOperator(self, ctx:CodeQualityDSLParser.OperatorContext):
        pass

    # Exit a parse tree produced by CodeQualityDSLParser#operator.
    def exitOperator(self, ctx:CodeQualityDSLParser.OperatorContext):
        pass



del CodeQualityDSLParser