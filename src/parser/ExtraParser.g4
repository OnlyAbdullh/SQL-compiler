parser grammar ExtraParser;
options {
	tokenVocab = SQLLexer;
}

user_variable : USER_VARIABLE;

identifier: IDENTIFIER;