class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return ": ".join([str(x) for x in [self.name, self.price]])


class Cart:
    def __init__(self):
        self.goods: list = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx: int):
        self.goods.pop(indx)

    def get_list(self):
        for item in self.goods:
            for value in item:
                print(value)


class Table(Product):
    pass


class TV(Product):
    pass


class NoteBook(Product):
    pass


class Cup(Product):
    pass


gd = (
    TV("Lenovo", 11000), TV("Samsung", 15000),
    Table("Console", 5000), NoteBook("Linux", 120000),
    NoteBook("Gigabyte", 100000)
)

cart = Cart()
cart.add(gd)

cart.get_list()
