// Generated from c:/Users/ihsan/Documents/GitHub/Quality-Code-Checker/grammar/CodeQualityDSL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CodeQualityDSLParser}.
 */
public interface CodeQualityDSLListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CodeQualityDSLParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(CodeQualityDSLParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeQualityDSLParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(CodeQualityDSLParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link CodeQualityDSLParser#rule_definition}.
	 * @param ctx the parse tree
	 */
	void enterRule_definition(CodeQualityDSLParser.Rule_definitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeQualityDSLParser#rule_definition}.
	 * @param ctx the parse tree
	 */
	void exitRule_definition(CodeQualityDSLParser.Rule_definitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CodeQualityDSLParser#rule_body}.
	 * @param ctx the parse tree
	 */
	void enterRule_body(CodeQualityDSLParser.Rule_bodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeQualityDSLParser#rule_body}.
	 * @param ctx the parse tree
	 */
	void exitRule_body(CodeQualityDSLParser.Rule_bodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link CodeQualityDSLParser#rule_attribute}.
	 * @param ctx the parse tree
	 */
	void enterRule_attribute(CodeQualityDSLParser.Rule_attributeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeQualityDSLParser#rule_attribute}.
	 * @param ctx the parse tree
	 */
	void exitRule_attribute(CodeQualityDSLParser.Rule_attributeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CodeQualityDSLParser#target_type}.
	 * @param ctx the parse tree
	 */
	void enterTarget_type(CodeQualityDSLParser.Target_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeQualityDSLParser#target_type}.
	 * @param ctx the parse tree
	 */
	void exitTarget_type(CodeQualityDSLParser.Target_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CodeQualityDSLParser#severity_level}.
	 * @param ctx the parse tree
	 */
	void enterSeverity_level(CodeQualityDSLParser.Severity_levelContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeQualityDSLParser#severity_level}.
	 * @param ctx the parse tree
	 */
	void exitSeverity_level(CodeQualityDSLParser.Severity_levelContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ComparisonCondition}
	 * labeled alternative in {@link CodeQualityDSLParser#condition_expr}.
	 * @param ctx the parse tree
	 */
	void enterComparisonCondition(CodeQualityDSLParser.ComparisonConditionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ComparisonCondition}
	 * labeled alternative in {@link CodeQualityDSLParser#condition_expr}.
	 * @param ctx the parse tree
	 */
	void exitComparisonCondition(CodeQualityDSLParser.ComparisonConditionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IdentifierCondition}
	 * labeled alternative in {@link CodeQualityDSLParser#condition_expr}.
	 * @param ctx the parse tree
	 */
	void enterIdentifierCondition(CodeQualityDSLParser.IdentifierConditionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IdentifierCondition}
	 * labeled alternative in {@link CodeQualityDSLParser#condition_expr}.
	 * @param ctx the parse tree
	 */
	void exitIdentifierCondition(CodeQualityDSLParser.IdentifierConditionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NotCondition}
	 * labeled alternative in {@link CodeQualityDSLParser#condition_expr}.
	 * @param ctx the parse tree
	 */
	void enterNotCondition(CodeQualityDSLParser.NotConditionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NotCondition}
	 * labeled alternative in {@link CodeQualityDSLParser#condition_expr}.
	 * @param ctx the parse tree
	 */
	void exitNotCondition(CodeQualityDSLParser.NotConditionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ParenCondition}
	 * labeled alternative in {@link CodeQualityDSLParser#condition_expr}.
	 * @param ctx the parse tree
	 */
	void enterParenCondition(CodeQualityDSLParser.ParenConditionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ParenCondition}
	 * labeled alternative in {@link CodeQualityDSLParser#condition_expr}.
	 * @param ctx the parse tree
	 */
	void exitParenCondition(CodeQualityDSLParser.ParenConditionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FunctionCallCondition}
	 * labeled alternative in {@link CodeQualityDSLParser#condition_expr}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCallCondition(CodeQualityDSLParser.FunctionCallConditionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FunctionCallCondition}
	 * labeled alternative in {@link CodeQualityDSLParser#condition_expr}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCallCondition(CodeQualityDSLParser.FunctionCallConditionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code OrCondition}
	 * labeled alternative in {@link CodeQualityDSLParser#condition_expr}.
	 * @param ctx the parse tree
	 */
	void enterOrCondition(CodeQualityDSLParser.OrConditionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code OrCondition}
	 * labeled alternative in {@link CodeQualityDSLParser#condition_expr}.
	 * @param ctx the parse tree
	 */
	void exitOrCondition(CodeQualityDSLParser.OrConditionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AndCondition}
	 * labeled alternative in {@link CodeQualityDSLParser#condition_expr}.
	 * @param ctx the parse tree
	 */
	void enterAndCondition(CodeQualityDSLParser.AndConditionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AndCondition}
	 * labeled alternative in {@link CodeQualityDSLParser#condition_expr}.
	 * @param ctx the parse tree
	 */
	void exitAndCondition(CodeQualityDSLParser.AndConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CodeQualityDSLParser#comparison_expr}.
	 * @param ctx the parse tree
	 */
	void enterComparison_expr(CodeQualityDSLParser.Comparison_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeQualityDSLParser#comparison_expr}.
	 * @param ctx the parse tree
	 */
	void exitComparison_expr(CodeQualityDSLParser.Comparison_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link CodeQualityDSLParser#operator}.
	 * @param ctx the parse tree
	 */
	void enterOperator(CodeQualityDSLParser.OperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CodeQualityDSLParser#operator}.
	 * @param ctx the parse tree
	 */
	void exitOperator(CodeQualityDSLParser.OperatorContext ctx);
}