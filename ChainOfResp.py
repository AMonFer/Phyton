from abc import ABC, abstractmethod
from lr0 import ParsearLR0
from lr1 import ParsearLR1
from Parser import *
from ParserLL1 import *
from Tokenize import tokenize
import re

class Handler:
    """Abstract handler"""
    def __init__(self, successor=None):
        self._successor = successor  # Next handler in the chain
    @abstractmethod
    def handle(self, request):
        """handle the request must be implemented by concrete classes"""
        pass
        

class LL1Parser(Handler):
    """Handle for LL1 grammars"""
    def handle(self, request):
        parser=ll1_parser(tokenize(request))
        self._successor=LR0Parser(Handler)
        if parser == True:
            print("Handled by LL1 parser: Parsing using LL1 techniques -> cadena aceptada.")
        elif self._successor:
            print("LL1 parser passes to the next handler.")
            self._successor.handle(request)

class LR0Parser(Handler):
    """Handle for LR0 grammars"""
    def handle(self, request):
        self._successor=LR1Parser(Handler)
        if ParsearLR0(request)=="Cadena aceptada.":
            print("Handled by LR0 parser: Parsing using LR0 techniques -> cadena aceptada.")
        elif self._successor:
            print("LR0 parser passes to the next handler.")
            self._successor.handle(request)

class LR1Parser(Handler):
    """Handle for LR1 grammars"""
    def handle(self, request):
        self._successor=RecursiveDescentParser(Handler)
        if ParsearLR1(request)=="Cadena aceptada.":
            print("Handled by LR1 parser: Parsing using LR1 techniques -> cadena aceptada.")
        elif self._successor:
            print("LR1 parser passes to the next handler.")
            self._successor.handle(request)

class RecursiveDescentParser(Handler):
    """Handle for recursive descent grammars"""
    def handle(self, request):
        parser=Parser(tokenize(request))
        if parser.parse():
            print("Handled by Recursive Descent parser: Parsing using recursive descent techniques -> Cadena aceptada.")
        else:
            print("Request not handled: No suitable parser found.")




