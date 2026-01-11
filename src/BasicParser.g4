parser grammar basicParser;

options {
	tokenVocab = SQLLexer;
}

import ExpressionParser;

table_source: IDENTIFIER;

column: IDENTIFIER;

where_clause: WHERE search_condition;
 
object_name : IDENTIFIER (DOT IDENTIFIER)*; 

