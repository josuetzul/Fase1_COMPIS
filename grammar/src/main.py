# src/main.py

import os, sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from antlr4 import FileStream, CommonTokenStream
from generated.ExprLexer  import ExprLexer
from generated.ExprParser import ExprParser
from src.my_visitor       import MyVisitor

def parse_and_visit(file_path):
    input_stream = FileStream(file_path, encoding='utf-8')
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    print(tree.toStringTree(recog=parser))
    visitor = MyVisitor()
    visitor.visit(tree)
    
    print("\n#Codigo Python resultante")
    for line in visitor.python_lines:
        print(line)

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

