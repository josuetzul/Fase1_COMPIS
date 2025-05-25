grammar Expr;

//Inicio de programa. Start Rule = programa
prog : sentencia* EOF;

sentencia
    : declaracion
    | asignacion
    | expresionInstruccion
    | funcion
    | control
    | whileLoop
    | input
    | output
    | llamadaFuncion
    | retorno
    ;

bloque : sentencia* ;

//Se agregaron asignacion y expresionInstruccion

// 2. Declaraciones con inicializador opcional
declaracion
    : TYPE_INT    ID ( '=' NUM )?     ';'  
    | TYPE_FLOAT  ID ( '=' FLOAT )?     ';'
    | TYPE_STRING ID ( '=' STRING )?    ';'
    | TYPE_BOOL   ID ( '=' BOOL )?      ';'
    ;


asignacion : ID '=' expresion ';' ;
expresionInstruccion : expresion ';' ;

tipo : TYPE_INT | TYPE_FLOAT | TYPE_STRING | TYPE_BOOL ;

expresion : termino1 (('+' | '-') termino1)* ;

/*
expresion ::= termino1 expresion2
expresion2 ::= + termino1 expresion2
       | - termino1 expresion2 
       | ε
*/

termino1  : factor1 (('*' | '/') factor1)* ;

/*
termino1 ::= factor1 termino2
termino1 ::= * factor1 termino2 
       | / factor1 termino2 
       | ε
*/

factor1
    : BOOL
    | STRING
    | NUM
    | FLOAT
    | ID
    | '(' expresion ')'
    | llamadaFuncionSinPuntoYComa
    ;

relacional : expresion DESI expresion ;

control : IF '(' relacional ')' '{' bloque '}' ('else' '{' bloque '}')? ;

/*
Control fue simplificado
<Control> ::= if ( <R> ) { <P> } <Control'>
<Control'> ::= else { <P> } 
	     | ε
*/

whileLoop : WHILE '(' relacional ')' '{' bloque '}' ;

funcion : DEF ID '(' parametros ')' '{' bloque '}' ;
parametros : (tipo ID) (',' tipo ID)* ;

/*
<Params> ::= <B> id <ParamList> 
           | ε
<ParamList> ::= , <B> id <ParamList> 
              | ε
*/

llamadaFuncion : llamadaFuncionSinPuntoYComa ';' ;
llamadaFuncionSinPuntoYComa : ID '(' (argumentos)? ')' ;
argumentos : expresion (',' expresion)* ;

/*
SinPuntoYComa es útil para llamar funcion dentro del read y write

<LlamadaFuncion> ::= id ( <Args> ) ;
<Args> ::= <E> <ArgList> 
         | ε
<ArgList> ::= , <E> <ArgList> 
            | ε
*/

retorno : RETURN expresion ';' ;
input : READ '(' ID ')' ';' ;
output : WRITE '(' expresion ')' ';' ;

// Reglas léxicas combinadas

// 1) Números, strings, operadores, espacios...
NUM    : [0-9]+ ;
FLOAT  : [0-9]+ '.' [0-9]+ ;
STRING : '"' ( '\\' . | ~["\\\r\n] )* '"' ;
BOOL   : 'true' | 'false' ;
DESI   : '>' | '<' | '>=' | '<=' | '==' | '!=' ;

// 2) Palabras clave
IF          : 'if' ;
ELSE        : 'else' ;
WHILE       : 'while' ;
DEF         : 'def' ;
RETURN      : 'return' ;
READ        : 'read' ;
WRITE       : 'write' ;

//3) Tokens de tipo (con lookahead para asegurarse de que NO formen parte de un identificador más largo)
TYPE_INT    : 'i' ~[a-zA-Z_0-9] ;
TYPE_FLOAT  : 'f' ~[a-zA-Z_0-9] ;
TYPE_STRING : 's' ~[a-zA-Z_0-9] ;
TYPE_BOOL   : 'b' ~[a-zA-Z_0-9] ;

ID
    : [a-zA-Z_][a-zA-Z_0-9]* ;

WS     : [ \t\r\n]+ -> skip ;