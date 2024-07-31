class Human:
    default_name: str = "Неизвестный"
    default_age: int = 0

    def __init__(self,
                 name: str = default_name,
                 age: int = default_age):
        self.name = name
        self.age = age
        if age < 0:
            print("Укажите корректное значение, большее 0")
        self.__money: int = 0
        self.__house: "House" | None = None

    def info(self):
        print(self.age, self.name, self.__house, self.__money)

    def default_info(self):
        print(self.default_name, self.default_age)

    def __make_deal(self, obj: "House", price: int):
        self.obj = obj
        self.price = price
        self.__money -= price

    def earn_money(self, value: int | float):
        if value < 0:
            print("Укажите корректное значение, большее 0")
        else:
            self.__money += value

    def buy_house(self, obj, discount: int):
        if discount < 0:
            print("Укажите корректное значение скидки, большее 0")
        else:
            price = obj.final_price(discount)
            if self.__money < price:
                print("Похоже у Вас недостаточно средств")
            else:
                self.__house = obj


class House:
    def __init__(self, _area: int, _price: int):
        self._area = _area
        self._price = _price
        if _price < 0 or _area < 0:
            print("Укажите корректное значение, большее 0")

    def final_price(self, discount: int):
        return self._price * discount // 100


class SmallHouse(House):
    def __init__(self):
        super().__init__(_area=40, _price=0)


human = Human()

human.info()
house = House(50, 1000)
small_house = SmallHouse()
human.buy_house(house, 25)
human.earn_money(1000)
human.buy_house(house, 25)
human.info()

