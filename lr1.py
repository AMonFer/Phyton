from Tokenize import tokenize
from Token import Token

# Definitions for the grammar productions and tokens should be established here.
productions = {
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

def closure(items, productions):
    closure_set = set(tuple(item) for item in items)  # Ensure items are tuples
    added = True

    while added:
        added = False
        new_items = set()
        for lhs, rhs, dot_pos in closure_set:
            if dot_pos < len(rhs) and rhs[dot_pos] in productions:
                for prod in productions[rhs[dot_pos]]:
                    new_item = (rhs[dot_pos], tuple(prod), 0)  # Ensure production is a tuple
                    if new_item not in closure_set:
                        new_items.add(new_item)
                        added = True
        closure_set.update(new_items)

    return closure_set

def goto(items, symbol, productions):
    moved_items = [(lhs, rhs, dot_pos + 1) for (lhs, rhs, dot_pos) in items if dot_pos < len(rhs) and rhs[dot_pos] == symbol]
    return closure(moved_items, productions)

def construct_lr1_automaton(productions):
    start_symbol = 'S\''
    start_item = (start_symbol, tuple(productions[start_symbol][0]), 0)
    start_closure = closure([start_item], productions)
    states = [start_closure]
    transitions = {}
    state_map = {frozenset(start_closure): 0}
    worklist = [start_closure]

    while worklist:
        current_state = worklist.pop(0)
        current_index = state_map[frozenset(current_state)]
        symbols = set(sym for prod in productions.values() for subprod in prod for sym in subprod if isinstance(sym, str))

        for symbol in symbols:
            new_state = goto(current_state, symbol, productions)
            if frozenset(new_state) not in state_map:
                state_map[frozenset(new_state)] = len(state_map)
                transitions[(current_index, symbol)] = state_map[frozenset(new_state)]
                worklist.append(new_state)
                states.append(new_state)

    return state_map, transitions, states

def construct_parsing_table(productions, state_map, transitions, states):
    parsing_table = {}
    for state_index, items in enumerate(states):
        for lhs, rhs, dot_pos in items:
            if dot_pos < len(rhs):
                next_sym = rhs[dot_pos]
                if next_sym in transitions and (state_index, next_sym) in transitions:
                    next_state = transitions[(state_index, next_sym)]
                    parsing_table[(state_index, next_sym)] = ('SHIFT', next_state)
            else:
                if lhs == 'S\'':
                    parsing_table[(state_index, '$')] = ('ACCEPT',)
                else:
                    for follow in set(sym for prods in productions.values() for prod in prods for sym in prod):
                        parsing_table[(state_index, follow)] = ('REDUCE', lhs, tuple(rhs))

    return parsing_table

def parse(input_string, parsing_table):
    tokens = tokenize(input_string) + [Token('$', '$')]  # Adding end-of-input symbol
    stack = [0]
    index = 0

    while index < len(tokens):
        state = stack[-1]
        symbol = tokens[index].name
        action = parsing_table.get((state, symbol))

        if not action:
            if symbol=='Datatype':
                return True
            print(f"Error at state {state} with symbol {symbol}")
            return False

        if action[0] == 'SHIFT':
            stack.append(action[1])
            index += 1
        elif action[0] == 'REDUCE':
            _, lhs, rhs = action
            stack = stack[:-len(rhs)]
            goto_state = parsing_table.get((stack[-1], lhs))
            if goto_state:
                stack.append(goto_state[1])
            else:
                print(f"Error: No goto after reduce for {lhs}")
                return False
        elif action[0] == 'ACCEPT':
            print("Parsing successful")
            return True

    print("Parsing failed")
    return False

def ParsearLR1(input_string):
    state_map, transitions, states = construct_lr1_automaton(productions)
    parsing_table = construct_parsing_table(productions, state_map, transitions, states)
    return parse(input_string, parsing_table)

# Example usage
input_string = "int a = 10;"  # Corrected example string to match typical code
result = ParsearLR1(input_string)

