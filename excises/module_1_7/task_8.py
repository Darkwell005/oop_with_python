import string


class CardCheck:
    digits: str = string.digits
    ascii_lowercase: str = string.ascii_lowercase
    CHARS_FOR_NAME: str = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number: str) -> bool:
        if number.count("-") != 3:
            return False
        else:
            if (all([x.isdigit() for x in "".join(number.split("-"))])
                    and all([len(x) == 4 for x in number.split("-")])):
                return True
            return False

    @classmethod
    def check_name(cls, name) -> bool:
        if all([x in cls.CHARS_FOR_NAME for x in "".join(name.split())]):
            return True
        return False


is_number = CardCheck.check_card_number("1224-2123-2345-3435")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
