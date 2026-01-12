parser grammar DeleteParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser;
import OutputParser;


delete_statement
    : DELETE top_clause? FROM? table_source output_clause? (FROM?  table_source)? delete_where_clause? SEMI?
    ;

  
delete_where_clause
    : WHERE search_condition
    | WHERE CURRENT OF cursor_name
    ;

