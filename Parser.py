from LanguageTokens import *

# Productions
productions = {"Declaration": [("Datatype", "Declaration1")],
               "Declaration1": ["Assignment", ("Identifier", SemiColon)],
               "Assignment": [("Identifier", "Assignment1", "Expression", SemiColon)],
               "Assignment1": [NormalAssignment, IncrementAssignment, DecrementAssignment],
               "Expression": [("Value", "UnaryOperator"), ("Value", "Expression1"), "Value"],
               "Expression1": [("BinaryOperator", "Value", "Expression1"), ("BinaryOperator", "Value")],
               "UnaryOperator": [IncrementOperator, DecrementOperator],
               "BinaryOperator": [AdditionOperator, SubtractionOperator,
                                  MultiplicationOperator, DivisionOperator,
                                  ModuleOperator],
               "Value": ["Integer", "Geminus", "Ingenium", "Chorda"]
               }


def get_tokens_until_token(tokens, ref_token):
    return_tokens = []
    for token in tokens:
        if token != ref_token:
            return_tokens.append(token)
        else:
            break
    return return_tokens


def is_all_tokens(options):
    true_if_tokens = [isinstance(x, Token) for x in options]
    return all(true_if_tokens)


def is_all_strings(options):
    true_if_strings = [isinstance(x, str) for x in options[0]]
    return all(true_if_strings)


def is_production(text):
    return text in productions.keys()


def get_production_options(production):
    return productions[production]


def token_is_second_option(option, token):
    if isinstance(option, str):
        return token == option if not is_production(option) else False
    if isinstance(option, tuple) and len(option) > 1:
        if isinstance(option[1], str):
            return token == option[1] if not is_production(option[0]) else False
        elif isinstance(option[1], Token):
            return token == option[1]
        else:
            raise NotImplementedError()  # Raise when not a valid option
    raise NotImplementedError()  # Raise when not a valid option


def production_is_second_option(option, production):
    if isinstance(option, str):
        return production == option
    if isinstance(option, tuple) and len(option) > 1:
        if isinstance(option[1], Token):
            return production == option[1]
        else:
            raise NotImplementedError()  # Raise when not a valid option
    raise NotImplementedError()  # Raise when not a valid option


def get_option_that_has_token(production, token):
    options = get_production_options(production)
    if is_all_tokens(options):
        if token in options:
            return options


def get_option_that_starts_with_token(production, token):
    options = get_production_options(production)
    print(f"there are {len(options)} options")
    options_start_token = []
    for option in options:
        print(f"current options are: {options}")
        if isinstance(option, str):
            if is_production(option):
                option_to_check = get_option_that_starts_with_token(option, token)
                if option_to_check is not None:
                    options_start_token += option_to_check
            else:
                option_to_check = option if token == option else None
                if option_to_check is not None:
                    options_start_token.append(option_to_check)

        elif isinstance(option, tuple):
            if isinstance(option[0], str):
                if is_production(option[0]):
                    option_to_check = get_option_that_starts_with_token(option[0], token)
                    if option_to_check is not None:
                        options_start_token.append(tuple([option_to_check]) + tuple([opt for opt in option[1::]]))
                else:
                    option_to_check = option if option[0] == token else None
                    if option_to_check is not None:
                        options_start_token.append(option_to_check)
            elif isinstance(option[0], Token):
                option_to_check = option[0] if option[0] == token else None
                if option_to_check is not None:
                    options_start_token.append(option_to_check)
        elif isinstance(option, Token):
            option_to_check = option if option == token else None
            if option_to_check is not None:
                options_start_token.append(option_to_check)
    if len(options_start_token) == 0:
        return None
    print(f"Value being returned is: {options_start_token}")
    return options_start_token


def find_pair_production_option_that_begins_with_token(token):
    production, options = None, None
    for key in productions.keys():
        options = get_option_that_starts_with_token(key, token)
        if options is not None:
            production = key
            break
    return production, options


def find_pair_production_option_that_contains_token(token):
    production, options = None, None
    for key in productions.keys():
        options = get_option_that_has_token(key, token)
        if options is not None:
            production = key
            break
    return production, options


def temporal_parser(tokens):
    for token in tokens:
        pair = find_pair_production_option_that_begins_with_token(token)
        print("pair found is: {} for datatype token".format(pair))


print("pair found is: {} for identifier token".format(
    find_pair_production_option_that_begins_with_token(Token("Identifier", "abc"))))

print("pair found is: {} for datatype token".format(
    find_pair_production_option_that_contains_token(Token("Assignment", "="))))
