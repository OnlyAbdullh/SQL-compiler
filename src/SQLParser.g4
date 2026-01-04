parser grammar SQLParser;

options {tokenVocab = SQLLexer;}

statments: ADD <EOF>;
