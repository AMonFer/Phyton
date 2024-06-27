# Assuming necessary imports from LanguageTokens and LanguageProductions
from Token import Token
from LanguageProductions import productions
from LanguageTokens import (IncrementOperator, DecrementOperator,
                            AdditionOperator, SubtractionOperator,
                            MultiplicationOperator, DivisionOperator,
                            ModuleOperator,
                            NormalAssignment, IncrementAssignment, DecrementAssignment,
                            SemiColon)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_index = 0

    def lookahead(self):
        if self.current_index < len(self.tokens):
            return self.tokens[self.current_index]
        return None

    def consume(self, expected_name):
        current = self.lookahead()
        if current and current.name == expected_name:
            print(f"Consuming: {current.name}")
            self.current_index += 1
            return True
        raise ValueError(f"Expected token '{expected_name}' but found '{current.name if current else 'None'}'")

    def parse_declaration(self):
        # Declaration -> Datatype Declaration1
        self.consume("Datatype")
        self.parse_declaration1()

    def parse_declaration1(self):
        # Declaration1 -> (Identifier, Assignment) or (Identifier, SemiColon)
        self.consume("Identifier")
        if self.lookahead() and self.lookahead().name == "SemiColon":
            self.consume("SemiColon")
        else:
            self.parse_assignment()

    def parse_assignment(self):
        # Assignment -> (Assignment1, Expression, SemiColon)
        self.parse_assignment1()
        self.parse_expression()
        self.consume("SemiColon")

    def parse_assignment1(self):
        # Assignment1 -> NormalAssignment | IncrementAssignment | DecrementAssignment
        token = self.lookahead()
        if token and token.name in ["NormalAssignment", "IncrementAssignment", "DecrementAssignment"]:
            self.consume(token.name)
        else:
            raise ValueError(f"Expected an assignment operator but found {token.name if token else 'None'}")

    def parse_expression(self):
        # Expression -> (Value, UnaryOperator) | (Value, Expression1) | Value
        self.parse_value()
        if self.lookahead() and self.lookahead().name in ["IncrementOperator", "DecrementOperator"]:
            self.parse_unary_operator()
        elif self.lookahead() and self.lookahead().name == "BinaryOperator":
            self.parse_expression1()

    def parse_expression1(self):
        # Expression1 -> (BinaryOperator, Value, Expression1) | (BinaryOperator, Value)
        self.consume("BinaryOperator")
        self.parse_value()
        if self.lookahead() and self.lookahead().name == "BinaryOperator":
            self.parse_expression1()

    def parse_unary_operator(self):
        # UnaryOperator -> IncrementOperator | DecrementOperator
        self.consume(self.lookahead().name)

    def parse_value(self):
        # Value -> Integer | Geminus | Ingenium | Chorda
        if self.lookahead() and self.lookahead().name in ["Integer", "Geminus", "Ingenium", "Chorda"]:
            self.consume(self.lookahead().name)
        else:
            raise ValueError("Expected a value")

    def parse(self):
        # Start parsing from the root production rule
        self.parse_declaration()
        if self.current_index != len(self.tokens):
            raise Exception("Parser error: extra input after last token.")
        else:
            return True

# Example usage of the parser

#tokens = [Token("Datatype", "int"), Token("Identifier", "a"), Token("NormalAssignment", "="), Token("Integer", "7"), Token("SemiColon", ";")]
#parser = Parser(tokens)
#parser.parse()
#print("Parsing completed successfully.")
