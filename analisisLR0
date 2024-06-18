from Production import Production
from LanguageTokens import (
    Token, SemiColon, AdditionOperator, SubtractionOperator, 
    MultiplicationOperator, DivisionOperator, ModuleOperator, 
    IncrementOperator, DecrementOperator, NormalAssignment, 
    IncrementAssignment, DecrementAssignment
)
from lr0 import construct_lr0_automaton, construct_parsing_table, parse

productions = {
    'S\'': [['S']],  # Augmented start symbol
    'S': [['Declaration']],
    'Declaration': [['Datatype', 'Declaration1']],
    'Declaration1': [['Assignment', 'Declaration1'], ['Identifier', ';']],
    'Assignment': [['Identifier', 'Assignment1', 'Expression', ';']],
    'Assignment1': [['='], ['+='], ['-=']],
    'Expression': [['Value', 'UnaryOperator'], ['Value', 'Expression1'], ['Value']],
    'Expression1': [['BinaryOperator', 'Value', 'Expression1'], ['BinaryOperator', 'Value']],
    'UnaryOperator': [['++'], ['--']],
    'BinaryOperator': [['+'], ['-'], ['*'], ['/'], ['mod']],
    'Value': [['Integer'], ['Geminus'], ['Ingenium'], ['Chorda']]
}

# Construcción del autómata LR(0)
state_map, transitions, states = construct_lr0_automaton(productions)

# Construcción de la tabla de análisis sintáctico
parsing_table, accepting_state = construct_parsing_table(productions, state_map, transitions, states)

#Ejemplo
input_string = 'Datatype Identifier = Integer;' 
result = parse(input_string, parsing_table, accepting_state)
print("Cadena aceptada." if result else "Cadena no aceptada.")