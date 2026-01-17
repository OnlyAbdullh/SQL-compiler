parser grammar VariableParser;


options {
	tokenVocab = SQLLexer;
}


import BasicParser, CursorParser,ExtraParser;

declare_var: DECLARE declare_var_list SEMI?;

declare_var_list:declare_var_item (COMMA declare_var_item)* ;

declare_var_item:user_variable ((AS? datatype (EQ expression)?) | CURSOR | (AS? table_type_definition));



set_variable: SET (select_set_variable_item | (user_variable EQ (user_variable | cursor_name | set_declare_cursor_item ))) SEMI?;

select_set_variable_item: user_variable (EQ | PLUS_EQ | MINUS_EQ | STAR_EQ | SLASH_EQ | PERCENT_EQ| AMPERSAND_EQ | CARET_EQ | PIPE_EQ) expression;

