grammar MiLenguaje;

//Inicio de programa. Start Rule = programa
programa : sentencia* EOF;

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
declaracion : tipo ID ('=' valor)? ';' ;
asignacion : ID '=' expresion ';' ;
expresionInstruccion : expresion ';' ;

tipo : 'i' | 'f' | 's' | 'b' ;
valor : NUM | FLOAT | STRING | BOOL ;

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
    : ID
    | STRING
    | NUM
    | FLOAT
    | '(' expresion ')'
    | llamadaFuncionSinPuntoYComa
    ;

relacional : expresion DESI expresion ;

control : 'if' '(' relacional ')' '{' bloque '}' ('else' '{' bloque '}')? ;

/*
Control fue simplificado
<Control> ::= if ( <R> ) { <P> } <Control'>
<Control'> ::= else { <P> } 
	     | ε
*/

whileLoop : 'while' '(' relacional ')' '{' bloque '}' ;

funcion : 'def' ID '(' parametros ')' '{' bloque '}' ;
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

retorno : 'return' expresion ';' ;
input : 'read' '(' ID ')' ';' ;
output : 'write' '(' expresion ')' ';' ;

// Reglas léxicas combinadas
ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
NUM    : [0-9]+ ;
FLOAT  : [0-9]+ '.' [0-9]+ ;
STRING : '"' ( '\\' . | ~["\\\r\n] )* '"' ;
BOOL   : 'true' | 'false' ;
DESI   : '>' | '<' | '>=' | '<=' | '==' | '!=' ;

WS     : [ \t\r\n]+ -> skip ;