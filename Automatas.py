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

operadores = ['*', '-', '/', '+', '%', '=']


def AutomataSimbolos(texto: string):
    if len(texto) == 0:
        return None, texto

    if texto[0] in simbolos:
        return Token("Symbol", texto[0]), texto[1::]
    else:
        return None, texto


def AutomataOperadores(texto: string):
    if len(texto) == 0:
        return None, texto

    if len(texto) > 1:
        if texto[:2] == "==":
            return Token("Operator", texto[:2]), texto[2::]

    if texto[0] in operadores:
        return Token("Operator", texto[0]), texto[1::]
    else:
        return None, texto


def AutomataPalabrasRes(i: int, texto: string):
    if len(texto) == 0:
        return None, texto

    type = "Datatype" if i in range(1, 5) else "Keyword"

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
        #return Token("Datatype", palabrasReservadas[i]), texto[tam::]
        return Token(type, palabrasReservadas[i]), texto[tam::]

    return None, texto


def AutomataIng(texto: string):
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


def AutomataCH(texto: string):
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


def AutomataNum(numero):
    if len(numero) == 0:
        return None, numero

    aux = True
    digits = ""
    for i in numero:
        if i not in numeros:
            break
        else:
            digits += i
            aux = False
    if not aux:
        return Token("Ordo", digits), numero[len(digits)::]
    else:
        return None, numero


def AutomataIdentifier(texto):
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


def GetTokens(text: string):
    # Lista de todos los tokens
    tokens = []
    num_keywrds = len(palabrasReservadas)
    while len(text) > 0:
        found = False
        for i in range(1, num_keywrds+1):
            token, texto = AutomataPalabrasRes(i, text)

            if token is not None:
                tokens.append(token)
                text = texto
                found = True
                break

        if found:
            found = False
            continue

        #print(f"current text: {text}")

        token, texto = AutomataOperadores(text)

        if token is not None:
            tokens.append(token)
            text = texto
            continue

        token, texto = AutomataSimbolos(text)

        if token is not None:
            tokens.append(token)
            text = texto
            continue

        token, texto = AutomataIng(text)

        if token is not None:
            tokens.append(token)
            text = texto
            continue

        token, texto = AutomataCH(text)

        if token is not None:
            tokens.append(token)
            text = texto
            continue

        token, texto = AutomataNum(text)

        if token is not None:
            tokens.append(token)
            text = texto
            continue

        token, texto = AutomataIdentifier(text)

        if token is not None:
            tokens.append(token)
            text = texto
            continue
    return tokens
