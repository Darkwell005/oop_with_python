from typing import Type


class Factory:
    @staticmethod
    def build_sequence() -> list:
        return []

    @staticmethod
    def build_number(string: str) -> int:
        return int(string)


class Loader:
    @staticmethod
    def parse_format(string: str, factory: Type[Factory]) -> list[int]:
        seq = factory.build_sequence()
        [seq.append(factory.build_number(sub)) for sub in string.split(", ")]

        return seq


res = Loader.parse_format("4, 5, -6", Factory)
print(res)
