
from ChainOfResp import *


def parserUnificado():
# Set up the chain
    handler = Handler()
    ll1_parser = LL1Parser(handler)
    lr0_parser = LR0Parser(handler)
    ll1_parser._successor=lr0_parser
    lr1_parser = LR1Parser(handler)
    lr0_parser._successor=lr1_parser
    recursive_parser = RecursiveDescentParser(handler)
    lr1_parser._successor=recursive_parser



    input_string = 'int a = 7 ;'  # Ejemplo de cadena de entrada

    ll1_parser.handle(input_string)
    ll1_parser._successor.handle(input_string)

parserUnificado()    


