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
        result_get_place = production_to_look_in.get_place(place)
        if result_get_place is None:
            break
        main_option, alternatives, type_of_value = result_get_place
        if type_of_value == "p":
            if main_option == production_to_look_for:
                result.append(main_option)

        if alternatives is None:
            place += 1
            continue

        for alternative in alternatives:
            if isinstance(alternative, Production):
                if production_to_look_for == alternative:
                    result.append(alternative)

        place += 1
    return result


def get_follow(production, processed=set()):
    resultados = []
    if str(production) in processed:
        return resultados

    processed.add(str(production))
    pr = None

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
                            pr = prod.get_place(place + 1)
                            if pr is None:
                                resultados += get_follow(prod, processed)
                            else:
                                val, alt, term = pr
                                if term == "t":
                                    resultados.append(val)
                                else:
                                    resultados += get_first(val)
                        else:
                            if alternativas is not None:
                                for a in alternativas:
                                    if a == production:
                                        pr = prod.get_place(place + 1)
                                    if pr is None:
                                        resultados += get_follow(prod, processed)
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


class ParsingTable:
    def __init__(self, prods):
        self.productions = prods
        self.table = {}
        self.construct_parsing_table()

    def construct_parsing_table(self):
        for production in self.productions:
            first_set = get_first(production)
            follow_set = get_follow(production)
            self.add_to_table(production, first_set)
            self.add_to_table(production, follow_set, follow=True)

    def add_to_table(self, production, token_set, follow=False):
        if production.name not in self.table:
            self.table[production.name] = {}

        for token in token_set:
            token_key = str(token)
            if token_key not in self.table[production.name]:
                self.table[production.name][token_key] = production
            elif follow:
                if '$' in token_set:
                    if '$' not in self.table[production.name]:
                        self.table[production.name]['$'] = production

    def print_table(self):
        print("Parsing Table:")
        for non_terminal, rules in self.table.items():
            print(f"{non_terminal}:")
            for token, production in rules.items():
                print(f"  {token} -> {production.name}")


parsing_table = ParsingTable(productions)
parsing_table.print_table()

