from Token import *
import re
def tokenize(input_string):
    tokens = []
    token_specification = [
        ('Datatype', r'\bint\b'),           # Datatype keyword
        ('Identifier', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),  # Identifiers
        ('NormalAssignment', r'\='),        # Assignment operator
        ('IncrementAssignment', r'\+='),
        ('DecrementAssignment', r'\-='),
        ('Integer', r'\b\d+\b'),            # Integer literals
        ('SemiColon', r'\;'),               # Semicolon
        ('Whitespace', r'\s+'),             # Skip over spaces and tabs
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    get_token = re.compile(tok_regex).match
    position = 0
    while position < len(input_string):
        match = get_token(input_string, position)
        if match:
            type = match.lastgroup
            value = match.group()
            if type != 'Whitespace':
                if type == 'Identifier' and value == 'int':
                    type = 'Datatype'  # Correcting classification for 'int'
                tokens.append(Token(type, value))
            position = match.end()
        else:
            raise RuntimeError('Unexpected character: {}'.format(input_string[position]))
    return tokens
