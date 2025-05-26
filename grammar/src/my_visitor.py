# src/my_visitor.py
import re
import os, sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from generated.ExprParser import ExprParser
from generated.ExprVisitor import ExprVisitor

class MyVisitor(ExprVisitor):
    
    def __init__(self, listener):
        super().__init__()
        self.python_lines = []
        self.indent_level = 0
        self.var_types = {}
        self.listener = listener
        
    def normalize_bool_literals(self, text: str) -> str:
        """Reemplaza 'true'/'false' (cualquier mayúscula/minúscula) por True/False."""
        # Primero false → False, luego true → True
        text = re.sub(r'\bfalse\b', 'False', text, flags=re.IGNORECASE)
        return re.sub(r'\btrue\b', 'True', text, flags=re.IGNORECASE)

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
        # Determinar tipo
        if ctx.TYPE_INT():
            typ = 'i'
            init_token = ctx.NUM()
        elif ctx.TYPE_FLOAT():
            typ = 'f'
            init_token = ctx.FLOAT()
        elif ctx.TYPE_STRING():
            typ = 's'
            init_token = ctx.STRING()
        elif ctx.TYPE_BOOL():
            typ = 'b'
            init_token = ctx.BOOL()
        else:
            typ = None
            init_token = None

        name = ctx.ID().getText()
        self.var_types[name] = typ
        
        if typ == 'b' and init_token:
            raw = init_token.getText().lower()
            value = 'True' if raw == 'true' else 'False'

        # Valor inicial opcional
        if init_token:
            value = init_token.getText()
            if typ == 'b':
                value = 'True' if value.lower() == 'true' else 'False'
        else:
            if typ == 'i':   value = '0'
            elif typ == 'f': value = '0.0'
            elif typ == 's': value = '""'
            elif typ == 'b': value = 'False'
            else:
                value = 'None'

        self.emit(f"{name} = {value}")
        return self.visitChildren(ctx)

    def visitAsignacion(self, ctx: ExprParser.AsignacionContext):
        name = ctx.ID().getText()
        expr_ctx = ctx.expresion()
        expr_text = self.normalize_bool_literals(expr_ctx.getText())
    
        # Inferir tipo de la expresion
        expr_t = self.infer_type(expr_ctx)
    
        # Si ya existia en el var_types, comparar
        if name in self.var_types:
            declared_t = self.var_types[name]
            if declared_t != expr_t:
                linea = ctx.start.line
                
                print(f"Error semantico (linea {linea}): "
                       f"no puedes asignar un '{expr_t}' a '{name}' de tipo '{declared_t}'")
                self.listener.has_error = True
                return None
        else:
            # si no existia, lo declaramos implicitamente
            self.var_types[name] = expr_t
    
        # Emitir linea de Python
        self.emit(f"{name} = {expr_text}")
        return None

    def visitExpresionInstruccion(self, ctx: ExprParser.ExpresionInstruccionContext):
        print("Visiting: expresionInstruccion", ctx.getText())
        return self.visitChildren(ctx)

    def infer_type(self, ctx):
        """Devuelve 'i','f','s' o 'b' segun el nodo ctx."""
        # literal entero
        if hasattr(ctx, 'NUM') and ctx.NUM():
            return 'i'
        # literal float
        if hasattr(ctx, 'FLOAT') and ctx.FLOAT():
            return 'f'
        # literal string
        if hasattr(ctx, 'STRING') and ctx.STRING():
            return 's'
        # literal bool
        if hasattr(ctx, 'BOOL') and ctx.BOOL():
            return 'b'
        # identificador
        if hasattr(ctx, 'ID') and ctx.ID():
            name = ctx.ID().getText()
            return self.var_types.get(name)
        # descendemos en Termino1Context
        if hasattr(ctx, 'factor1') and ctx.factor1():
            return self.infer_type(ctx.factor1(0))
        # descendemos en ExpresionContext
        if hasattr(ctx, 'termino1') and ctx.termino1():
            return self.infer_type(ctx.termino1(0))

        # paretesis -> desciende
        if hasattr(ctx, 'expresion') and ctx.expression():
            return self.infer_type(ctx.expresion())

    def visitExpresion(self, ctx: ExprParser.ExpresionContext):
        # log
        print("Visiting: expresion", ctx.getText())
        # ahora, chequeo de suma/resta
        if len(ctx.termino1()) > 1:
            # puede haber varias sumas encadenadas: chequear cada par
            for i in range(1, len(ctx.termino1())):
                left, right = ctx.termino1(i-1), ctx.termino1(1)
                lt = self.infer_type(left)
                rt = self.infer_type(right)
                if lt is not None and rt is not None and lt != rt:
                    linea = ctx.start.line
                    print(f"Error semantico (linea {linea}): no se puede sumar/restar '{lt}' con '{rt}'")
                    self.listener.has_error = True
                    # cortamos la visita de esta rama
                    return None
        return self.visitChildren(ctx)
    

    def visitTermino1(self, ctx: ExprParser.Termino1Context):
        print("Visiting: termino1", ctx.getText())
        return self.visitChildren(ctx)

    def visitFactor1(self, ctx: ExprParser.Factor1Context):
        print("Visiting: factor1", ctx.getText())
        # chequeo semantico: ID declarada
        return self.visitChildren(ctx)

    def visitRelacional(self, ctx: ExprParser.RelacionalContext):
        print("Visiting: relacional", ctx.getText())
        return self.visitChildren(ctx)

    def visitControl(self, ctx: ExprParser.ControlContext):
        print("Visiting: control (if/else)", ctx.getText())
        cond = self.normalize_bool_literals(ctx.relacional().getText())
        self.emit(f"if {cond}:")
        self.indent_level += 1
        self.visit(ctx.bloque(0))
        self.indent_level -= 1

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
        args = [e.getText() for e in ctx.argumentos().expresion()] if ctx.argumentos() else []
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
        typ = self.var_types.get(var, 's')
        
        if typ == 'i':
            self.emit(f"{var} = int(input())")
        elif typ == 'f':
            self.emit(f"{var} = float(input())")
        elif typ == 'b':
            self.emit(f"{var} = input().strip().lower() in ('true','1')")
        else:
            self.emit(f"{var} = input()")
        return self.visitChildren(ctx)
    
    def visitOutput(self, ctx: ExprParser.OutputContext):
        print("Visiting: output", ctx.getText())
        self.visit(ctx.expresion())
        expr = self.normalize_bool_literals(ctx.expresion().getText())
        self.emit(f"print({expr})")
        return None