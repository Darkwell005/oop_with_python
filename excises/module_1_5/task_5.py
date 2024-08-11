class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __is_number(self):
        return all(
            map(
                lambda x: isinstance(x, (int, float)),
                (self.a, self.b, self.c)
            )
        )

    def __is_natural_number(self):
        if self.__is_number():
            return all(
                map(
                    lambda x: x > 0,
                    (self.a, self.b, self.c)
                )
            )
        return False

    def __is_triangle(self):
        return (
            self.a + self.b > self.c
            and self.a + self.c > self.b
            and self.b + self.c > self.a
        )

    def is_triangle(self):
        if not (self.__is_number() and self.__is_natural_number()):
            return 1
        if not self.__is_triangle():
            return 2
        return 3


if __name__ == "__main__":
    tr = TriangleChecker(3, 4, 5)
    tr2 = TriangleChecker(2, 3, 2)
    print(tr.is_triangle())
    print(tr2.is_triangle())
