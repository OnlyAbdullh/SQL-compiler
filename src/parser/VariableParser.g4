parser grammar VariableParser;


options {
	tokenVocab = SQLLexer;
}


import BasicParser, CursorParser;


declare_var: DECLARE declare_var_list SEMI?;
declare_var_list:declare_var_item (COMMA declare_var_item)* ;

declare_var_item:
        scalar_var| cursor_var| table_var;

scalar_var: USER_VARIABLE AS? datatype (EQ expression)?;

cursor_var: USER_VARIABLE CURSOR;

table_var: USER_VARIABLE AS? table_type_definition;


// TODO : Complete from here

set_variable: SET (select_set_variable_item | (USER_VARIABLE EQ (USER_VARIABLE | cursor_name | set_declare_cursor_item ))) SEMI?;

select_set_variable_item: USER_VARIABLE (EQ | PLUS_EQ | MINUS_EQ | STAR_EQ | SLASH_EQ | PERCENT_EQ| AMPERSAND_EQ | CARET_EQ | PIPE_EQ) expression;
