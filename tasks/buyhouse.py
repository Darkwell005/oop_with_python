class Human:
    default_name: str = "Неизвестный"
    default_age: int = -1

    def __init__(self,
                 name: str = default_name,
                 age: int = default_age):
        self.name = name
        self.age = age
        self.__money: int = 0
        self.__house: 'House' | None = None

    # TODO: 1. Пункт 4: Реализуйте справочный метод info(),
    #  который будет выводить поля name, age, house и money.

    def default_info(self):
        print(self.default_name, self.default_age)

    def some_method(self, obj: 'House', discount: float):
        price = obj.final(discount)


class House:
    pass


if __name__ == '__main__':
    unknown = Human()
    house = House()
    unknown.some_method(house, 25)
    print(unknown.__dict__)
