# Generated from grammar/Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#sentencia.
    def enterSentencia(self, ctx:ExprParser.SentenciaContext):
        pass

    # Exit a parse tree produced by ExprParser#sentencia.
    def exitSentencia(self, ctx:ExprParser.SentenciaContext):
        pass


    # Enter a parse tree produced by ExprParser#bloque.
    def enterBloque(self, ctx:ExprParser.BloqueContext):
        pass

    # Exit a parse tree produced by ExprParser#bloque.
    def exitBloque(self, ctx:ExprParser.BloqueContext):
        pass


    # Enter a parse tree produced by ExprParser#declaracion.
    def enterDeclaracion(self, ctx:ExprParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by ExprParser#declaracion.
    def exitDeclaracion(self, ctx:ExprParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by ExprParser#asignacion.
    def enterAsignacion(self, ctx:ExprParser.AsignacionContext):
        pass

    # Exit a parse tree produced by ExprParser#asignacion.
    def exitAsignacion(self, ctx:ExprParser.AsignacionContext):
        pass


    # Enter a parse tree produced by ExprParser#expresionInstruccion.
    def enterExpresionInstruccion(self, ctx:ExprParser.ExpresionInstruccionContext):
        pass

    # Exit a parse tree produced by ExprParser#expresionInstruccion.
    def exitExpresionInstruccion(self, ctx:ExprParser.ExpresionInstruccionContext):
        pass


    # Enter a parse tree produced by ExprParser#tipo.
    def enterTipo(self, ctx:ExprParser.TipoContext):
        pass

    # Exit a parse tree produced by ExprParser#tipo.
    def exitTipo(self, ctx:ExprParser.TipoContext):
        pass


    # Enter a parse tree produced by ExprParser#valor.
    def enterValor(self, ctx:ExprParser.ValorContext):
        pass

    # Exit a parse tree produced by ExprParser#valor.
    def exitValor(self, ctx:ExprParser.ValorContext):
        pass


    # Enter a parse tree produced by ExprParser#expresion.
    def enterExpresion(self, ctx:ExprParser.ExpresionContext):
        pass

    # Exit a parse tree produced by ExprParser#expresion.
    def exitExpresion(self, ctx:ExprParser.ExpresionContext):
        pass


    # Enter a parse tree produced by ExprParser#termino1.
    def enterTermino1(self, ctx:ExprParser.Termino1Context):
        pass

    # Exit a parse tree produced by ExprParser#termino1.
    def exitTermino1(self, ctx:ExprParser.Termino1Context):
        pass


    # Enter a parse tree produced by ExprParser#factor1.
    def enterFactor1(self, ctx:ExprParser.Factor1Context):
        pass

    # Exit a parse tree produced by ExprParser#factor1.
    def exitFactor1(self, ctx:ExprParser.Factor1Context):
        pass


    # Enter a parse tree produced by ExprParser#relacional.
    def enterRelacional(self, ctx:ExprParser.RelacionalContext):
        pass

    # Exit a parse tree produced by ExprParser#relacional.
    def exitRelacional(self, ctx:ExprParser.RelacionalContext):
        pass


    # Enter a parse tree produced by ExprParser#control.
    def enterControl(self, ctx:ExprParser.ControlContext):
        pass

    # Exit a parse tree produced by ExprParser#control.
    def exitControl(self, ctx:ExprParser.ControlContext):
        pass


    # Enter a parse tree produced by ExprParser#whileLoop.
    def enterWhileLoop(self, ctx:ExprParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by ExprParser#whileLoop.
    def exitWhileLoop(self, ctx:ExprParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by ExprParser#funcion.
    def enterFuncion(self, ctx:ExprParser.FuncionContext):
        pass

    # Exit a parse tree produced by ExprParser#funcion.
    def exitFuncion(self, ctx:ExprParser.FuncionContext):
        pass


    # Enter a parse tree produced by ExprParser#parametros.
    def enterParametros(self, ctx:ExprParser.ParametrosContext):
        pass

    # Exit a parse tree produced by ExprParser#parametros.
    def exitParametros(self, ctx:ExprParser.ParametrosContext):
        pass


    # Enter a parse tree produced by ExprParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:ExprParser.LlamadaFuncionContext):
        pass

    # Exit a parse tree produced by ExprParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:ExprParser.LlamadaFuncionContext):
        pass


    # Enter a parse tree produced by ExprParser#llamadaFuncionSinPuntoYComa.
    def enterLlamadaFuncionSinPuntoYComa(self, ctx:ExprParser.LlamadaFuncionSinPuntoYComaContext):
        pass

    # Exit a parse tree produced by ExprParser#llamadaFuncionSinPuntoYComa.
    def exitLlamadaFuncionSinPuntoYComa(self, ctx:ExprParser.LlamadaFuncionSinPuntoYComaContext):
        pass


    # Enter a parse tree produced by ExprParser#argumentos.
    def enterArgumentos(self, ctx:ExprParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by ExprParser#argumentos.
    def exitArgumentos(self, ctx:ExprParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by ExprParser#retorno.
    def enterRetorno(self, ctx:ExprParser.RetornoContext):
        pass

    # Exit a parse tree produced by ExprParser#retorno.
    def exitRetorno(self, ctx:ExprParser.RetornoContext):
        pass


    # Enter a parse tree produced by ExprParser#input.
    def enterInput(self, ctx:ExprParser.InputContext):
        pass

    # Exit a parse tree produced by ExprParser#input.
    def exitInput(self, ctx:ExprParser.InputContext):
        pass


    # Enter a parse tree produced by ExprParser#output.
    def enterOutput(self, ctx:ExprParser.OutputContext):
        pass

    # Exit a parse tree produced by ExprParser#output.
    def exitOutput(self, ctx:ExprParser.OutputContext):
        pass



del ExprParser