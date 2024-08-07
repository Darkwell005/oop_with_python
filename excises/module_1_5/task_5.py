class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))):
            return 1
        if not all(map(lambda x: x > 0, (self.a, self.b, self.c))):
            return 1
        elif (self.a >= self.b + self.c or self.b
              >= self.a + self.c or self.c >= self.a + self.b):
            return 2
        return 3

tr = TriangleChecker(2, 3, 7)
print(tr.is_triangle())