from abc import abstractmethod, ABC

__all__ = [
    "House",
    "SmallHouse",
    "LargeHouse",
    "MediumHouse"
]


class BaseHouse(ABC):  # Родительский класс
    """Абстрактный класс."""

    FLOOR: int = 1

    @abstractmethod
    def get_house_type(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    def some_method(self):
        pass


class House(BaseHouse):  # Дочерный класс
    "Базовый класс."

    def __init__(self, address: str, floor: int) -> None:
        self.address = address
        self.floor = floor

    # Обязательное переопределение абстрактного метода
    def get_house_type(self):
        return type(self)

    # Обязательное переопределение абстрактного метода
    def get_info(self):
        print(
            f'\nАдрес: {self.address}'
            f'\nКоличество этажей: {self.floor}'
        )
        print('-----------------------')


class SmallHouse(House):
    pass


class MediumHouse(House):
    pass


class LargeHouse(House):
    pass


class Cottedge(SmallHouse):
    def __init__(self, address: str, floor: int, rooms: int):
        super().__init__(address, floor)
        self.rooms = rooms


# -----------------------

small = SmallHouse('пр.Ленина 19', 5)
print(small.get_house_type())
small.get_info()

# -----------------------

house_one = House('ул.Пушкина 4', 9)

print(house_one.get_house_type())
house_one.get_info()

cottedge = Cottedge('ул.Загородная', 2, 8)
