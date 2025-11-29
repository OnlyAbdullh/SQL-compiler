import sys
from antlr4 import FileStream
from generated.SQLLexer import SQLLexer



def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file.sql>")
        return

    input_stream = FileStream(sys.argv[1], encoding='utf-8')

    lexer = SQLLexer(input_stream)

    tokens = lexer.getAllTokens()
    
    for token in tokens:
        print(token)
        token_name = lexer.symbolicNames[token.type]
        print(f"{token_name:15} -> {token.text}\n")

    

if __name__ == "__main__":
    main()
