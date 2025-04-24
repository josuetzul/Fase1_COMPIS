grammar Proyect;

s 	: p EOF;

p 	: declaracion p
	| function p
	| control p
	| while p
	| in p
	| out p
	| llamadaFuncion p
	| return p
	|
	;

declaracion	: b ID '=' v ';';
b			: 'i' | 'f' | 's' | 'b';
v			: NUM | FLOAT | STRING | BOOL ;

e		: t1 e_prime;

e_prime	: '+' t1 e_prime
		| '-' t1 e_prime
		|
		;

t1		: f1 t_prime;

t_prime : '*' f1 t_prime
		| '/' f1 t_prime
		|
		;
		
f1		: ID
		| STRING
		| NUM
		| FLOAT
		| '(' e ')'
		| llamadaFuncion
		;

r		: e DESI e;

control			: 'if' '(' r ')' '{' p '}' control_prime;

control_prime	: 'else' '{' p '}'
				|
				;
				
while			: 'while' '(' r ')' '{' p '}';
  
function		: 'def' ID '(' params ')' '{' p '}';

params			: b ID paramlist
				|
				;

paramlist		: ',' b ID paramlist
				|
				;

llamadaFuncion	: ID '(' args ')' ';';

args			: e arglist
				|
				;
arglist			: ',' e arglist
				|
				;

return			: 'return' e ';';

in 				: 'read' '(' ID ')' ';';
out				: 'write' '(' e ')' ';';

ID				: [a-zA-Z_][a-zA-Z0-9_]*;
NUM				: [0-9]+;
FLOAT			: [0-9]+ '.' [0-9]+;
STRING 			: '"' .*? '"';
BOOL			: 'true' | 'false';
DESI			: '<' | '>' | '<=' | '>=' | '==' | '!=';
WS : [ \t\r\n]+ -> skip;