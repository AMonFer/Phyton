import string


class Token:
    def __init__(self, name: string, value):
        self.name = name
        self.value = value

    def token_type(self):
        print(f"This is a {self.name} token with value {self.value}")
