from Production import Production
from LanguageTokens import Token
from lr0 import construct_lr0_automaton, construct_parsing_table, parse

productionsLr0 = {
    'S\'': [['S']],  # Augmented start symbol
    'S': [['Declaration']],
    'Declaration': [['Datatype', 'Declaration1']],
    'Declaration1': [['Assignment', 'Declaration1'], ['Identifier', 'SemiColon']],
    'Assignment': [['Identifier', 'Assignment1', 'Expression', 'SemiColon']],
    'Assignment1': [['NormalAssignment'], ['IncrementAssignment'], ['DecrementAssignment']],
    'Expression': [['Value', 'UnaryOperator'], ['Value', 'Expression1'], ['Value']],
    'Expression1': [['BinaryOperator', 'Value', 'Expression1'], ['BinaryOperator', 'Value']],
    'UnaryOperator': [['IncrementOperator'], ['DecrementOperator']],
    'BinaryOperator': [['AdditionOperator'], ['SubtractionOperator'], ['MultiplicationOperator'], ['DivisionOperator'], ['ModuleOperator']],
    'Value': [['Integer'], ['Geminus'], ['Ingenium'], ['Chorda']]
}

def ParsearLR0(input_string):
    
    state_map, transitions, states = construct_lr0_automaton(productionsLr0)
    parsing_table, accepting_state = construct_parsing_table(productionsLr0, state_map, transitions, states)

    result = parse(input_string, parsing_table, accepting_state)  # Adjusted to use token names
    print("Cadena aceptada." if result else "Cadena no aceptada.")

    return "Cadena aceptada." if result else "Cadena no aceptada."

# Example usage
input_string = "int a = 10;"  # Corrected example string to match typical code
ParsearLR0(input_string)
