%{ 
	#include<stdio.h>
	#include<stdlib.h>
	int yylex();
	int yyerror();
%}


%token PUBLIC INTERFACE IDENTIFIER VOID TYPE SEMI OPEN CLOSE SOPEN SCLOSE EXTENDS;

%%

S: E {printf("interface declared succussfully\n"); exit(0);}

E: PUBLIC INTERFACE IDENTIFIER A OPEN BODY CLOSE;

A: EXTENDS IDENTIFIER
	|
	;

BODY: BODY PUBLIC return IDENTIFIER SOPEN PARAM SCLOSE SEMI
	| 
	;
	
return: TYPE
	| VOID
	;
	
PARAM: PARAM ',' TYPE IDENTIFIER
	| TYPE IDENTIFIER
	|
	;
%%

int yyerror()
{
	printf("Error encountered in the module");
	return 1;
}

int main()
{
	printf("Enter Java Interface Module: \n");
	yyparse();
	return 0;
}
