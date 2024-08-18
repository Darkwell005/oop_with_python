from pprint import pprint


class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.name}: {self.price}"


class Cart:
    def __init__(self):
        self.goods: list = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx: int):
        self.goods.pop(indx)

    def get_list(self) -> list[str]:
        result: list[str] = []
        for item in self.goods:
            result.append(f"{item.name}: {item.price}")
        return result


class Table(Product):
    pass


class TV(Product):
    pass


class NoteBook(Product):
    pass


class Cup(Product):
    pass


products: tuple[Product, ...] = (
    TV("Lenovo", 11000),
    TV("Samsung", 15000),
    Table("Console", 5000),
    NoteBook("Linux", 120000),
    NoteBook("Gigabyte", 100000),
    Cup("Coffee", 100)
)

cart = Cart()
for product in products:
    cart.add(product)

pprint(cart.get_list())
