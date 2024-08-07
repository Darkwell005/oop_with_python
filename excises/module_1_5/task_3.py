class Point:
    def __init__(self, x: int, y: int, color: str = "black"):
        self.x = x
        self.y = y
        self.color = color


points = [Point(2 * x + 1, 2 * x + 1) for x in range(1000)]

points[1].color = "yellow"
