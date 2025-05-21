import os, sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from generated.ExprParser import ExprParser
from generated.ExprVisitor import ExprVisitor

class MyVisitor(ExprVisitor):
    
    def __init__(self):
        super().__init__()
        self.python_lines = []
        self.indent_level = 0
        self.var_types = {}
        
    def emit(self, line: str):
        """Agregar una linea con la identacion actual."""
        indent = '    ' * self.indent_level
        self.python_lines.append(f"{indent}{line}")
    
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
        name = ctx.ID().getText()
        typ  = ctx.tipo().getText()
        self.var_types[name] = typ

        if ctx.valor():
            value = ctx.valor().getText()
        else:
            if typ == 'i':   value = '0'
            elif typ == 'f': value = '0.0'
            elif typ == 's': value = '""'
            else:            value = 'False'
        self.emit(f"{name} = {value}")
        return self.visitChildren(ctx)

    def visitAsignacion(self, ctx: ExprParser.AsignacionContext):
        print("Visiting: asignacion", ctx.getText())
        name = ctx.ID().getText()
        expr = ctx.expresion().getText()
        self.emit(f"{name} = {expr}")
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
        cond = ctx.relacional().getText()
        # if
        self.emit(f"if {cond}:")
        self.indent_level += 1
        self.visit(ctx.bloque(0))
        self.indent_level -= 1

        # else?
        if len(ctx.bloque()) > 1:
            self.emit("else:")
            self.indent_level += 1
            self.visit(ctx.bloque(1))
            self.indent_level -= 1

        return None

    def visitWhileLoop(self, ctx: ExprParser.WhileLoopContext):
        print("Visiting: whileLoop", ctx.getText())
        cond = ctx.relacional().getText()
        self.emit(f"while {cond}:")
        self.indent_level += 1
        self.visit(ctx.bloque())
        self.indent_level -= 1
        return None

    def visitFuncion(self, ctx: ExprParser.FuncionContext):
        print("Visiting: funcion", ctx.getText())
        name = ctx.ID().getText()
        param_names = [i.getText() for i in ctx.parametros().ID()]
        params_str  = ", ".join(param_names)

        self.emit(f"def {name}({params_str}):")
        self.indent_level += 1
        self.visit(ctx.bloque())
        self.indent_level -= 1
        return None

    def visitParametros(self, ctx: ExprParser.ParametrosContext):
        print("Visiting: parametros", ctx.getText())
        return self.visitChildren(ctx)

    def visitLlamadaFuncion(self, ctx: ExprParser.LlamadaFuncionContext):
        print("Visiting: llamadaFuncion", ctx.getText())
        name = ctx.ID().getText()
        args = []
        if ctx.argumentos():
            args = [e.getText() for e in ctx.argumentos().expresion()]
        self.emit(f"{name}({', '.join(args)})")
        return self.visitChildren(ctx)

    def visitLlamadaFuncionSinPuntoYComa(self, ctx: ExprParser.LlamadaFuncionSinPuntoYComaContext):
        print("Visiting: llamadaFuncionSinPuntoYComa", ctx.getText())
        return self.visitChildren(ctx)

    def visitArgumentos(self, ctx: ExprParser.ArgumentosContext):
        print("Visiting: argumentos", ctx.getText())
        return self.visitChildren(ctx)

    def visitRetorno(self, ctx: ExprParser.RetornoContext):
        print("Visiting: retorno", ctx.getText())
        expr = ctx.expresion().getText()
        self.emit(f"return {expr}")
        return self.visitChildren(ctx)

    def visitInput(self, ctx: ExprParser.InputContext):
        print("Visiting: input", ctx.getText())
        var = ctx.ID().getText()
        typ = self.var_types.get(var, 's')  # si no esta declarado, asumimos string
        
        if typ == 'i':
            self.emit(f"{var} = int(input())")
        elif typ == 'f':
            self.emit(f"{var} = float(input())")
        elif typ == 'b':
            self.emit(f"{var} = input().strip().lower() in ('true','1')")
            self.emit(f"{var} = input()")
        return self.visitChildren(ctx)

    def visitOutput(self, ctx: ExprParser.OutputContext):
        print("Visiting: output", ctx.getText())
        expr = ctx.expresion().getText()
        self.emit(f"print({expr})")
        return self.visitChildren(ctx)