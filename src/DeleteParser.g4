parser grammar DeleteParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser;
delete_statement
    : DELETE top_clause? FROM? table_source output_clause? (FROM?  table_source)? delete_where_clause? SEMI?
    ;

  
delete_where_clause
    : WHERE search_condition
    | WHERE CURRENT OF cursor_name
    ;

output_clause
    : OUTPUT output_item (COMMA output_item)* output_into_clause?
    ;

output_into_clause
    : INTO table_variable
    ;

output_item
    : DELETED DOT STAR
    | DELETED DOT IDENTIFIER
    | full_column_name
    ;

table_variable
    : USER_VARIABLE
    ;