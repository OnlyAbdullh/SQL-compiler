parser grammar DeleteParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser;
delete_statement
    : DELETE top_clause? FROM? table_source where_clause? SEMI?
    ;

top_clause
    : TOP LPAREN add_sub_expression RPAREN PERCENT?
    ;