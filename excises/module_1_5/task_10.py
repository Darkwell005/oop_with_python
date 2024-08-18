from random import randint


class Cell:
    def __init__(self, around_mines: int = 0, mine: bool = False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.pole: list[list['Cell']] = []
        self.init()
        # pprint(self.pole)

    def _fill_cells(self):
        for i in range(self.n):
            temp = []
            for i in range(self.n):
                obj = Cell(around_mines=0, mine=False)
                temp.append(obj)
            self.pole.append(temp)

    def _set_around_mines(self, x, y):
        pass

    def _set_mines(self):
        for _ in range(self.m):
            x = randint(0, self.n - 1)
            y = randint(0, self.n - 1)
            self.pole[x][y].mine = True
            self._set_around_mines(x, y)

    def init(self):
        self._fill_cells()

    def show(self):
        pass
        # for i in range(self.n):
        #     self.pole.append(["x"] * self.n)

    def nums(self, ):
        _nums = []
        for i in range(4):
            temp = []
            for i in range(4):
                # obj = Cell(around_mines=2, mine=False)
                temp.append(i)
            _nums.append(temp)
        return _nums


c1 = Cell(4, False)
pole_game = GamePole(4, 20)
print(pole_game.nums())

[
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3]
]

# TODO:
