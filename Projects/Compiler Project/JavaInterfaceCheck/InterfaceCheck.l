%{
#include <stdio.h>
#include "y.tab.h"
extern int yylval;
%}

alpha [A-Za-z]
digit [0-9]
%%
public  						return PUBLIC;
interface						return INTERFACE;
void							return VOID;
int|float|char|String			return TYPE;
{alpha}({alpha}|{digit})*		return IDENTIFIER;
"{"								return OPEN;
"}"								return CLOSE;
"("								return SOPEN;
")"								return SCLOSE;
";"								return SEMI;
[ \t\n]+						/* ignore whitespace */;
.								return yytext[0];
%%


int yywrap()
{
	return 1;
}
