# SQL-Compiler
  use this command to generated the lexer 
  ```shell
  antlr4 src/SQLLexer.g4 -Dlanguage=Python3 -o .\generated\

  python -m src.main inputFile

  python -m src.main .\queries\test1.sql  
  ```