parser grammar selectParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser;

select_statement:
	SELECT select_list FROM table_source where_clause? SEMI?;

select_list: STAR | column (COMMA column)*;