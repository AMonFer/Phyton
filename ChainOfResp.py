from abc import ABC, abstractmethod
from analisisLR0 import ParsearLR0
from analisisLR1 import ParsearLR1

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
        if request == 'LL1':
            print("Handled by LL1 parser: Parsing using LL1 techniques.")
        elif self._successor:
            print("LL1 parser passes to the next handler.")
            self._successor.handle(request)

class LR0Parser(Handler):
    """Handle for LR0 grammars"""
    def handle(self, request):
        if ParsearLR0(request)=="Cadena aceptada.":
            print("Handled by LR0 parser: Parsing using LR0 techniques.")
        elif self._successor:
            print("LR0 parser passes to the next handler.")
            self._successor.handle(request)

class LR1Parser(Handler):
    """Handle for LR1 grammars"""
    def handle(self, request):
        if ParsearLR1(request)=="Cadena aceptada.":
            print("Handled by LR1 parser: Parsing using LR1 techniques.")
        elif self._successor:
            print("LR1 parser passes to the next handler.")
            self._successor.handle(request)

class RecursiveDescentParser(Handler):
    """Handle for recursive descent grammars"""
    def handle(self, request):
        if request == 'Recursive':
            print("Handled by Recursive Descent parser: Parsing using recursive descent techniques.")
        else:
            print("Request not handled: No suitable parser found.")



