from random import choice, choices


class Shape:
    def __init__(self, a, b, c, d):
        self.sp: tuple[int, int] = (a, b)
        self.ep: tuple[int, int] = (c, d)

    def __str__(self):
        return f"{self.__class__.__name__}(sp={self.sp}, ep={self.ep})"


class Line(Shape):
    pass


class Rect(Shape):
    pass


class Ellipse(Shape):
    pass


if __name__ == "__main__":
    ARGS_COUNT: int = 4
    models: list = [Ellipse, Line, Rect]

    elements = []
    for _ in range(217):
        model = choice(models)
        if model == Line:
            elements.append(model(0, 0, 0, 0))
        else:
            items: list[int] = choices(range(10, 100),
                                       k=ARGS_COUNT)
            elements.append(model(*items))

    print(*elements, sep='\n')
