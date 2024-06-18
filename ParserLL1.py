from Stack import Stack
from ParsingTable import ParsingTable
from LanguageProductions import productions
from LanguageTokens import Token
from Production import Production
from ParsingTable import get_first


class Parser:
    def __init__(self, parsing_table):
        self.parsing_table = parsing_table
        self.stack = Stack()

    def find_production_for_token(self, token):
        for production in productions:
            first_set = get_first(production)
            for item in first_set:
                if isinstance(item, str):
                    if token == item:
                        return production
                elif isinstance(item, Token) and item.name == token:
                    return production
        return None

    def parse(self, tokens):
        first_token = tokens[0]
        initial_production = self.find_production_for_token(first_token)
        if initial_production is None:
            print(f"Error: No production found for token {first_token}")
            return False

        self.stack.push(initial_production)
        index = 0

        while not self.stack.is_empty() and index < len(tokens):
            top = self.stack.peek()
            current_token = tokens[index]

            print(f"Top of stack: {top}, Current token: {current_token}")

            if isinstance(top, Token):
                if top.name == current_token.name:
                    print(f"Matched token: {current_token}")
                    self.stack.pop()
                    index += 1
                else:
                    return False
            elif isinstance(top, Production):
                if current_token.name in self.parsing_table.table.get(top.name, {}):
                    production = self.parsing_table.table[top.name][current_token.name]
                    print(f"Reducing using production: {production.name}")
                    self.stack.pop()

                    elements_to_push = []
                    if production.terminals:
                        elements_to_push.extend(production.terminals)
                    if production.non_terminals:
                        elements_to_push.extend(production.non_terminals)

                    for place, element, alternative in reversed(elements_to_push):
                        if isinstance(element, str):
                            self.stack.push(Token(element, element))
                        elif element:
                            self.stack.push(element)
                        print(f"Pushed {element} to stack")
                else:
                    print(f"Error: No production found for {current_token.name} in {top.name}")
                    return False
            elif isinstance(top, str):
                if top == current_token.name:
                    print(f"Matched terminal: {current_token}")
                    self.stack.pop()
                    index += 1
                else:
                    print(f"Error: Expected {top}, found {current_token.name}")
                    return False
            else:
                print(f"Error: Unexpected item at top of stack: {top}")
                return False

        if index < len(tokens):
            print("Error: Unprocessed tokens remaining")
            return False

        if not self.stack.is_empty():
            print("Error: Stack is not empty after parsing all tokens")
            return False

        return True


parsing_table = ParsingTable(productions)

tokens = [
    Token("Datatype", "int"),
    Token("Identifier", "x"),
    Token("Assignment", "="),
    Token("Integer", "10"),
    Token("Symbol", ";")
]

parser = Parser(parsing_table)
result = parser.parse(tokens)
