from Token import *
import re


def tokenize(input_string):
    tokens = []
    token_specification = [
        ('Datatoken_type', r'\bint\b'),           # Datatoken_type keyword
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
            token_type = match.lastgroup
            value = match.group()
            if token_type != 'Whitespace':
                if token_type == 'Identifier' and value == 'int':
                    token_type = 'Datatoken_type'  # Correcting classification for 'int'
                tokens.append(Token(token_type, value))
            position = match.end()
        else:
            raise RuntimeError('Unexpected character: {}'.format(input_string[position]))
    return tokens
