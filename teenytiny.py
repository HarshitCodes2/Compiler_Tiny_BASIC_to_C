from lex import *


def main():
    source = "a = 12"
    lexer = Lexer(source)
    token = lexer.getToken()
    
    while token.kind != TokenType.EOF:
        print(token.text + ' -> ', token.kind)
        token = lexer.getToken()
       

main()
