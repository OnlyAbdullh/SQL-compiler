parser grammar UpdateParser;
options {
	tokenVocab = SQLLexer;
}

import BasicParser,ExpressionParser;
update_statement :
UPDATE table_source SET assignment (COMMA assignment)* from_update_clause where_clause? SEMI? ;

from_update_clause:
	from_clause;
assignment :
	target EQ source ;

target : 
	column;

source :
	expression;

