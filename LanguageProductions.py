from Production import Production
from LanguageTokens import (IncrementOperator, DecrementOperator,
                            AdditionOperator, SubtractionOperator,
                            MultiplicationOperator, DivisionOperator,
                            ModuleOperator,
                            NormalAssignment, IncrementAssignment, DecrementAssignment,
                            SemiColon)

value = Production('Value')
value.add_terminal("Integer", 1)
value.add_terminal("Geminus", 2)
value.add_terminal("Ingenium", 3)
value.add_terminal("Chorda", 4)

binary_operator = Production('BinaryOperator')
binary_operator.add_terminal(AdditionOperator, 1)
binary_operator.add_terminal(SubtractionOperator, 2)
binary_operator.add_terminal(MultiplicationOperator, 3)
binary_operator.add_terminal(DivisionOperator, 4)
binary_operator.add_terminal(ModuleOperator, 5)

unary_operator = Production('UnaryOperator')
unary_operator.add_terminal(IncrementOperator, 1)
unary_operator.add_terminal(DecrementOperator, 2)

expression1_1 = Production("Expression1")
expression1_1.add_non_terminal(binary_operator, 1)
expression1_1.add_non_terminal(value, 2)

expression1_2 = Production("Expression1")
expression1_2.add_non_terminal(binary_operator, 1)
expression1_2.add_non_terminal(value, 2)

expression1 = Production("Expression1")
expression1.add_non_terminal(expression1_1, 1, expression1_2)

expression1_1.add_non_terminal(expression1, 3)

expression_1 = Production("Expression")
expression_1.add_non_terminal(value, 1)
expression_1.add_non_terminal(unary_operator, 2)

expression_2 = Production("Expression")
expression_2.add_non_terminal(value, 1)
expression_2.add_non_terminal(expression1, 2)

expression_3 = Production("Expression")
expression_3.add_non_terminal(value, 1)

expression = Production("Expression")
expression.add_non_terminal(expression_1, 1, expression_2, expression_3)

assignment1 = Production("Assignment1")
assignment1.add_terminal(NormalAssignment, 1)
assignment1.add_terminal(IncrementAssignment, 2)
assignment1.add_terminal(DecrementAssignment, 3)

assignment = Production("Assignment")
assignment.add_terminal("Identifier", 1)
assignment.add_non_terminal(assignment1, 2)
assignment.add_non_terminal(expression, 3)
assignment.add_terminal(SemiColon, 4)

declaration1_2 = Production("Declaration1")
declaration1_2.add_terminal("Identifier", 1)
declaration1_2.add_terminal(SemiColon, 2)

declaration1 = Production("Declaration1")
declaration1.add_non_terminal(assignment, 1, declaration1_2)

declaration = Production('Declaration')
declaration.add_terminal("Datatype", 1)
declaration.add_non_terminal(declaration1, 2)


productions = [value, binary_operator, unary_operator,
               expression1, expression,
               assignment1, assignment,
               declaration1, declaration]

# productions = {"Declaration": [("Datatype", "Declaration1")],
#                "Declaration1": ["Assignment", ("Identifier", SemiColon)],
#                "Assignment": [("Identifier", "Assignment1", "Expression", SemiColon)],
#                "Assignment1": [NormalAssignment, IncrementAssignment, DecrementAssignment],
#                "Expression": [("Value", "UnaryOperator"), ("Value", "Expression1"), "Value"],
#                "Expression1": [("BinaryOperator", "Value", "Expression1"), ("BinaryOperator", "Value")],
#                "UnaryOperator": [IncrementOperator, DecrementOperator],
#                "BinaryOperator": [AdditionOperator, SubtractionOperator,
#                                   MultiplicationOperator, DivisionOperator,
#                                   ModuleOperator],
#                "Value": ["Integer", "Geminus", "Ingenium", "Chorda"]
#                }
