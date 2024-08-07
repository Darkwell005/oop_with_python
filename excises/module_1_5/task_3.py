class Point:
    def __init__(self, x: int, y: int, color: str = "black"):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return (f"{self.__class__.__name__}(x={self.x}, "
                f"y={self.y}, color='{self.color}')")


if __name__ == "__main__":
    points = [Point(2 * x + 1, 2 * x + 1) for x in range(1000)]
    # points = [Point(x, x) for x in range(1, 2001, 2)]
    points[1].color = "yellow"
    print(points[1])
