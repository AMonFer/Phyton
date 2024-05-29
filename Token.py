import string


class Token:
    def __init__(self, name: string, value):
        self.name = name
        self.value = value

    def token_type(self):
        print(f"This is a {self.name} token with value {self.value}")

    def __eq__(self, other):
        if isinstance(other, Token):
            name = other.name
            value = other.value

            return name == self.name and value == self.value
        elif isinstance(other, str):
            return other == self.name
        else:
            raise NotImplementedError()  # raise exception when other is not a Token or a string
