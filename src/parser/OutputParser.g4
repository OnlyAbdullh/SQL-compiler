parser grammar OutputParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser,ExtraParser,ExtraParser;


output_clause: OUTPUT output_select_list (INTO output_into_clause)?;

output_select_list: output_select_list_item (COMMA output_select_list_item)*;
output_select_list_item: expression | ((identifier|INSERTED|DELETED) DOT STAR as_alias?) ;

output_into_clause
    : user_variable | full_table_name column_list?
    ;

