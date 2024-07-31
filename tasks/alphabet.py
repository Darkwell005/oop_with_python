import string


class Alphabet:
    def __init__(self, lang: str, letters: str) -> None:
        self.lang = lang
        self.letters = letters
        print(letters)

    def print(self) -> None:
        print(self.letters)

    def letters_num(self) -> int:
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = len(string.ascii_uppercase)

    def __init__(self) -> None:
        super().__init__("En", string.ascii_uppercase)
        # Alphabet.__init__(self, "En", string.ascii_uppercase)

    def is_en_letter(self, letter: str) -> bool:
        return letter.upper() in self.letters

    def letters_num(self) -> int:
        return self.__letters_num

    @staticmethod
    def example() -> str:
        return "The quick brown fox jumps over the lazy dog"


if __name__ == "__main__":
    eng = EngAlphabet()
    print(eng.letters_num())
    print(eng.is_en_letter("F"))
    print(eng.is_en_letter("щ"))
    EngAlphabet.example()
