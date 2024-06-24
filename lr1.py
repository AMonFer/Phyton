from collections import defaultdict

def closure(items, productions):
    closure_set = set(items)
    added = True

    while added:
        added = False
        new_items = set(closure_set)
        for (lhs, rhs, dot_pos, lookahead) in closure_set:
            if dot_pos < len(rhs):
                next_symbol = rhs[dot_pos]
                if next_symbol in productions:
                    for prod in productions[next_symbol]:
                        new_lookaheads = first(rhs[dot_pos+1:] + (lookahead,), productions)
                        for new_lookahead in new_lookaheads:
                            new_item = (next_symbol, tuple(prod), 0, new_lookahead)
                            if new_item not in closure_set:
                                new_items.add(new_item)
                                added = True
        closure_set = new_items

    return closure_set

def first(symbols, productions):
    first_set = set()
    if len(symbols) == 0:
        return first_set
    if symbols[0] not in productions:
        return {symbols[0]}
    for prod in productions[symbols[0]]:
        if prod[0] == '':
            first_set |= first(symbols[1:], productions)
        else:
            first_set |= first(prod, productions)
    return first_set

def goto(items, symbol, productions):
    next_items = set()
    for (lhs, rhs, dot_pos, lookahead) in items:
        if dot_pos < len(rhs) and rhs[dot_pos] == symbol:
            next_items.add((lhs, rhs, dot_pos + 1, lookahead))
    return closure(next_items, productions)

def construct_lr1_automaton(productions):
    start_symbol = list(productions.keys())[0]
    start_item = (start_symbol, tuple(productions[start_symbol][0]), 0, '$')
    start_closure = closure([start_item], productions)
    states = [start_closure]
    symbols = set(sym for prods in productions.values() for prod in prods for sym in prod) | set(productions.keys())
    transitions = {}
    state_map = {frozenset(start_closure): 0}

    while True:
        added = False
        new_states = list(states)
        for state in states:
            for symbol in symbols:
                new_state = goto(state, symbol, productions)
                if new_state and frozenset(new_state) not in state_map:
                    new_states.append(new_state)
                    state_map[frozenset(new_state)] = len(state_map)
                    added = True
                if new_state:
                    transitions[(state_map[frozenset(state)], symbol)] = state_map[frozenset(new_state)]
        if not added:
            break
        states = new_states

    return state_map, transitions, states

def construct_parsing_table(productions, state_map, transitions, states):
    parsing_table = {}
    accepting_state = None

    for state_index, state in enumerate(states):
        symbols = set(sym for prods in productions.values() for prod in prods for sym in prod) | set(productions.keys())
        for (lhs, rhs, dot_pos, lookahead) in state:
            if dot_pos == len(rhs):
                if lhs == 'S\'':
                    parsing_table[(state_index, '$')] = ('ACCEPT',)
                    accepting_state = state_index
                else:
                    if (state_index, lookahead) not in parsing_table:
                        parsing_table[(state_index, lookahead)] = ('REDUCE', lhs, rhs)
            else:
                next_symbol = rhs[dot_pos]
                if (state_index, next_symbol) in transitions:
                    next_state = transitions[(state_index, next_symbol)]
                    if next_symbol in productions:
                        parsing_table[(state_index, next_symbol)] = ('GOTO', next_state)
                    else:
                        parsing_table[(state_index, next_symbol)] = ('SHIFT', next_state)

    return parsing_table, accepting_state

def parse(input_string, parsing_table, accepting_state):
    stack = [0]
    tokens = input_string.replace(';', ' ;').split() + ['$']  # Tokenize the string properly
    index = 0

    while True:
        state = stack[-1]
        symbol = tokens[index]
        action = parsing_table.get((state, symbol))

        if not action:
            if symbol == '$':
                print(f"Current state: {state}, current symbol: {symbol}, action: ACCEPT")
                return True
            print(f"Current state: {state}, current symbol: {symbol}, action: {action}")
            return False

        print(f"Stack: {stack}, Input: {tokens[index:]}, Action: {action}")

        if action[0] == 'SHIFT':
            stack.append(action[1])
            index += 1
        elif action[0] == 'REDUCE':
            lhs, rhs = action[1], action[2]
            for _ in range(len(rhs)):
                stack.pop()
            goto_state = parsing_table[(stack[-1], lhs)][1]
            stack.append(goto_state)
        elif action[0] == 'ACCEPT':
            return True
