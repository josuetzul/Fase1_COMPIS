# Generated from grammar/Expr.g4 by ANTLR 4.13.2
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
        4,1,29,218,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,61,8,1,1,2,5,2,64,8,2,10,2,12,2,67,9,2,1,
        3,1,3,1,3,1,3,3,3,73,8,3,1,3,1,3,1,3,1,3,1,3,3,3,80,8,3,1,3,1,3,
        1,3,1,3,1,3,3,3,87,8,3,1,3,1,3,1,3,1,3,1,3,3,3,94,8,3,1,3,3,3,97,
        8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,5,7,112,
        8,7,10,7,12,7,115,9,7,1,8,1,8,1,8,5,8,120,8,8,10,8,12,8,123,9,8,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,135,8,9,1,10,1,10,1,
        10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,3,11,153,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,5,14,179,8,14,10,14,12,14,182,9,14,1,15,1,15,1,15,1,16,1,
        16,1,16,3,16,190,8,16,1,16,1,16,1,17,1,17,1,17,5,17,197,8,17,10,
        17,12,17,200,9,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,
        19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,0,0,21,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,0,3,1,0,24,27,1,0,3,4,1,0,
        5,6,226,0,45,1,0,0,0,2,60,1,0,0,0,4,65,1,0,0,0,6,96,1,0,0,0,8,98,
        1,0,0,0,10,103,1,0,0,0,12,106,1,0,0,0,14,108,1,0,0,0,16,116,1,0,
        0,0,18,134,1,0,0,0,20,136,1,0,0,0,22,140,1,0,0,0,24,154,1,0,0,0,
        26,162,1,0,0,0,28,171,1,0,0,0,30,183,1,0,0,0,32,186,1,0,0,0,34,193,
        1,0,0,0,36,201,1,0,0,0,38,205,1,0,0,0,40,211,1,0,0,0,42,44,3,2,1,
        0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,
        1,0,0,0,47,45,1,0,0,0,48,49,5,0,0,1,49,1,1,0,0,0,50,61,3,6,3,0,51,
        61,3,8,4,0,52,61,3,10,5,0,53,61,3,26,13,0,54,61,3,22,11,0,55,61,
        3,24,12,0,56,61,3,38,19,0,57,61,3,40,20,0,58,61,3,30,15,0,59,61,
        3,36,18,0,60,50,1,0,0,0,60,51,1,0,0,0,60,52,1,0,0,0,60,53,1,0,0,
        0,60,54,1,0,0,0,60,55,1,0,0,0,60,56,1,0,0,0,60,57,1,0,0,0,60,58,
        1,0,0,0,60,59,1,0,0,0,61,3,1,0,0,0,62,64,3,2,1,0,63,62,1,0,0,0,64,
        67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,5,1,0,0,0,67,65,1,0,0,
        0,68,69,5,24,0,0,69,72,5,28,0,0,70,71,5,1,0,0,71,73,5,12,0,0,72,
        70,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,97,5,2,0,0,75,76,5,25,
        0,0,76,79,5,28,0,0,77,78,5,1,0,0,78,80,5,13,0,0,79,77,1,0,0,0,79,
        80,1,0,0,0,80,81,1,0,0,0,81,97,5,2,0,0,82,83,5,26,0,0,83,86,5,28,
        0,0,84,85,5,1,0,0,85,87,5,14,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,
        88,1,0,0,0,88,97,5,2,0,0,89,90,5,27,0,0,90,93,5,28,0,0,91,92,5,1,
        0,0,92,94,5,15,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,95,1,0,0,0,95,
        97,5,2,0,0,96,68,1,0,0,0,96,75,1,0,0,0,96,82,1,0,0,0,96,89,1,0,0,
        0,97,7,1,0,0,0,98,99,5,28,0,0,99,100,5,1,0,0,100,101,3,14,7,0,101,
        102,5,2,0,0,102,9,1,0,0,0,103,104,3,14,7,0,104,105,5,2,0,0,105,11,
        1,0,0,0,106,107,7,0,0,0,107,13,1,0,0,0,108,113,3,16,8,0,109,110,
        7,1,0,0,110,112,3,16,8,0,111,109,1,0,0,0,112,115,1,0,0,0,113,111,
        1,0,0,0,113,114,1,0,0,0,114,15,1,0,0,0,115,113,1,0,0,0,116,121,3,
        18,9,0,117,118,7,2,0,0,118,120,3,18,9,0,119,117,1,0,0,0,120,123,
        1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,17,1,0,0,0,123,121,1,
        0,0,0,124,135,5,15,0,0,125,135,5,14,0,0,126,135,5,12,0,0,127,135,
        5,13,0,0,128,135,5,28,0,0,129,130,5,7,0,0,130,131,3,14,7,0,131,132,
        5,8,0,0,132,135,1,0,0,0,133,135,3,32,16,0,134,124,1,0,0,0,134,125,
        1,0,0,0,134,126,1,0,0,0,134,127,1,0,0,0,134,128,1,0,0,0,134,129,
        1,0,0,0,134,133,1,0,0,0,135,19,1,0,0,0,136,137,3,14,7,0,137,138,
        5,16,0,0,138,139,3,14,7,0,139,21,1,0,0,0,140,141,5,17,0,0,141,142,
        5,7,0,0,142,143,3,20,10,0,143,144,5,8,0,0,144,145,5,9,0,0,145,146,
        3,4,2,0,146,152,5,10,0,0,147,148,5,18,0,0,148,149,5,9,0,0,149,150,
        3,4,2,0,150,151,5,10,0,0,151,153,1,0,0,0,152,147,1,0,0,0,152,153,
        1,0,0,0,153,23,1,0,0,0,154,155,5,19,0,0,155,156,5,7,0,0,156,157,
        3,20,10,0,157,158,5,8,0,0,158,159,5,9,0,0,159,160,3,4,2,0,160,161,
        5,10,0,0,161,25,1,0,0,0,162,163,5,20,0,0,163,164,5,28,0,0,164,165,
        5,7,0,0,165,166,3,28,14,0,166,167,5,8,0,0,167,168,5,9,0,0,168,169,
        3,4,2,0,169,170,5,10,0,0,170,27,1,0,0,0,171,172,3,12,6,0,172,173,
        5,28,0,0,173,180,1,0,0,0,174,175,5,11,0,0,175,176,3,12,6,0,176,177,
        5,28,0,0,177,179,1,0,0,0,178,174,1,0,0,0,179,182,1,0,0,0,180,178,
        1,0,0,0,180,181,1,0,0,0,181,29,1,0,0,0,182,180,1,0,0,0,183,184,3,
        32,16,0,184,185,5,2,0,0,185,31,1,0,0,0,186,187,5,28,0,0,187,189,
        5,7,0,0,188,190,3,34,17,0,189,188,1,0,0,0,189,190,1,0,0,0,190,191,
        1,0,0,0,191,192,5,8,0,0,192,33,1,0,0,0,193,198,3,14,7,0,194,195,
        5,11,0,0,195,197,3,14,7,0,196,194,1,0,0,0,197,200,1,0,0,0,198,196,
        1,0,0,0,198,199,1,0,0,0,199,35,1,0,0,0,200,198,1,0,0,0,201,202,5,
        21,0,0,202,203,3,14,7,0,203,204,5,2,0,0,204,37,1,0,0,0,205,206,5,
        22,0,0,206,207,5,7,0,0,207,208,5,28,0,0,208,209,5,8,0,0,209,210,
        5,2,0,0,210,39,1,0,0,0,211,212,5,23,0,0,212,213,5,7,0,0,213,214,
        3,14,7,0,214,215,5,8,0,0,215,216,5,2,0,0,216,41,1,0,0,0,15,45,60,
        65,72,79,86,93,96,113,121,134,152,180,189,198
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'+'", "'-'", "'*'", "'/'", 
                     "'('", "')'", "'{'", "'}'", "','", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'if'", "'else'", 
                     "'while'", "'def'", "'return'", "'read'", "'write'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUM", "FLOAT", "STRING", "BOOL", "DESI", "IF", "ELSE", 
                      "WHILE", "DEF", "RETURN", "READ", "WRITE", "TYPE_INT", 
                      "TYPE_FLOAT", "TYPE_STRING", "TYPE_BOOL", "ID", "WS" ]

    RULE_prog = 0
    RULE_sentencia = 1
    RULE_bloque = 2
    RULE_declaracion = 3
    RULE_asignacion = 4
    RULE_expresionInstruccion = 5
    RULE_tipo = 6
    RULE_expresion = 7
    RULE_termino1 = 8
    RULE_factor1 = 9
    RULE_relacional = 10
    RULE_control = 11
    RULE_whileLoop = 12
    RULE_funcion = 13
    RULE_parametros = 14
    RULE_llamadaFuncion = 15
    RULE_llamadaFuncionSinPuntoYComa = 16
    RULE_argumentos = 17
    RULE_retorno = 18
    RULE_input = 19
    RULE_output = 20

    ruleNames =  [ "prog", "sentencia", "bloque", "declaracion", "asignacion", 
                   "expresionInstruccion", "tipo", "expresion", "termino1", 
                   "factor1", "relacional", "control", "whileLoop", "funcion", 
                   "parametros", "llamadaFuncion", "llamadaFuncionSinPuntoYComa", 
                   "argumentos", "retorno", "input", "output" ]

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
    NUM=12
    FLOAT=13
    STRING=14
    BOOL=15
    DESI=16
    IF=17
    ELSE=18
    WHILE=19
    DEF=20
    RETURN=21
    READ=22
    WRITE=23
    TYPE_INT=24
    TYPE_FLOAT=25
    TYPE_STRING=26
    TYPE_BOOL=27
    ID=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(ExprParser.SentenciaContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 536539264) != 0):
                self.state = 42
                self.sentencia()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(ExprParser.DeclaracionContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(ExprParser.AsignacionContext,0)


        def expresionInstruccion(self):
            return self.getTypedRuleContext(ExprParser.ExpresionInstruccionContext,0)


        def funcion(self):
            return self.getTypedRuleContext(ExprParser.FuncionContext,0)


        def control(self):
            return self.getTypedRuleContext(ExprParser.ControlContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(ExprParser.WhileLoopContext,0)


        def input_(self):
            return self.getTypedRuleContext(ExprParser.InputContext,0)


        def output(self):
            return self.getTypedRuleContext(ExprParser.OutputContext,0)


        def llamadaFuncion(self):
            return self.getTypedRuleContext(ExprParser.LlamadaFuncionContext,0)


        def retorno(self):
            return self.getTypedRuleContext(ExprParser.RetornoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = ExprParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.declaracion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.expresionInstruccion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.funcion()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.control()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 55
                self.whileLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 56
                self.input_()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 57
                self.output()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 58
                self.llamadaFuncion()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 59
                self.retorno()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(ExprParser.SentenciaContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = ExprParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 536539264) != 0):
                self.state = 62
                self.sentencia()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_INT(self):
            return self.getToken(ExprParser.TYPE_INT, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def TYPE_FLOAT(self):
            return self.getToken(ExprParser.TYPE_FLOAT, 0)

        def FLOAT(self):
            return self.getToken(ExprParser.FLOAT, 0)

        def TYPE_STRING(self):
            return self.getToken(ExprParser.TYPE_STRING, 0)

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def TYPE_BOOL(self):
            return self.getToken(ExprParser.TYPE_BOOL, 0)

        def BOOL(self):
            return self.getToken(ExprParser.BOOL, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = ExprParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracion)
        self._la = 0 # Token type
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(ExprParser.TYPE_INT)
                self.state = 69
                self.match(ExprParser.ID)
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 70
                    self.match(ExprParser.T__0)
                    self.state = 71
                    self.match(ExprParser.NUM)


                self.state = 74
                self.match(ExprParser.T__1)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(ExprParser.TYPE_FLOAT)
                self.state = 76
                self.match(ExprParser.ID)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 77
                    self.match(ExprParser.T__0)
                    self.state = 78
                    self.match(ExprParser.FLOAT)


                self.state = 81
                self.match(ExprParser.T__1)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.match(ExprParser.TYPE_STRING)
                self.state = 83
                self.match(ExprParser.ID)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 84
                    self.match(ExprParser.T__0)
                    self.state = 85
                    self.match(ExprParser.STRING)


                self.state = 88
                self.match(ExprParser.T__1)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                self.match(ExprParser.TYPE_BOOL)
                self.state = 90
                self.match(ExprParser.ID)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 91
                    self.match(ExprParser.T__0)
                    self.state = 92
                    self.match(ExprParser.BOOL)


                self.state = 95
                self.match(ExprParser.T__1)
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


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(ExprParser.ExpresionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = ExprParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(ExprParser.ID)
            self.state = 99
            self.match(ExprParser.T__0)
            self.state = 100
            self.expresion()
            self.state = 101
            self.match(ExprParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionInstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(ExprParser.ExpresionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expresionInstruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionInstruccion" ):
                listener.enterExpresionInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionInstruccion" ):
                listener.exitExpresionInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionInstruccion" ):
                return visitor.visitExpresionInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def expresionInstruccion(self):

        localctx = ExprParser.ExpresionInstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expresionInstruccion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.expresion()
            self.state = 104
            self.match(ExprParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_INT(self):
            return self.getToken(ExprParser.TYPE_INT, 0)

        def TYPE_FLOAT(self):
            return self.getToken(ExprParser.TYPE_FLOAT, 0)

        def TYPE_STRING(self):
            return self.getToken(ExprParser.TYPE_STRING, 0)

        def TYPE_BOOL(self):
            return self.getToken(ExprParser.TYPE_BOOL, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = ExprParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 251658240) != 0)):
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


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Termino1Context)
            else:
                return self.getTypedRuleContext(ExprParser.Termino1Context,i)


        def getRuleIndex(self):
            return ExprParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)




    def expresion(self):

        localctx = ExprParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.termino1()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 109
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 110
                self.termino1()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Termino1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Factor1Context)
            else:
                return self.getTypedRuleContext(ExprParser.Factor1Context,i)


        def getRuleIndex(self):
            return ExprParser.RULE_termino1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino1" ):
                listener.enterTermino1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino1" ):
                listener.exitTermino1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino1" ):
                return visitor.visitTermino1(self)
            else:
                return visitor.visitChildren(self)




    def termino1(self):

        localctx = ExprParser.Termino1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_termino1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.factor1()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 117
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 118
                self.factor1()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Factor1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ExprParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def FLOAT(self):
            return self.getToken(ExprParser.FLOAT, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(ExprParser.ExpresionContext,0)


        def llamadaFuncionSinPuntoYComa(self):
            return self.getTypedRuleContext(ExprParser.LlamadaFuncionSinPuntoYComaContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_factor1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor1" ):
                listener.enterFactor1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor1" ):
                listener.exitFactor1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor1" ):
                return visitor.visitFactor1(self)
            else:
                return visitor.visitChildren(self)




    def factor1(self):

        localctx = ExprParser.Factor1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_factor1)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(ExprParser.BOOL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(ExprParser.STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.match(ExprParser.NUM)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.match(ExprParser.FLOAT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.match(ExprParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 129
                self.match(ExprParser.T__6)
                self.state = 130
                self.expresion()
                self.state = 131
                self.match(ExprParser.T__7)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 133
                self.llamadaFuncionSinPuntoYComa()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpresionContext,i)


        def DESI(self):
            return self.getToken(ExprParser.DESI, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelacional" ):
                listener.enterRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelacional" ):
                listener.exitRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelacional" ):
                return visitor.visitRelacional(self)
            else:
                return visitor.visitChildren(self)




    def relacional(self):

        localctx = ExprParser.RelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_relacional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.expresion()
            self.state = 137
            self.match(ExprParser.DESI)
            self.state = 138
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ControlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def relacional(self):
            return self.getTypedRuleContext(ExprParser.RelacionalContext,0)


        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.BloqueContext)
            else:
                return self.getTypedRuleContext(ExprParser.BloqueContext,i)


        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_control

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterControl" ):
                listener.enterControl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitControl" ):
                listener.exitControl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControl" ):
                return visitor.visitControl(self)
            else:
                return visitor.visitChildren(self)




    def control(self):

        localctx = ExprParser.ControlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_control)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(ExprParser.IF)
            self.state = 141
            self.match(ExprParser.T__6)
            self.state = 142
            self.relacional()
            self.state = 143
            self.match(ExprParser.T__7)
            self.state = 144
            self.match(ExprParser.T__8)
            self.state = 145
            self.bloque()
            self.state = 146
            self.match(ExprParser.T__9)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 147
                self.match(ExprParser.ELSE)
                self.state = 148
                self.match(ExprParser.T__8)
                self.state = 149
                self.bloque()
                self.state = 150
                self.match(ExprParser.T__9)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)

        def relacional(self):
            return self.getTypedRuleContext(ExprParser.RelacionalContext,0)


        def bloque(self):
            return self.getTypedRuleContext(ExprParser.BloqueContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoop" ):
                return visitor.visitWhileLoop(self)
            else:
                return visitor.visitChildren(self)




    def whileLoop(self):

        localctx = ExprParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(ExprParser.WHILE)
            self.state = 155
            self.match(ExprParser.T__6)
            self.state = 156
            self.relacional()
            self.state = 157
            self.match(ExprParser.T__7)
            self.state = 158
            self.match(ExprParser.T__8)
            self.state = 159
            self.bloque()
            self.state = 160
            self.match(ExprParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(ExprParser.DEF, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def parametros(self):
            return self.getTypedRuleContext(ExprParser.ParametrosContext,0)


        def bloque(self):
            return self.getTypedRuleContext(ExprParser.BloqueContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)




    def funcion(self):

        localctx = ExprParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(ExprParser.DEF)
            self.state = 163
            self.match(ExprParser.ID)
            self.state = 164
            self.match(ExprParser.T__6)
            self.state = 165
            self.parametros()
            self.state = 166
            self.match(ExprParser.T__7)
            self.state = 167
            self.match(ExprParser.T__8)
            self.state = 168
            self.bloque()
            self.state = 169
            self.match(ExprParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.TipoContext)
            else:
                return self.getTypedRuleContext(ExprParser.TipoContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def getRuleIndex(self):
            return ExprParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = ExprParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.tipo()
            self.state = 172
            self.match(ExprParser.ID)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 174
                self.match(ExprParser.T__10)
                self.state = 175
                self.tipo()
                self.state = 176
                self.match(ExprParser.ID)
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaFuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def llamadaFuncionSinPuntoYComa(self):
            return self.getTypedRuleContext(ExprParser.LlamadaFuncionSinPuntoYComaContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_llamadaFuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamadaFuncion" ):
                listener.enterLlamadaFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamadaFuncion" ):
                listener.exitLlamadaFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaFuncion" ):
                return visitor.visitLlamadaFuncion(self)
            else:
                return visitor.visitChildren(self)




    def llamadaFuncion(self):

        localctx = ExprParser.LlamadaFuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_llamadaFuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.llamadaFuncionSinPuntoYComa()
            self.state = 184
            self.match(ExprParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaFuncionSinPuntoYComaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def argumentos(self):
            return self.getTypedRuleContext(ExprParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_llamadaFuncionSinPuntoYComa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamadaFuncionSinPuntoYComa" ):
                listener.enterLlamadaFuncionSinPuntoYComa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamadaFuncionSinPuntoYComa" ):
                listener.exitLlamadaFuncionSinPuntoYComa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaFuncionSinPuntoYComa" ):
                return visitor.visitLlamadaFuncionSinPuntoYComa(self)
            else:
                return visitor.visitChildren(self)




    def llamadaFuncionSinPuntoYComa(self):

        localctx = ExprParser.LlamadaFuncionSinPuntoYComaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_llamadaFuncionSinPuntoYComa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(ExprParser.ID)
            self.state = 187
            self.match(ExprParser.T__6)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 268497024) != 0):
                self.state = 188
                self.argumentos()


            self.state = 191
            self.match(ExprParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpresionContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = ExprParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.expresion()
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 194
                self.match(ExprParser.T__10)
                self.state = 195
                self.expresion()
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ExprParser.RETURN, 0)

        def expresion(self):
            return self.getTypedRuleContext(ExprParser.ExpresionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_retorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetorno" ):
                listener.enterRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetorno" ):
                listener.exitRetorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetorno" ):
                return visitor.visitRetorno(self)
            else:
                return visitor.visitChildren(self)




    def retorno(self):

        localctx = ExprParser.RetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_retorno)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(ExprParser.RETURN)
            self.state = 202
            self.expresion()
            self.state = 203
            self.match(ExprParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(ExprParser.READ, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput" ):
                listener.enterInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput" ):
                listener.exitInput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput" ):
                return visitor.visitInput(self)
            else:
                return visitor.visitChildren(self)




    def input_(self):

        localctx = ExprParser.InputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_input)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(ExprParser.READ)
            self.state = 206
            self.match(ExprParser.T__6)
            self.state = 207
            self.match(ExprParser.ID)
            self.state = 208
            self.match(ExprParser.T__7)
            self.state = 209
            self.match(ExprParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(ExprParser.WRITE, 0)

        def expresion(self):
            return self.getTypedRuleContext(ExprParser.ExpresionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput" ):
                return visitor.visitOutput(self)
            else:
                return visitor.visitChildren(self)




    def output(self):

        localctx = ExprParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_output)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(ExprParser.WRITE)
            self.state = 212
            self.match(ExprParser.T__6)
            self.state = 213
            self.expresion()
            self.state = 214
            self.match(ExprParser.T__7)
            self.state = 215
            self.match(ExprParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





