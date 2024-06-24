
from ChainOfResp import Handler,LL1Parser,LR0Parser,LR1Parser,RecursiveDescentParser

# Set up the chain
handler = Handler()
ll1_parser = LL1Parser(handler)
lr0_parser = LR0Parser(handler)
ll1_parser._successor=lr0_parser
lr1_parser = LR1Parser(handler)
lr0_parser._successor=lr1_parser
recursive_parser = RecursiveDescentParser(handler)
lr1_parser._successor=recursive_parser

# Define the head of the chain
head_parser = recursive_parser

# List of different grammar types
requests = ['LL1', 'LR0', 'LR1', 'Recursive', 'Unknown']

input_string = 'Datatype Identifier = Integer ;.'  # Ejemplo de cadena de entrada
lr0_parser.handle(input_string)
lr1_parser.handle(input_string)
# Process each request
#for req in requests:
#    print(f"\nProcessing request: {req}")
#    ll1_parser.handle(req)


