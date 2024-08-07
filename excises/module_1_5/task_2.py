class Money:
    def __init__(self, money):
        self.__money = money

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if value < 0:
            raise ValueError('')
        self.__money = value


if __name__ == '__main__':
    my_money = Money(100)
    your_money = Money(1000)
