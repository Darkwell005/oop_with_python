import string


class Alphabet:
    def __init__(self, lang: str, letters: str):
        self.lang = lang
        self.letters = letters
        print(letters)

    def letters_num(self):
        return len(self.letters)


def example():
    return "HELLO"


class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__("En", string.ascii_uppercase)

    __letters_num = len(string.ascii_uppercase)

    def is_en_letter(self, letter):
        return letter in self.letters

    def letters_num(self):
        return self.__letters_num


eng = EngAlphabet()
print(eng.letters_num())
print(eng.is_en_letter("F"))
print(eng.is_en_letter("Щ"))
print(example())
