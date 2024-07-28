import string


class Alphabet:
    def __init__(self, lang: str, letters: str):
        self.lang = lang
        self.letters = letters
        print(letters)

    # TODO: 1. Пункт 3: Создайте метод print(),
    #  который выведет в консоль буквы алфавита

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = len(string.ascii_uppercase)

    def __init__(self):
        super().__init__("En", string.ascii_uppercase)
        # Alphabet.__init__(self, "En", string.ascii_uppercase)

    def is_en_letter(self, letter: str):
        return letter in self.letters

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return "HELLO"


if __name__ == "__main__":
    eng = EngAlphabet()
    print(eng.letters_num())
    print(eng.is_en_letter("F"))
    print(eng.is_en_letter("Щ"))
    EngAlphabet.example()
