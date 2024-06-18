from Token import Token

# Symbols
SemiColon = Token("Symbol", ';')
Coma = Token("Symbol",  ',')

OpenParenthesis = Token("Symbol", '(')
CloseParenthesis = Token("Symbol", ')')

OpenCurlyBracket = Token("Symbol", '{')
CloseCurlyBracket = Token("Symbol", '}')

OpenSquareBracket = Token("Symbol", '[')
CloseSquareBracket = Token("Symbol", ']')

# Assignments
NormalAssignment = Token("Assignment", '=')
IncrementAssignment = Token("Assignment", '+=')
DecrementAssignment = Token("Assignment", '-=')


# Operators

# Binary Operators
AdditionOperator = Token("Binary Operator", '+')
SubtractionOperator = Token("Binary Operator", '-')

MultiplicationOperator = Token("Binary Operator", '*')

DivisionOperator = Token("Binary Operator", '/')
ModuleOperator = Token("Binary Operator", "mod")

# Unary Operator
IncrementOperator = Token("Unary Operator", "++")
DecrementOperator = Token("Unary Operator", "--")

# Comparisons
GreaterThan = Token("Comparison", '>')
LessThan = Token("Comparison", '<')

EqualTo = Token("Comparison", "==")
NotEqualTo = Token("Comparison", "!=")

GreaterThanOrEqualTo = Token("Comparison", ">=")
LessThanOrEqualTo = Token("Comparison", "<=")
