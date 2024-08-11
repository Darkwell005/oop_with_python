class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __is_number(self):
        return not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c)))

    def __is_natural_number(self):
        if self.__is_number():
            return not all(map(lambda x: x > 0, (self.a, self.b, self.c)))

    def __is_triangle(self):
        if not (self.__is_number() and self.__is_natural_number()):
            return (self.a >= self.b + self.c or self.b
                    >= self.a + self.c or self.c >= self.a + self.b)

    def is_triangle(self):
        if self.__is_number() or self.__is_natural_number():
            return 1
        if self.__is_triangle():
            return 2
        return 3


if __name__ == "__main__":
    # TODO:

    tr = TriangleChecker(2, 3, 2)
    print(tr.is_triangle())
