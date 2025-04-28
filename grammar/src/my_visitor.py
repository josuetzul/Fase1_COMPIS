import os, sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from generated.ExprParser import ExprParser
from generated.ExprVisitor import ExprVisitor

class MyVisitor(ExprVisitor):
    
    def visitProg(self, ctx: ExprParser.ProgContext):
        print("Visiting: prog", ctx.getText())
        return self.visitChildren(ctx)

    def visitSentencia(self, ctx: ExprParser.SentenciaContext):
        print("Visiting: sentencia", ctx.getText())
        return self.visitChildren(ctx)
    
    def visitBloque(self, ctx: ExprParser.BloqueContext):
        print("Visiting: bloque", ctx.getText())
        return self.visitChildren(ctx)

    def visitDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        print("Visiting: declaracion", ctx.getText())
        return self.visitChildren(ctx)

    def visitAsignacion(self, ctx: ExprParser.AsignacionContext):
        print("Visiting: asignacion", ctx.getText())
        return self.visitChildren(ctx)

    def visitExpresionInstruccion(self, ctx: ExprParser.ExpresionInstruccionContext):
        print("Visiting: expresionInstruccion", ctx.getText())
        return self.visitChildren(ctx)

    def visitTipo(self, ctx: ExprParser.TipoContext):
        print("Visiting: tipo", ctx.getText())
        return self.visitChildren(ctx)

    def visitValor(self, ctx: ExprParser.ValorContext):
        print("Visiting: valor", ctx.getText())
        return self.visitChildren(ctx)

    def visitExpresion(self, ctx: ExprParser.ExpresionContext):
        print("Visiting: expresion", ctx.getText())
        return self.visitChildren(ctx)

    def visitTermino1(self, ctx: ExprParser.Termino1Context):
        print("Visiting: termino1", ctx.getText())
        return self.visitChildren(ctx)

    def visitFactor1(self, ctx: ExprParser.Factor1Context):
        print("Visiting: factor1", ctx.getText())
        return self.visitChildren(ctx)

    def visitRelacional(self, ctx: ExprParser.RelacionalContext):
        print("Visiting: relacional", ctx.getText())
        return self.visitChildren(ctx)

    def visitControl(self, ctx: ExprParser.ControlContext):
        print("Visiting: control (if/else)", ctx.getText())
        return self.visitChildren(ctx)

    def visitWhileLoop(self, ctx: ExprParser.WhileLoopContext):
        print("Visiting: whileLoop", ctx.getText())
        return self.visitChildren(ctx)

    def visitFuncion(self, ctx: ExprParser.FuncionContext):
        print("Visiting: funcion", ctx.getText())
        return self.visitChildren(ctx)

    def visitParametros(self, ctx: ExprParser.ParametrosContext):
        print("Visiting: parametros", ctx.getText())
        return self.visitChildren(ctx)

    def visitLlamadaFuncion(self, ctx: ExprParser.LlamadaFuncionContext):
        print("Visiting: llamadaFuncion", ctx.getText())
        return self.visitChildren(ctx)

    def visitLlamadaFuncionSinPuntoYComa(self, ctx: ExprParser.LlamadaFuncionSinPuntoYComaContext):
        print("Visiting: llamadaFuncionSinPuntoYComa", ctx.getText())
        return self.visitChildren(ctx)

    def visitArgumentos(self, ctx: ExprParser.ArgumentosContext):
        print("Visiting: argumentos", ctx.getText())
        return self.visitChildren(ctx)

    def visitRetorno(self, ctx: ExprParser.RetornoContext):
        print("Visiting: retorno", ctx.getText())
        return self.visitChildren(ctx)

    def visitInput(self, ctx: ExprParser.InputContext):
        print("Visiting: input", ctx.getText())
        return self.visitChildren(ctx)

    def visitOutput(self, ctx: ExprParser.OutputContext):
        print("Visiting: output", ctx.getText())
        return self.visitChildren(ctx)