import string
from Tokens import Token

# Lista de todos los tokens
tokens = []

# todos los caracteres reconocidos
diccionario = string.ascii_lowercase + string.ascii_uppercase

# diccionario del diccionario:
# 1-int, 2-double, 3-char, 4-void, 5-return, 6-funcion, 7-for, 8-while, 9-break, 11-and, 12-or, 13-if, 14-elif, 15-else,
# 16-verdad, 17-falso, 18-chorda: string
palabrasReservadas = {1: "int", 2: "gem", 3: "ing", 4: "inan", 5: "red", 6: "clib", 7: "quia", 8: "dum", 9: "finis",
                      10: ";", 11: "et", 12: "vel", 13: "ac si", 14: "alium si", 15: "alium", 16: "verus", 17: "falsus",
                      18: "ch"}

numeros= [0,1,2,3,4,5,6,7,8,9]


def AutomataPalabrasRes(i: int, texto: string):
    palabra = palabrasReservadas[i]
    tam = len(palabra)

    for letra in texto:
        if len(palabra) == 0:
            break
        if letra == palabra[0]:
            palabra = palabra[1::]
            print(len(palabra))
        else:
            break
    if len(palabra) == 0:
        return Token("Datatype", palabrasReservadas[i]), texto[tam::]

    return None, texto

def AutomataIng(i:int,texto:string):
    for i in range(len(texto)):
        letra = texto[i]
        if letra == "'":
            if i+2 <= len(texto):
                if texto[i+2] == "'":
                    return Token("Ingenium", texto[:i+2]), texto[i+3::]
        break
    return None, texto

def AutomataCH(i:int,texto:string):
    aux=""
    leyendo = False
    for i in range(len(texto)):
        letra = texto[i]
        if letra == "\"":
            aux += letra
            if not leyendo:
                leyendo= True
            else:
                break
        elif leyendo:
            aux += letra
    if len(aux) == 0:
        return Token("Chorda", aux), texto[len(aux)::]
    return None, texto

def AutomataNum(numero):
    aux = True
    digits = ""
    for i in numero:
        if i not in numeros:
            break
        else:
            digits += i
            aux = False
    if not aux:
        return Token("Ordo",digits), numero[len(digits)::]




c = AutomataPalabrasRes(1, "int")
print(c)
