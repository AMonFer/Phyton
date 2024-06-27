"""
MODIFY PRODUCTIONS TO SAVE TERMINALS AND NON_TERMINALS
WITH THEIR CORRESPONDING PLACES AND ALTERNATIVES IN A
FORMAT:
    (TERMINAL, PLACE, ALTERNATIVE)
    (NON_TERMINAL, PLACE, ALTERNATIVE)

"""


class Production:
    def __init__(self, name):
        self.name = name
        self.terminals = None
        self.non_terminals = None

    def __place_exists_in_terminals(self, place: int):
        if self.terminals is None:
            return False
        return any([p == place for p, _, _ in self.terminals])

    def __place_exists_in_non_terminals(self, place: int):
        if self.non_terminals is None:
            return False
        return any([p == place for p, _, _ in self.non_terminals])

    def add_terminal(self, terminal, place: int, *args):
        if self.terminals is None:
            self.terminals = []

        if self.__place_exists_in_terminals(place):
            raise NotImplementedError()  # Raise exception when place already exists

        if self.__place_exists_in_non_terminals(place):
            raise NotImplementedError()  # Raise exception when place already exists

        if len(args) == 0:
            self.terminals.append((place, terminal, None))
        else:
            self.terminals.append((place, terminal, args))

    def add_non_terminal(self, non_terminal, place: int, *args):
        if self.non_terminals is None:
            self.non_terminals = []

        if self.__place_exists_in_non_terminals(place):
            # Raise exception when place already exists
            raise RuntimeError(f"Can't add production at place: {place} as it already exists")

        if self.__place_exists_in_terminals(place):
            # Raise exception when place already exists
            raise RuntimeError(f"Can't add terminal at place: {place} as it already exists")

        if len(args) == 0:
            self.non_terminals.append((place, non_terminal, None))
        else:
            self.non_terminals.append((place, non_terminal, args))

    def get_place(self, place: int):
        if self.__place_exists_in_terminals(place):
            for p, terminal, alternative in self.terminals:
                if place == p:
                    return terminal, alternative, "t"

        if self.__place_exists_in_non_terminals(place):
            for p, non_terminal, alternative in self.non_terminals:
                if place == p:
                    return non_terminal, alternative, "p"

        return

    def __eq__(self, other):
        if isinstance(other, Production):
            return self.name == other.name

        # raise when not comparing with a Production
        raise RuntimeError(f"Can't compare a production with a {type(other)}")
