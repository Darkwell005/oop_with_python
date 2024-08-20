from random import randint


class Cell:
    def __init__(self, around_mines: int = 0, mine: bool = False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:
    def __init__(self, n: int, m: int):
        self.size = n
        self.required_num_of_mines = m
        self.pole: list[list['Cell']] = []
        self.init()

    def _fill_cells(self):
        for _ in range(self.size):
            row = []
            for _ in range(self.size):
                obj = Cell(around_mines=0, mine=False)
                row.append(obj)
            self.pole.append(row)

    def _set_num_of_mines_around(self):
        cells: list[tuple] = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for x in range(self.size):
            for y in range(self.size):
                around_mines: int = sum(
                    (self.pole[i + x][j + y].mine
                     for i, j in cells
                     if 0 <= i + x < self.size and 0 <= j + y < self.size)
                )
                self.pole[x][y].around_mines = around_mines

    def _set_mines(self):
        num_of_installed_mines: int = 0

        # Сломается, когда количество мин
        # значительно превысит количество ячеек
        while num_of_installed_mines < self.required_num_of_mines:
            x = randint(0, self.size - 1)
            y = randint(0, self.size - 1)

            if not self.pole[x][y].mine:
                self.pole[x][y].mine = True
                num_of_installed_mines += 1

            # if num_of_installed_mines >= (self.size ** 2):
            #     break

    def init(self):
        self._fill_cells()
        self._set_mines()
        self._set_num_of_mines_around()

    def show(self):
        for row in self.pole:
            output: str = ""
            for cell in row:
                if not cell.fl_open:
                    output += "# "
                elif not cell.mine:
                    output += f"{cell.around_mines} "
                else:
                    output += "* "

            # Если нужно избежать пробела после последнего символа,
            # используйте join()
            # output = " ".join(output.replace(" ", ""))
            print(output)


if __name__ == "__main__":
    pole_game = GamePole(4, 20)
    pole_game.show()
