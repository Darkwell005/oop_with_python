
class Cell:
    def __init__(self, around_mines: int = 0, mine: bool = None):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.pole = []

        for i in range(self.n):
            self.pole.append(["x"] * self.n)
        print(self.pole)


c1 = Cell(4, False)
pole_game = GamePole(4, 20)
