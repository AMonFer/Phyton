# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Preprocesador import preprocess
from Automatas import get_tokens
from Parser import temporal_parser


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    preprocessed_text = preprocess("prueba.phy")
    print(f"After the preprocess: {preprocessed_text}")

    tokens = get_tokens(preprocessed_text)
    print("The tokens are:")
    for token in tokens:
        token.token_type()
        # print(f"token name: {token.name} - token value: {token.value}")

    temporal_parser(tokens)

# See PyCharm help at https://www.jetbrains.com/help/p
