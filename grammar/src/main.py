# src/main.py

import os, sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from generated.ExprLexer  import ExprLexer
from generated.ExprParser import ExprParser
from src.my_visitor       import MyVisitor

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.has_error = False

    def syntaxError(self, recognizer, offendingSymbol, line, col, msg, e):
        print(f"Error sintactico en linea {line}, columna {col}: {msg}")
        self.has_error = True

def parse_and_visit(file_path):
    input_stream = FileStream(file_path, encoding='utf-8')
    lexer = ExprLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)
    parser.removeErrorListeners()
    listener = SyntaxErrorListener()
    parser.addErrorListener(listener)
    tree = parser.prog()
    if listener.has_error:
        return
    print(tree.toStringTree(recog=parser))
    visitor = MyVisitor(listener)
    visitor.visit(tree)
    
    # Nombre base del archivo de entrada (sin extension)
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    # Ruta de salida en la raiz del proyecto
    output_path = os.path.join(project_root, f'{base_name}_output.py')

    # Escribir el codigo Python en el archivo
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in visitor.python_lines:
            f.write(line + '\n')

    # Mostrar ruta en consola
    print(f"\n Codigo Python generado en: {output_path}")

if __name__ == "__main__":
    tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tests'))

    if len(sys.argv) == 2:
        chosen = sys.argv[1]
    else:
        # Listar todos los tests
        files = sorted(f for f in os.listdir(tests_dir) if f.endswith('.txt'))
        print("Elige el test a ejecutar:")
        for i, f in enumerate(files):
            print(f"  {i+1}) {f}")
        sel = input("> ")
        try:
            idx = int(sel) - 1
            chosen = files[idx]
        except:
            print("Seleccion invalida. Saliendo.")
            sys.exit(1)

    test_path = os.path.join(tests_dir, chosen)
    print(f"\n Ejecutando prueba: {chosen}\n")
    parse_and_visit(test_path)