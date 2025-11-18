// Generated from c:/Users/ihsan/Documents/GitHub/Quality-Code-Checker/grammar/CodeQualityDSL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class CodeQualityDSLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, AND=24, OR=25, 
		NOT=26, IDENTIFIER=27, NUMBER=28, STRING=29, WS=30, COMMENT=31;
	public static final int
		RULE_program = 0, RULE_rule_definition = 1, RULE_rule_body = 2, RULE_rule_attribute = 3, 
		RULE_target_type = 4, RULE_severity_level = 5, RULE_condition_expr = 6, 
		RULE_comparison_expr = 7, RULE_operator = 8;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "rule_definition", "rule_body", "rule_attribute", "target_type", 
			"severity_level", "condition_expr", "comparison_expr", "operator"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'rule'", "'{'", "'}'", "'target'", "':'", "'condition'", "'severity'", 
			"'message'", "'function'", "'class'", "'variable'", "'import'", "'error'", 
			"'warning'", "'info'", "'('", "')'", "'>'", "'<'", "'>='", "'<='", "'=='", 
			"'!='", "'AND'", "'OR'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"AND", "OR", "NOT", "IDENTIFIER", "NUMBER", "STRING", "WS", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "CodeQualityDSL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CodeQualityDSLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(CodeQualityDSLParser.EOF, 0); }
		public List<Rule_definitionContext> rule_definition() {
			return getRuleContexts(Rule_definitionContext.class);
		}
		public Rule_definitionContext rule_definition(int i) {
			return getRuleContext(Rule_definitionContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(19); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(18);
				rule_definition();
				}
				}
				setState(21); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__0 );
			setState(23);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Rule_definitionContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(CodeQualityDSLParser.STRING, 0); }
		public Rule_bodyContext rule_body() {
			return getRuleContext(Rule_bodyContext.class,0);
		}
		public Rule_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rule_definition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).enterRule_definition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).exitRule_definition(this);
		}
	}

	public final Rule_definitionContext rule_definition() throws RecognitionException {
		Rule_definitionContext _localctx = new Rule_definitionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_rule_definition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(25);
			match(T__0);
			setState(26);
			match(STRING);
			setState(27);
			match(T__1);
			setState(28);
			rule_body();
			setState(29);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Rule_bodyContext extends ParserRuleContext {
		public List<Rule_attributeContext> rule_attribute() {
			return getRuleContexts(Rule_attributeContext.class);
		}
		public Rule_attributeContext rule_attribute(int i) {
			return getRuleContext(Rule_attributeContext.class,i);
		}
		public Rule_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rule_body; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).enterRule_body(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).exitRule_body(this);
		}
	}

	public final Rule_bodyContext rule_body() throws RecognitionException {
		Rule_bodyContext _localctx = new Rule_bodyContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_rule_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(31);
				rule_attribute();
				}
				}
				setState(34); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 464L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Rule_attributeContext extends ParserRuleContext {
		public Target_typeContext target_type() {
			return getRuleContext(Target_typeContext.class,0);
		}
		public Condition_exprContext condition_expr() {
			return getRuleContext(Condition_exprContext.class,0);
		}
		public Severity_levelContext severity_level() {
			return getRuleContext(Severity_levelContext.class,0);
		}
		public TerminalNode STRING() { return getToken(CodeQualityDSLParser.STRING, 0); }
		public Rule_attributeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rule_attribute; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).enterRule_attribute(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).exitRule_attribute(this);
		}
	}

	public final Rule_attributeContext rule_attribute() throws RecognitionException {
		Rule_attributeContext _localctx = new Rule_attributeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_rule_attribute);
		try {
			setState(48);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				enterOuterAlt(_localctx, 1);
				{
				setState(36);
				match(T__3);
				setState(37);
				match(T__4);
				setState(38);
				target_type();
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 2);
				{
				setState(39);
				match(T__5);
				setState(40);
				match(T__4);
				setState(41);
				condition_expr(0);
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 3);
				{
				setState(42);
				match(T__6);
				setState(43);
				match(T__4);
				setState(44);
				severity_level();
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 4);
				{
				setState(45);
				match(T__7);
				setState(46);
				match(T__4);
				setState(47);
				match(STRING);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Target_typeContext extends ParserRuleContext {
		public Target_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_target_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).enterTarget_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).exitTarget_type(this);
		}
	}

	public final Target_typeContext target_type() throws RecognitionException {
		Target_typeContext _localctx = new Target_typeContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_target_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7680L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Severity_levelContext extends ParserRuleContext {
		public Severity_levelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_severity_level; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).enterSeverity_level(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).exitSeverity_level(this);
		}
	}

	public final Severity_levelContext severity_level() throws RecognitionException {
		Severity_levelContext _localctx = new Severity_levelContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_severity_level);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 57344L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Condition_exprContext extends ParserRuleContext {
		public Condition_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition_expr; }
	 
		public Condition_exprContext() { }
		public void copyFrom(Condition_exprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonConditionContext extends Condition_exprContext {
		public Comparison_exprContext comparison_expr() {
			return getRuleContext(Comparison_exprContext.class,0);
		}
		public ComparisonConditionContext(Condition_exprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).enterComparisonCondition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).exitComparisonCondition(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IdentifierConditionContext extends Condition_exprContext {
		public TerminalNode IDENTIFIER() { return getToken(CodeQualityDSLParser.IDENTIFIER, 0); }
		public IdentifierConditionContext(Condition_exprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).enterIdentifierCondition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).exitIdentifierCondition(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NotConditionContext extends Condition_exprContext {
		public TerminalNode NOT() { return getToken(CodeQualityDSLParser.NOT, 0); }
		public Condition_exprContext condition_expr() {
			return getRuleContext(Condition_exprContext.class,0);
		}
		public NotConditionContext(Condition_exprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).enterNotCondition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).exitNotCondition(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParenConditionContext extends Condition_exprContext {
		public Condition_exprContext condition_expr() {
			return getRuleContext(Condition_exprContext.class,0);
		}
		public ParenConditionContext(Condition_exprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).enterParenCondition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).exitParenCondition(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallConditionContext extends Condition_exprContext {
		public TerminalNode IDENTIFIER() { return getToken(CodeQualityDSLParser.IDENTIFIER, 0); }
		public TerminalNode STRING() { return getToken(CodeQualityDSLParser.STRING, 0); }
		public FunctionCallConditionContext(Condition_exprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).enterFunctionCallCondition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).exitFunctionCallCondition(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OrConditionContext extends Condition_exprContext {
		public List<Condition_exprContext> condition_expr() {
			return getRuleContexts(Condition_exprContext.class);
		}
		public Condition_exprContext condition_expr(int i) {
			return getRuleContext(Condition_exprContext.class,i);
		}
		public TerminalNode OR() { return getToken(CodeQualityDSLParser.OR, 0); }
		public OrConditionContext(Condition_exprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).enterOrCondition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).exitOrCondition(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AndConditionContext extends Condition_exprContext {
		public List<Condition_exprContext> condition_expr() {
			return getRuleContexts(Condition_exprContext.class);
		}
		public Condition_exprContext condition_expr(int i) {
			return getRuleContext(Condition_exprContext.class,i);
		}
		public TerminalNode AND() { return getToken(CodeQualityDSLParser.AND, 0); }
		public AndConditionContext(Condition_exprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).enterAndCondition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).exitAndCondition(this);
		}
	}

	public final Condition_exprContext condition_expr() throws RecognitionException {
		return condition_expr(0);
	}

	private Condition_exprContext condition_expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Condition_exprContext _localctx = new Condition_exprContext(_ctx, _parentState);
		Condition_exprContext _prevctx = _localctx;
		int _startState = 12;
		enterRecursionRule(_localctx, 12, RULE_condition_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				_localctx = new ComparisonConditionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(55);
				comparison_expr();
				}
				break;
			case 2:
				{
				_localctx = new NotConditionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(56);
				match(NOT);
				setState(57);
				condition_expr(4);
				}
				break;
			case 3:
				{
				_localctx = new ParenConditionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(58);
				match(T__15);
				setState(59);
				condition_expr(0);
				setState(60);
				match(T__16);
				}
				break;
			case 4:
				{
				_localctx = new FunctionCallConditionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(62);
				match(IDENTIFIER);
				setState(63);
				match(T__15);
				setState(64);
				match(STRING);
				setState(65);
				match(T__16);
				}
				break;
			case 5:
				{
				_localctx = new IdentifierConditionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(66);
				match(IDENTIFIER);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(77);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(75);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new AndConditionContext(new Condition_exprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_condition_expr);
						setState(69);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(70);
						match(AND);
						setState(71);
						condition_expr(7);
						}
						break;
					case 2:
						{
						_localctx = new OrConditionContext(new Condition_exprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_condition_expr);
						setState(72);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(73);
						match(OR);
						setState(74);
						condition_expr(6);
						}
						break;
					}
					} 
				}
				setState(79);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Comparison_exprContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(CodeQualityDSLParser.IDENTIFIER, 0); }
		public OperatorContext operator() {
			return getRuleContext(OperatorContext.class,0);
		}
		public TerminalNode NUMBER() { return getToken(CodeQualityDSLParser.NUMBER, 0); }
		public Comparison_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).enterComparison_expr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).exitComparison_expr(this);
		}
	}

	public final Comparison_exprContext comparison_expr() throws RecognitionException {
		Comparison_exprContext _localctx = new Comparison_exprContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_comparison_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			match(IDENTIFIER);
			setState(81);
			operator();
			setState(82);
			match(NUMBER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperatorContext extends ParserRuleContext {
		public OperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).enterOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CodeQualityDSLListener ) ((CodeQualityDSLListener)listener).exitOperator(this);
		}
	}

	public final OperatorContext operator() throws RecognitionException {
		OperatorContext _localctx = new OperatorContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 16515072L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 6:
			return condition_expr_sempred((Condition_exprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean condition_expr_sempred(Condition_exprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 6);
		case 1:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001fW\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0001\u0000\u0004\u0000\u0014\b\u0000\u000b\u0000\f\u0000\u0015"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0004\u0002!\b\u0002\u000b\u0002"+
		"\f\u0002\"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0003\u00031\b\u0003\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0003\u0006D\b\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0005\u0006L\b\u0006"+
		"\n\u0006\f\u0006O\t\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\b\u0000\u0001\f\t\u0000\u0002\u0004\u0006\b\n\f"+
		"\u000e\u0010\u0000\u0003\u0001\u0000\t\f\u0001\u0000\r\u000f\u0001\u0000"+
		"\u0012\u0017X\u0000\u0013\u0001\u0000\u0000\u0000\u0002\u0019\u0001\u0000"+
		"\u0000\u0000\u0004 \u0001\u0000\u0000\u0000\u00060\u0001\u0000\u0000\u0000"+
		"\b2\u0001\u0000\u0000\u0000\n4\u0001\u0000\u0000\u0000\fC\u0001\u0000"+
		"\u0000\u0000\u000eP\u0001\u0000\u0000\u0000\u0010T\u0001\u0000\u0000\u0000"+
		"\u0012\u0014\u0003\u0002\u0001\u0000\u0013\u0012\u0001\u0000\u0000\u0000"+
		"\u0014\u0015\u0001\u0000\u0000\u0000\u0015\u0013\u0001\u0000\u0000\u0000"+
		"\u0015\u0016\u0001\u0000\u0000\u0000\u0016\u0017\u0001\u0000\u0000\u0000"+
		"\u0017\u0018\u0005\u0000\u0000\u0001\u0018\u0001\u0001\u0000\u0000\u0000"+
		"\u0019\u001a\u0005\u0001\u0000\u0000\u001a\u001b\u0005\u001d\u0000\u0000"+
		"\u001b\u001c\u0005\u0002\u0000\u0000\u001c\u001d\u0003\u0004\u0002\u0000"+
		"\u001d\u001e\u0005\u0003\u0000\u0000\u001e\u0003\u0001\u0000\u0000\u0000"+
		"\u001f!\u0003\u0006\u0003\u0000 \u001f\u0001\u0000\u0000\u0000!\"\u0001"+
		"\u0000\u0000\u0000\" \u0001\u0000\u0000\u0000\"#\u0001\u0000\u0000\u0000"+
		"#\u0005\u0001\u0000\u0000\u0000$%\u0005\u0004\u0000\u0000%&\u0005\u0005"+
		"\u0000\u0000&1\u0003\b\u0004\u0000\'(\u0005\u0006\u0000\u0000()\u0005"+
		"\u0005\u0000\u0000)1\u0003\f\u0006\u0000*+\u0005\u0007\u0000\u0000+,\u0005"+
		"\u0005\u0000\u0000,1\u0003\n\u0005\u0000-.\u0005\b\u0000\u0000./\u0005"+
		"\u0005\u0000\u0000/1\u0005\u001d\u0000\u00000$\u0001\u0000\u0000\u0000"+
		"0\'\u0001\u0000\u0000\u00000*\u0001\u0000\u0000\u00000-\u0001\u0000\u0000"+
		"\u00001\u0007\u0001\u0000\u0000\u000023\u0007\u0000\u0000\u00003\t\u0001"+
		"\u0000\u0000\u000045\u0007\u0001\u0000\u00005\u000b\u0001\u0000\u0000"+
		"\u000067\u0006\u0006\uffff\uffff\u00007D\u0003\u000e\u0007\u000089\u0005"+
		"\u001a\u0000\u00009D\u0003\f\u0006\u0004:;\u0005\u0010\u0000\u0000;<\u0003"+
		"\f\u0006\u0000<=\u0005\u0011\u0000\u0000=D\u0001\u0000\u0000\u0000>?\u0005"+
		"\u001b\u0000\u0000?@\u0005\u0010\u0000\u0000@A\u0005\u001d\u0000\u0000"+
		"AD\u0005\u0011\u0000\u0000BD\u0005\u001b\u0000\u0000C6\u0001\u0000\u0000"+
		"\u0000C8\u0001\u0000\u0000\u0000C:\u0001\u0000\u0000\u0000C>\u0001\u0000"+
		"\u0000\u0000CB\u0001\u0000\u0000\u0000DM\u0001\u0000\u0000\u0000EF\n\u0006"+
		"\u0000\u0000FG\u0005\u0018\u0000\u0000GL\u0003\f\u0006\u0007HI\n\u0005"+
		"\u0000\u0000IJ\u0005\u0019\u0000\u0000JL\u0003\f\u0006\u0006KE\u0001\u0000"+
		"\u0000\u0000KH\u0001\u0000\u0000\u0000LO\u0001\u0000\u0000\u0000MK\u0001"+
		"\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000N\r\u0001\u0000\u0000\u0000"+
		"OM\u0001\u0000\u0000\u0000PQ\u0005\u001b\u0000\u0000QR\u0003\u0010\b\u0000"+
		"RS\u0005\u001c\u0000\u0000S\u000f\u0001\u0000\u0000\u0000TU\u0007\u0002"+
		"\u0000\u0000U\u0011\u0001\u0000\u0000\u0000\u0006\u0015\"0CKM";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}