# Generated from grammar/Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#sentencia.
    def visitSentencia(self, ctx:ExprParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bloque.
    def visitBloque(self, ctx:ExprParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#declaracion.
    def visitDeclaracion(self, ctx:ExprParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#asignacion.
    def visitAsignacion(self, ctx:ExprParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expresionInstruccion.
    def visitExpresionInstruccion(self, ctx:ExprParser.ExpresionInstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tipo.
    def visitTipo(self, ctx:ExprParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#valor.
    def visitValor(self, ctx:ExprParser.ValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expresion.
    def visitExpresion(self, ctx:ExprParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#termino1.
    def visitTermino1(self, ctx:ExprParser.Termino1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#factor1.
    def visitFactor1(self, ctx:ExprParser.Factor1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#relacional.
    def visitRelacional(self, ctx:ExprParser.RelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#control.
    def visitControl(self, ctx:ExprParser.ControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#whileLoop.
    def visitWhileLoop(self, ctx:ExprParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#funcion.
    def visitFuncion(self, ctx:ExprParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parametros.
    def visitParametros(self, ctx:ExprParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#llamadaFuncion.
    def visitLlamadaFuncion(self, ctx:ExprParser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#llamadaFuncionSinPuntoYComa.
    def visitLlamadaFuncionSinPuntoYComa(self, ctx:ExprParser.LlamadaFuncionSinPuntoYComaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#argumentos.
    def visitArgumentos(self, ctx:ExprParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#retorno.
    def visitRetorno(self, ctx:ExprParser.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#input.
    def visitInput(self, ctx:ExprParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#output.
    def visitOutput(self, ctx:ExprParser.OutputContext):
        return self.visitChildren(ctx)



del ExprParser