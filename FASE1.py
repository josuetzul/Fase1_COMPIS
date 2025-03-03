import re

def load_file(file_path):
    """
    Lee un archivo de texto y devuelve su contenido como una única cadena.
    Se eliminan los espacios en blanco al inicio y final de cada línea antes de concatenarlas.
    
    :param file_path: Ruta del archivo a leer.
    :return: Contenido del archivo como una sola cadena de texto.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return " ".join(line.strip() for line in f.readlines())

# Definición de tokens con prioridad en palabras clave
TOKEN_REGEX = {
    'READ': re.compile(r'\bread\b'),      # Palabra clave 'read'
    'WRITE': re.compile(r'\bwrite\b'),    # Palabra clave 'write'
    'IF': re.compile(r'\bif\b'),          # Palabra clave 'if'
    'ELSE': re.compile(r'\belse\b'),      # Palabra clave 'else'
    'WHILE': re.compile(r'\bwhile\b'),    # Palabra clave 'while'
    'DEF': re.compile(r'\bdef\b'),        # Palabra clave 'def' (definición de función)
    'RETURN': re.compile(r'\breturn\b'),  # Palabra clave 'return'
    'BOOL': re.compile(r'\bTrue\b|\bFalse\b'),  # Valores booleanos 'True' o 'False'
    'DESI': re.compile(r'==|!=|<=|>=|<|>'),  # Operadores de comparación
    'FLOAT': re.compile(r'\d+\.\d+'),     # Números de punto flotante
    'NUM': re.compile(r'\b\d+\b'),        # Números enteros
    'STRING': re.compile(r'"[^"]*"'),     # Cadenas de texto entre comillas dobles
    'TYPE': re.compile(r'\bi\b|\bf\b|\bs\b|\bb\b'),  # Tipos de datos (i: entero, f: float, s: string, b: booleano)
    'ID': re.compile(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),  # Identificadores (variables, nombres de funciones)
    'EQUAL': re.compile(r'='),              # Signo de asignación '='
    'OP': re.compile(r'[+\-*/]'),          # Operadores aritméticos '+', '-', '*', '/'
    'LPAREN': re.compile(r'\('),           # Paréntesis izquierdo '('
    'RPAREN': re.compile(r'\)'),           # Paréntesis derecho ')'
    'LBRACE': re.compile(r'\{'),           # Llave izquierda '{'
    'RBRACE': re.compile(r'\}'),           # Llave derecha '}'
    'COMMA': re.compile(r','),              # Coma ','
    'SEMICOLON': re.compile(r';')           # Punto y coma ';'
}

def lexer(input_text):
    """
    Analizador léxico (lexer) que toma un código fuente como entrada y lo convierte en una lista de tokens.
    
    :param input_text: Código fuente a analizar.
    :return: Lista de tokens representados como tuplas (tipo de token, valor).
    """
    tokens = []
    while input_text:
        input_text = input_text.lstrip()  # Eliminar espacios en blanco iniciales
        matched = False
        
        # Intentar hacer coincidir la entrada con los patrones de los tokens
        for token_type, pattern in TOKEN_REGEX.items():
            match = pattern.match(input_text)
            if match:
                tokens.append((token_type, match.group(0)))
                input_text = input_text[match.end():]  # Avanzar en la cadena de entrada
                matched = True
                break
        
        # Si no hay coincidencia, lanzar un error léxico
        if not matched:
            raise SyntaxError(f"Error léxico en: {input_text}")
    
    tokens.append(('EOF', ''))  # Agregar token de fin de archivo
    return tokens

def main():
    """
    Función principal que solicita al usuario la ruta de un archivo,
    lee su contenido y genera los tokens utilizando el lexer.
    """
    file_path = input("Ingrese la ruta del archivo con el código de prueba: ").strip()
    try:
        code = load_file(file_path)
        tokens = lexer(code)
        print("Tokens generados:")
        for token in tokens:
            print(token)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()