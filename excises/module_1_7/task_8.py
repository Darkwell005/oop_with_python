import string


class CardCheck:
    __digits: str = string.digits
    __ascii_lowercase: str = string.ascii_uppercase
    __CHARS_FOR_NAME: str = __ascii_lowercase + __digits

    @staticmethod
    def check_card_number(number: str) -> bool:
        return (number.count("-") == 3
                and number.replace("-", "").isdigit()
                and all(
            [len(x) == 4 for x in number.split("-")]))

    @classmethod
    def check_name(cls, name) -> bool:
        return all([x in cls.__CHARS_FOR_NAME for x in "".join(name.split())])


is_number = CardCheck.check_card_number("1254-223-2235-3435")
is_name = CardCheck.check_name("SERGEI BALAKIREV")

print(is_number)
