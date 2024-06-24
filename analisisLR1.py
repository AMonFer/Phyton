from Production import Production
from LanguageTokens import (
    SemiColon, AdditionOperator, SubtractionOperator, 
    MultiplicationOperator, DivisionOperator, ModuleOperator, 
    IncrementOperator, DecrementOperator, NormalAssignment, 
    IncrementAssignment, DecrementAssignment
)
from lr1 import construct_lr1_automaton, construct_parsing_table, parse

# Conversión de producciones a formato esperado por el autómata LR(1)
productions = {
    'S\'': [('S',)],  # Augmented start symbol
    'S': [('Declaration',)],
    'Declaration': [('Datatype', 'Declaration1')],
    'Declaration1': [('Assignment', 'Declaration1'), ('Identifier', ';')],
    'Assignment': [('Identifier', 'Assignment1', 'Expression', ';')],
    'Assignment1': [('=',), ('+=',), ('-=',)],
    'Expression': [('Value', 'UnaryOperator'), ('Value', 'Expression1'), ('Value',)],
    'Expression1': [('BinaryOperator', 'Value', 'Expression1'), ('BinaryOperator', 'Value')],
    'UnaryOperator': [('++',), ('--',)],
    'BinaryOperator': [('+',), ('-',), ('*',), ('/',), ('mod',)],
    'Value': [('Integer',), ('Geminus',), ('Ingenium',), ('Chorda',)]
}

# Construcción del autómata LR(1)
state_map, transitions, states = construct_lr1_automaton(productions)

# Construcción de la tabla de análisis sintáctico
parsing_table, accepting_state = construct_parsing_table(productions, state_map, transitions, states)

# Ejemplo de uso
input_string = 'Datatype Identifier = Integer ;'  # Ejemplo de cadena de entrada
result = parse(input_string, parsing_table, accepting_state)
print("Cadena aceptada." if result else "Cadena no aceptada.")