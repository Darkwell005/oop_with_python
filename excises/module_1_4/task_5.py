class Graph:
    LIMIT_Y: list[int] = [0, 10]

    def set_data(self, data: list[int]):
        self.data = data

    def draw(self):
        start, end = self.LIMIT_Y
        print(
            " ".join(
                [
                    str(num) for num in self.data
                    if num in range(start, end + 1)
                ]
            )
        )


if __name__ == "__main__":
    test_data: list[int] = [
        10, -5, 100, 20, 0, 80, 45, 2, 5, 7
    ]

    g = Graph()
    g.set_data(test_data)
    g.draw()
