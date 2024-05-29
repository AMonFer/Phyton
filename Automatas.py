from Token import Token
from LanguageSymbols import *


def automata_symbols(texto: string):
    if len(texto) == 0:
        return None, texto

    if texto[0] in symbols:
        return Token("Symbol", texto[0]), texto[1::]
    else:
        return None, texto


def automata_operators_comparisons_assignments(texto: string, token_type: string):
    list_options = []

    if token_type == "Binary Operator":
        list_options = binary_operators
    elif token_type == "Unary Operator":
        list_options = unary_operators
    elif token_type == "Comparison":
        list_options = comparadores
    elif token_type == "Assignment":
        list_options = assignments

    if len(texto) == 0:
        return None, texto

    token, value = None, ""

    for operator in list_options:
        operator_length = len(operator)
        if texto[:operator_length] == operator:
            value = texto[:operator_length]
            token = Token(token_type, value)
            break

    return token, texto[len(value)::]


def automata_palabras_res(i: int, texto: string):
    if len(texto) == 0:
        return None, texto

    token_type = "Datatype" if i in range(1, 6) else "Keyword"

    palabra = palabrasReservadas[i]
    tam = len(palabra)

    for letra in texto:
        if len(palabra) == 0:
            break
        if letra == palabra[0]:
            palabra = palabra[1::]
        else:
            break
    if len(palabra) == 0:
        return Token(token_type, palabrasReservadas[i]), texto[tam::]

    return None, texto


def automata_ing(texto: string):
    if len(texto) == 0:
        return None, texto

    for i in range(len(texto)):
        letra = texto[i]
        if letra == "'":
            if i + 2 <= len(texto):
                if texto[i + 2] == "'":
                    return Token("Ingenium", texto[:i + 3]), texto[i + 3::]
        break
    return None, texto


def automata_ch(texto: string):
    if len(texto) == 0:
        return None, texto

    aux = ""
    leyendo = False
    for i in range(len(texto)):
        letra = texto[i]
        if letra == "\"":
            aux += letra
            if not leyendo:
                leyendo = True
            else:
                break
        elif leyendo:
            aux += letra
        else:
            break
    if len(aux) > 0:
        return Token("Chorda", aux), texto[len(aux)::]
    return None, texto


def automata_num(numero):
    if len(numero) == 0:
        return None, numero

    dot_found = False
    reading_numbers = False
    digits = ""
    for i in numero:
        if i not in numbers:
            if i == ".":
                if not dot_found:
                    dot_found = True
                    if len(digits) == 0:
                        digits = "0"
                        reading_numbers = True
                    digits += i
                    continue
                else:
                    raise NotImplementedError()  # raise exception when two dots(.) are found, i.e. 2.453.1
            break
        else:
            digits += i
            reading_numbers = True
    if reading_numbers:
        if dot_found:
            if digits[-1] == ".":
                return Token("Geminus", digits + '0'), numero[len(digits)::]
            return Token("Geminus", digits), numero[len(digits)::]

        return Token("Integer", digits), numero[len(digits)::]
    else:
        return None, numero


def automata_identifier(texto):
    if len(texto) == 0:
        return None, texto

    identifier = ""
    for char in texto:
        if char in identificadores:
            identifier += char
        else:
            break

    if len(identifier) > 0:
        return Token("Identifier", identifier), texto[len(identifier)::]

    return None, texto


def get_tokens(text: string):
    # Lista de todos los tokens
    tokens = []
    num_keywords = len(palabrasReservadas)
    while len(text) > 0:
        found = False
        for i in range(1, num_keywords+1):
            token, texto = automata_palabras_res(i, text)

            if token is not None:
                tokens.append(token)
                text = texto
                found = True
                break

        if found:
            continue

        token, texto = automata_operators_comparisons_assignments(text, "Unary Operator")

        if token is not None:
            tokens.append(token)
            text = texto
            continue

        token, texto = automata_operators_comparisons_assignments(text, "Comparison")

        if token is not None:
            tokens.append(token)
            text = texto
            continue

        token, texto = automata_operators_comparisons_assignments(text, "Assignment")

        if token is not None:
            tokens.append(token)
            text = texto
            continue

        token, texto = automata_operators_comparisons_assignments(text, " Binary Operator")

        if token is not None:
            tokens.append(token)
            text = texto
            continue

        token, texto = automata_symbols(text)

        if token is not None:
            tokens.append(token)
            text = texto
            continue

        token, texto = automata_ing(text)

        if token is not None:
            tokens.append(token)
            text = texto
            continue

        token, texto = automata_ch(text)

        if token is not None:
            tokens.append(token)
            text = texto
            continue

        token, texto = automata_num(text)

        if token is not None:
            tokens.append(token)
            text = texto
            continue

        token, texto = automata_identifier(text)

        if token is not None:
            tokens.append(token)
            text = texto
            continue
    return tokens
