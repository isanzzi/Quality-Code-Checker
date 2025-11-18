# Generated from CodeQualityDSL.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,87,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,2,4,2,33,8,2,11,2,12,2,34,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,49,8,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,68,8,6,1,6,1,6,1,6,1,
        6,1,6,1,6,5,6,76,8,6,10,6,12,6,79,9,6,1,7,1,7,1,7,1,7,1,8,1,8,1,
        8,0,1,12,9,0,2,4,6,8,10,12,14,16,0,3,1,0,9,12,1,0,13,15,1,0,18,23,
        88,0,19,1,0,0,0,2,25,1,0,0,0,4,32,1,0,0,0,6,48,1,0,0,0,8,50,1,0,
        0,0,10,52,1,0,0,0,12,67,1,0,0,0,14,80,1,0,0,0,16,84,1,0,0,0,18,20,
        3,2,1,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,
        22,23,1,0,0,0,23,24,5,0,0,1,24,1,1,0,0,0,25,26,5,1,0,0,26,27,5,29,
        0,0,27,28,5,2,0,0,28,29,3,4,2,0,29,30,5,3,0,0,30,3,1,0,0,0,31,33,
        3,6,3,0,32,31,1,0,0,0,33,34,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,
        35,5,1,0,0,0,36,37,5,4,0,0,37,38,5,5,0,0,38,49,3,8,4,0,39,40,5,6,
        0,0,40,41,5,5,0,0,41,49,3,12,6,0,42,43,5,7,0,0,43,44,5,5,0,0,44,
        49,3,10,5,0,45,46,5,8,0,0,46,47,5,5,0,0,47,49,5,29,0,0,48,36,1,0,
        0,0,48,39,1,0,0,0,48,42,1,0,0,0,48,45,1,0,0,0,49,7,1,0,0,0,50,51,
        7,0,0,0,51,9,1,0,0,0,52,53,7,1,0,0,53,11,1,0,0,0,54,55,6,6,-1,0,
        55,68,3,14,7,0,56,57,5,26,0,0,57,68,3,12,6,4,58,59,5,16,0,0,59,60,
        3,12,6,0,60,61,5,17,0,0,61,68,1,0,0,0,62,63,5,27,0,0,63,64,5,16,
        0,0,64,65,5,29,0,0,65,68,5,17,0,0,66,68,5,27,0,0,67,54,1,0,0,0,67,
        56,1,0,0,0,67,58,1,0,0,0,67,62,1,0,0,0,67,66,1,0,0,0,68,77,1,0,0,
        0,69,70,10,6,0,0,70,71,5,24,0,0,71,76,3,12,6,7,72,73,10,5,0,0,73,
        74,5,25,0,0,74,76,3,12,6,6,75,69,1,0,0,0,75,72,1,0,0,0,76,79,1,0,
        0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,13,1,0,0,0,79,77,1,0,0,0,80,81,
        5,27,0,0,81,82,3,16,8,0,82,83,5,28,0,0,83,15,1,0,0,0,84,85,7,2,0,
        0,85,17,1,0,0,0,6,21,34,48,67,75,77
    ]

class CodeQualityDSLParser ( Parser ):

    grammarFileName = "CodeQualityDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'rule'", "'{'", "'}'", "'target'", "':'", 
                     "'condition'", "'severity'", "'message'", "'function'", 
                     "'class'", "'variable'", "'import'", "'error'", "'warning'", 
                     "'info'", "'('", "')'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'!='", "'AND'", "'OR'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "AND", "OR", "NOT", "IDENTIFIER", "NUMBER", "STRING", 
                      "WS", "COMMENT" ]

    RULE_program = 0
    RULE_rule_definition = 1
    RULE_rule_body = 2
    RULE_rule_attribute = 3
    RULE_target_type = 4
    RULE_severity_level = 5
    RULE_condition_expr = 6
    RULE_comparison_expr = 7
    RULE_operator = 8

    ruleNames =  [ "program", "rule_definition", "rule_body", "rule_attribute", 
                   "target_type", "severity_level", "condition_expr", "comparison_expr", 
                   "operator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    AND=24
    OR=25
    NOT=26
    IDENTIFIER=27
    NUMBER=28
    STRING=29
    WS=30
    COMMENT=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CodeQualityDSLParser.EOF, 0)

        def rule_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CodeQualityDSLParser.Rule_definitionContext)
            else:
                return self.getTypedRuleContext(CodeQualityDSLParser.Rule_definitionContext,i)


        def getRuleIndex(self):
            return CodeQualityDSLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CodeQualityDSLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.rule_definition()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 23
            self.match(CodeQualityDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CodeQualityDSLParser.STRING, 0)

        def rule_body(self):
            return self.getTypedRuleContext(CodeQualityDSLParser.Rule_bodyContext,0)


        def getRuleIndex(self):
            return CodeQualityDSLParser.RULE_rule_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_definition" ):
                listener.enterRule_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_definition" ):
                listener.exitRule_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_definition" ):
                return visitor.visitRule_definition(self)
            else:
                return visitor.visitChildren(self)




    def rule_definition(self):

        localctx = CodeQualityDSLParser.Rule_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_rule_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(CodeQualityDSLParser.T__0)
            self.state = 26
            self.match(CodeQualityDSLParser.STRING)
            self.state = 27
            self.match(CodeQualityDSLParser.T__1)
            self.state = 28
            self.rule_body()
            self.state = 29
            self.match(CodeQualityDSLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rule_attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CodeQualityDSLParser.Rule_attributeContext)
            else:
                return self.getTypedRuleContext(CodeQualityDSLParser.Rule_attributeContext,i)


        def getRuleIndex(self):
            return CodeQualityDSLParser.RULE_rule_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_body" ):
                listener.enterRule_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_body" ):
                listener.exitRule_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_body" ):
                return visitor.visitRule_body(self)
            else:
                return visitor.visitChildren(self)




    def rule_body(self):

        localctx = CodeQualityDSLParser.Rule_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_rule_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 31
                self.rule_attribute()
                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 464) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def target_type(self):
            return self.getTypedRuleContext(CodeQualityDSLParser.Target_typeContext,0)


        def condition_expr(self):
            return self.getTypedRuleContext(CodeQualityDSLParser.Condition_exprContext,0)


        def severity_level(self):
            return self.getTypedRuleContext(CodeQualityDSLParser.Severity_levelContext,0)


        def STRING(self):
            return self.getToken(CodeQualityDSLParser.STRING, 0)

        def getRuleIndex(self):
            return CodeQualityDSLParser.RULE_rule_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_attribute" ):
                listener.enterRule_attribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_attribute" ):
                listener.exitRule_attribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_attribute" ):
                return visitor.visitRule_attribute(self)
            else:
                return visitor.visitChildren(self)




    def rule_attribute(self):

        localctx = CodeQualityDSLParser.Rule_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_rule_attribute)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(CodeQualityDSLParser.T__3)
                self.state = 37
                self.match(CodeQualityDSLParser.T__4)
                self.state = 38
                self.target_type()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(CodeQualityDSLParser.T__5)
                self.state = 40
                self.match(CodeQualityDSLParser.T__4)
                self.state = 41
                self.condition_expr(0)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.match(CodeQualityDSLParser.T__6)
                self.state = 43
                self.match(CodeQualityDSLParser.T__4)
                self.state = 44
                self.severity_level()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.match(CodeQualityDSLParser.T__7)
                self.state = 46
                self.match(CodeQualityDSLParser.T__4)
                self.state = 47
                self.match(CodeQualityDSLParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Target_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CodeQualityDSLParser.RULE_target_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTarget_type" ):
                listener.enterTarget_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTarget_type" ):
                listener.exitTarget_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTarget_type" ):
                return visitor.visitTarget_type(self)
            else:
                return visitor.visitChildren(self)




    def target_type(self):

        localctx = CodeQualityDSLParser.Target_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_target_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Severity_levelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CodeQualityDSLParser.RULE_severity_level

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeverity_level" ):
                listener.enterSeverity_level(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeverity_level" ):
                listener.exitSeverity_level(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeverity_level" ):
                return visitor.visitSeverity_level(self)
            else:
                return visitor.visitChildren(self)




    def severity_level(self):

        localctx = CodeQualityDSLParser.Severity_levelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_severity_level)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CodeQualityDSLParser.RULE_condition_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ComparisonConditionContext(Condition_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CodeQualityDSLParser.Condition_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comparison_expr(self):
            return self.getTypedRuleContext(CodeQualityDSLParser.Comparison_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonCondition" ):
                listener.enterComparisonCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonCondition" ):
                listener.exitComparisonCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonCondition" ):
                return visitor.visitComparisonCondition(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierConditionContext(Condition_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CodeQualityDSLParser.Condition_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(CodeQualityDSLParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierCondition" ):
                listener.enterIdentifierCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierCondition" ):
                listener.exitIdentifierCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierCondition" ):
                return visitor.visitIdentifierCondition(self)
            else:
                return visitor.visitChildren(self)


    class NotConditionContext(Condition_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CodeQualityDSLParser.Condition_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(CodeQualityDSLParser.NOT, 0)
        def condition_expr(self):
            return self.getTypedRuleContext(CodeQualityDSLParser.Condition_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotCondition" ):
                listener.enterNotCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotCondition" ):
                listener.exitNotCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotCondition" ):
                return visitor.visitNotCondition(self)
            else:
                return visitor.visitChildren(self)


    class ParenConditionContext(Condition_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CodeQualityDSLParser.Condition_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condition_expr(self):
            return self.getTypedRuleContext(CodeQualityDSLParser.Condition_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenCondition" ):
                listener.enterParenCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenCondition" ):
                listener.exitParenCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenCondition" ):
                return visitor.visitParenCondition(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallConditionContext(Condition_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CodeQualityDSLParser.Condition_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(CodeQualityDSLParser.IDENTIFIER, 0)
        def STRING(self):
            return self.getToken(CodeQualityDSLParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallCondition" ):
                listener.enterFunctionCallCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallCondition" ):
                listener.exitFunctionCallCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallCondition" ):
                return visitor.visitFunctionCallCondition(self)
            else:
                return visitor.visitChildren(self)


    class OrConditionContext(Condition_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CodeQualityDSLParser.Condition_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condition_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CodeQualityDSLParser.Condition_exprContext)
            else:
                return self.getTypedRuleContext(CodeQualityDSLParser.Condition_exprContext,i)

        def OR(self):
            return self.getToken(CodeQualityDSLParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrCondition" ):
                listener.enterOrCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrCondition" ):
                listener.exitOrCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrCondition" ):
                return visitor.visitOrCondition(self)
            else:
                return visitor.visitChildren(self)


    class AndConditionContext(Condition_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CodeQualityDSLParser.Condition_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condition_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CodeQualityDSLParser.Condition_exprContext)
            else:
                return self.getTypedRuleContext(CodeQualityDSLParser.Condition_exprContext,i)

        def AND(self):
            return self.getToken(CodeQualityDSLParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndCondition" ):
                listener.enterAndCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndCondition" ):
                listener.exitAndCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndCondition" ):
                return visitor.visitAndCondition(self)
            else:
                return visitor.visitChildren(self)



    def condition_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CodeQualityDSLParser.Condition_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_condition_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = CodeQualityDSLParser.ComparisonConditionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 55
                self.comparison_expr()
                pass

            elif la_ == 2:
                localctx = CodeQualityDSLParser.NotConditionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 56
                self.match(CodeQualityDSLParser.NOT)
                self.state = 57
                self.condition_expr(4)
                pass

            elif la_ == 3:
                localctx = CodeQualityDSLParser.ParenConditionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 58
                self.match(CodeQualityDSLParser.T__15)
                self.state = 59
                self.condition_expr(0)
                self.state = 60
                self.match(CodeQualityDSLParser.T__16)
                pass

            elif la_ == 4:
                localctx = CodeQualityDSLParser.FunctionCallConditionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 62
                self.match(CodeQualityDSLParser.IDENTIFIER)
                self.state = 63
                self.match(CodeQualityDSLParser.T__15)
                self.state = 64
                self.match(CodeQualityDSLParser.STRING)
                self.state = 65
                self.match(CodeQualityDSLParser.T__16)
                pass

            elif la_ == 5:
                localctx = CodeQualityDSLParser.IdentifierConditionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 66
                self.match(CodeQualityDSLParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 75
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = CodeQualityDSLParser.AndConditionContext(self, CodeQualityDSLParser.Condition_exprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 70
                        self.match(CodeQualityDSLParser.AND)
                        self.state = 71
                        self.condition_expr(7)
                        pass

                    elif la_ == 2:
                        localctx = CodeQualityDSLParser.OrConditionContext(self, CodeQualityDSLParser.Condition_exprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 73
                        self.match(CodeQualityDSLParser.OR)
                        self.state = 74
                        self.condition_expr(6)
                        pass

             
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Comparison_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CodeQualityDSLParser.IDENTIFIER, 0)

        def operator(self):
            return self.getTypedRuleContext(CodeQualityDSLParser.OperatorContext,0)


        def NUMBER(self):
            return self.getToken(CodeQualityDSLParser.NUMBER, 0)

        def getRuleIndex(self):
            return CodeQualityDSLParser.RULE_comparison_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_expr" ):
                listener.enterComparison_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_expr" ):
                listener.exitComparison_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison_expr" ):
                return visitor.visitComparison_expr(self)
            else:
                return visitor.visitChildren(self)




    def comparison_expr(self):

        localctx = CodeQualityDSLParser.Comparison_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comparison_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(CodeQualityDSLParser.IDENTIFIER)
            self.state = 81
            self.operator()
            self.state = 82
            self.match(CodeQualityDSLParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CodeQualityDSLParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = CodeQualityDSLParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.condition_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def condition_expr_sempred(self, localctx:Condition_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




