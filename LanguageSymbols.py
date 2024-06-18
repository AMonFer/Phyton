import string
# todos los caracteres reconocidos
identificadores = string.ascii_lowercase + string.ascii_uppercase

# diccionario de palabras reservadas:
# Values from 1 to 4 are be Datatypes

# 1-int, 2-double, 3-char, 4-void, 5-chorda: string, 6-return, 7-funcion,
# 8-for, 9-while, 10-break, 11-and, 12-or, 13-if : ac si, 14-elif : alium si,
# 15-else, 16-verdad, 17-falso
palabrasReservadas = {1: "int", 2: "gem", 3: "ing", 4: "inan", 5: "ch", 6: "red", 7: "clib",
                      8: "quia", 9: "dum", 10: "finis", 11: "et", 12: "vel", 13: "acsi", 14: "aliumsi",
                      15: "alium", 16: "verus", 17: "falsus"}

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = [';', ',', '(', ')', '{', '}', '[', ']']

assignments = ["=", "+=", "-="]

binary_operators = ["*", "-", "/", "+", "mod"]

unary_operators = ["++", "--"]

comparadores = [">", "<", "==", "<=", ">=", "!="]
