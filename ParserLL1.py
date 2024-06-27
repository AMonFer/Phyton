from Stack import Stack

#from ChainOfResp import tokenize

def ll1_parser(tokens):
    
    ll1_table = {
    'Declaration': {'Datatype': ['Datatype', 'Assignment']},
    'Assignment': {'Identifier': ['Identifier', 'Assignment1', 'Expression', 'SemiColon']},
    'Assignment1': {
        'NormalAssignment': ['NormalAssignment'],
        'IncrementAssignment': ['IncrementAssignment'],
        'DecrementAssignment': ['DecrementAssignment']
    },
    'Expression': {
        'Integer': ['Value'],
        'AdditionOperator': ['Value', 'UnaryOperator'],  
        'BinaryOperator': ['Value', 'Expression1']
    },
    'Expression1': {
        'BinaryOperator': ['BinaryOperator', 'Value', 'Expression1'],
    },
    'UnaryOperator': {
        'IncrementOperator': ['IncrementOperator'],
        'DecrementOperator': ['DecrementOperator'],
    },
    'Value': {
        'Integer': ['Integer'],
        'Geminus': ['Geminus'],
        'Ingenium': ['Ingenium'],
        'Chorda': ['Chorda']
    }
}
    stack = ['Declaration']
    token_index = 0

    while stack and token_index < len(tokens):
        top = stack.pop()
        current_token = tokens[token_index]
        print(f"Stack Top: {top}, Current Token: {current_token.name}")

        if top in ll1_table:  # No-terminal
            if current_token.name in ll1_table[top]:
                print(f"Expanding: {top} with {ll1_table[top][current_token.name]}")
                stack.extend(reversed(ll1_table[top][current_token.name]))
            else:
                print(f"No matching rule for {current_token.name} under {top}")
                return False
        else:  # Terminal
            if top == current_token.name:
                print("Matched terminal, moving to next token.")
                token_index += 1
            else:
                print(f"Expected {top}, found {current_token.name}")
                return False

        if token_index >= len(tokens) and stack:
            print("Tokens exhausted but stack not empty.")
            return False

    print("Final stack status:", stack)
    print("Final token index:", token_index)

    
    return not stack and token_index == len(tokens)


'''input_string = "int a = 10;"
tokens = tokenize(input_string)
for token in tokens:
    print(f"Token Type: {token.name}, Token Value: {token.value}")
result = ll1_parser(tokens)
print("Parsing successful:", result)'''
