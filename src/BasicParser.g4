parser grammar basicParser;

options {
	tokenVocab = SQLLexer;
}

import ExpressionParser;

table_source
    : object_name
    ;

column
    : object_name
    ;

where_clause: WHERE search_condition;
 
object_name
    : IDENTIFIER (DOT IDENTIFIER)*
    ;
 
 






 
