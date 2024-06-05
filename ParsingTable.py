from LanguageProductions import *


def get_first(production):
    main_option, alternatives, type_of_value = production.get_place(1)
    result = []
    if type_of_value == "t":
        result.append(main_option)
    else:
        first_of_production = get_first(main_option)
        result += first_of_production

    if alternatives is not None:
        for alternative in alternatives:
            first_of_production = get_first(alternative)
            result += first_of_production

    return result


def find_production_as_option(production_to_look_for, production_to_look_in):
    place = 1
    result = []
    while True:
        main_option, alternatives, type_of_value = production_to_look_in.get_place(place)
        if type_of_value == "p":
            if main_option == production_to_look_for:
                next_option, next_alternatives, type_of_value = production_to_look_in.get_place(place+1)


def get_follow(production):
    resultados = []
    for p in productions:
        lista_prod = find_production_as_option(production, p)
        for prod in lista_prod:
            place = 1
            while True:
                aux = prod.get_place(place)
                if aux is not None:
                    valor, alternativas, terminal = aux
                    if terminal == "p":
                        if valor == production:
                            pr = prod.get_place(place+1)

                            if pr is None:
                                resultados += get_follow(prod)
                            else:
                                val, alt, term = pr
                                if term == "t":
                                    resultados.append(val)
                                else:
                                    resultados += get_first(val)
                        else:
                            for a in alternativas:
                                if a == production:
                                    pr = prod.get_place(place + 1)

                                    if pr is None:
                                        resultados += get_follow(prod)
                                    else:
                                        val, alt, term = pr
                                        if term == "t":
                                            resultados.append(val)
                                        else:
                                            resultados += get_first(val)
                    else:
                        resultados.append(valor)
                else:
                    break

                place += 1
    return resultados














