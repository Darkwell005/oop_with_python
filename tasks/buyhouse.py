class Human:
    default_name: str = "Неизвестный"
    default_age: int = 0

    def __init__(self,
                 name: str = default_name,
                 age: int = default_age) -> None:
        self.name = name
        self.age = age
        # if age < 0:
        #     print("Укажите корректное значение, большее 0")
        self.__money: int = 0
        self.__house: "House" | None = None

    def info(self) -> None:
        print(self)

    @staticmethod
    def default_info() -> None:
        print(Human.default_name, Human.default_age)

    def __make_deal(self, obj: "House", price: float | int) -> None:
        self.__house = obj
        self.__money -= price

    def _validate(self, value) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(
                "Укажите числовое значение"
            )

        if value < 0:
            raise ValueError(
                "Укажите корректное значение больше 0"
            )

    def earn_money(self, value: int | float) -> None:
        self._validate(value)
        self.__money += value

    def _has_money(self, other) -> None:
        if self.__money < other:
            raise ValueError(
                "Похоже у Вас недостаточно средств"
            )

    def buy_house(self, house: "House", discount: int) -> None:
        self._validate(discount)
        price = house.final_price(discount)
        self._has_money(price)
        self.__make_deal(house, price)

    def __str__(self) -> str:
        return (f'\nВозраст: {self.age}'
                f'\nИмя: {self.name}'
                f'\nДом: {self.__house}'
                f'\nБаланс: ${self.__money}')


class House:
    def __init__(self, area: int, price: int):
        self._validate((area, price))
        self._area = area
        self._price = price

    def _validate(self, data: tuple | list) -> None:
        for value in data:
            if value < 0:
                raise ValueError(
                    "Укажите корректное значение, большее 0"
                )

    def final_price(self, discount: int) -> float:
        return (
                self._price * (100 - discount) // 100
        )

    def __str__(self):
        return f"Площадь {self._area}м2, цена ${self._price}"


class SmallHouse(House):
    __AREA = 40

    def __init__(self, price: float | int) -> None:
        super().__init__(area=self.__AREA, price=price)


if __name__ == '__main__':
    Human.default_info()
    human = Human("Вася", 20)
    human.info()

    small_house = SmallHouse(700)
    # human.buy_house(small_house, 25)
    human.earn_money(700)
    human.buy_house(small_house, 25)
    human.info()

    big_house = House(165, 1900)
    human.buy_house(big_house, 95)
    human.info()
