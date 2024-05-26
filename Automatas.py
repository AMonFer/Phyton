import string
from Tokens import Token

# todos los caracteres reconocidos
identificadores = string.ascii_lowercase + string.ascii_uppercase

# diccionario de palabras reservadas:
# Values from 1 to 4 are be Datatypes

# 1-int, 2-double, 3-char, 4-void, 5-return, 6-funcion, 7-for, 8-while, 9-break, 10-and, 11-or, 12-if : ac si, 13-elif : alium si, 14-else,
# 15-verdad, 16-falso, 17-chorda: string
palabrasReservadas = {1: "int", 2: "gem", 3: "ing", 4: "inan", 5: "red", 6: "clib", 7: "quia", 8: "dum", 9: "finis",
                      10: "et", 11: "vel", 12: "acsi", 13: "aliumsi", 14: "alium", 15: "verus", 16: "falsus",
                      17: "ch"}

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

simbolos = [';', ',', '(', ')', '{', '}']

operadores = ["*", "-", "/", "+", "mod", "=", "++", "--"]

comparadores = [">", "<", "==", "<=", ">=", "!="]


def automata_simbolos(texto: string):
    if len(texto) == 0:
        return None, texto

    if texto[0] in simbolos:
        return Token("Symbol", texto[0]), texto[1::]
    else:
        return None, texto


def automata_operadores_comparadores(texto: string, token_type: string):
    lista_opciones = []

    if token_type == "Operator":
        lista_opciones = operadores
    elif token_type == "Comparison":
        lista_opciones = comparadores

    if len(texto) == 0:
        return None, texto

    token, value = None, ""

    for operator in lista_opciones:
        operator_length = len(operator)
        if texto[:operator_length] == operator:
            value = texto[:operator_length]
            token = Token(token_type, value)
            break

    return token, texto[len(value)::]


def automata_palabras_res(i: int, texto: string):
    if len(texto) == 0:
        return None, texto

    token_type = "Datatype" if i in range(1, 5) else "Keyword"

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
        # return Token("Datatype", palabrasReservadas[i]), texto[tam::]
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
        if i not in numeros:
            if i == ".":
                if not dot_found:
                    dot_found = True
                    if len(digits) == 0:
                        digits = "0"
                        reading_numbers = True
                    digits += i
                    continue
                else:
                    raise NotImplementedError() # raise exception when two dots(.) are found, i.e. 2.453.1
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
    num_keywrds = len(palabrasReservadas)
    while len(text) > 0:
        found = False
        for i in range(1, num_keywrds+1):
            token, texto = automata_palabras_res(i, text)

            if token is not None:
                tokens.append(token)
                text = texto
                found = True
                break

        if found:
            continue

        # print(f"current text: {text}")

        token, texto = automata_operadores_comparadores(text, "Comparison")

        if token is not None:
            tokens.append(token)
            text = texto
            continue

        token, texto = automata_operadores_comparadores(text, "Operator")

        if token is not None:
            tokens.append(token)
            text = texto
            continue

        token, texto = automata_simbolos(text)

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
