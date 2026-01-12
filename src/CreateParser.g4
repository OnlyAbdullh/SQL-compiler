parser grammar CreateParser;

options { tokenVocab = SQLLexer; }

import BasicParser;

create_statement
    : create_table
    | create_index
    ;

create_table
    : CREATE TABLE full_table_name create_table_body SEMI?
    ;

create_table_body
    : LPAREN create_table_element_list RPAREN
    ;

create_table_element_list
    : create_table_element (COMMA create_table_element)*
    ;

create_table_element
    : column_definition
    | table_constraint
    ;

create_index
    : CREATE UNIQUE? index_clustering? INDEX index_name
      ON full_table_name index_column_list
      include_clause?
      where_clause_for_index?
      index_with_clause?
      SEMI?
    ;

index_clustering
    : CLUSTERED
    | NONCLUSTERED
    ;

index_column_list
    : LPAREN index_column (COMMA index_column)* RPAREN;

index_column
    : full_column_name (ASC | DESC)?;

include_clause
    : INCLUDE LPAREN full_column_name (COMMA full_column_name)* RPAREN;

where_clause_for_index
    : WHERE search_condition;
index_with_clause
    : WITH LPAREN index_option (COMMA index_option)* RPAREN;

index_option
    : PAD_INDEX EQ (ON | OFF)
    | FILLFACTOR EQ expression
    | IGNORE_DUP_KEY EQ (ON | OFF)
    | ALLOW_ROW_LOCKS EQ (ON | OFF)
    | ALLOW_PAGE_LOCKS EQ (ON | OFF)
    ;
