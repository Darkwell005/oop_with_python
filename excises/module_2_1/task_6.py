class Book:
    def __init__(self, author: str, title: str, price: int):
        self.__title = title
        self.__author = author
        self.__price = price

    def set_title(self, title) -> None:
        self.__title = title

    def set_author(self, author) -> None:
        self.__author = author

    def set_price(self, price: int) -> None:
        self.__price = price

    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def get_price(self) -> int:
        return self.__price



