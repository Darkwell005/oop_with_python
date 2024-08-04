from pprint import pprint


class Tomato:
    states: dict[int, str] = {
        0: "Отсутствует",
        1: "Цветение",
        2: "Зеленый",
        3: "Красный"
    }

    def __init__(self, index: int) -> None:
        self._index = index
        self.__count = 0
        self._state = self.states[0]

    def grow(self) -> None:
        if not self.is_ripe():
            self.__count += 1
            self._state = self.states[self.__count]

    def is_ripe(self) -> bool:
        return self.__count == (len(self.states) - 1)
        # return self._state == self.states[len(self.states) - 1]

    def get_index(self) -> int:
        return self._index


class TomatoBush:
    def __init__(self, quantity):
        self.tomatoes: list[Tomato] = [
            Tomato(i) for i in range(quantity)
        ]
        # pprint(self.tomatoes)

    def find(self, target: int) -> bool:
        for tomato in self.tomatoes:
            if tomato.get_index() == target:
                return True
        return False

    def remove(self, target: int) -> None:
        self.tomatoes = [
            tomato for tomato in self.tomatoes
            if tomato.get_index() != target
        ]

    def grow_all(self) -> None:
        # for tomato in self.tomatoes:
        #     tomato.grow()
        [tomato.grow() for tomato in self.tomatoes]

    def all_are_ripe(self) -> bool:
        return all(
            [tomato.is_ripe() for tomato in self.tomatoes]
        )

    def give_away_all(self) -> None:
        if self.all_are_ripe():
            self.tomatoes.clear()


class Gardener:
    def __init__(self, name: str, plant: "TomatoBush") -> None:
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print("Не все помидоры созрели...")

    @staticmethod
    def knowledge_base() -> None:
        print(
            """
            1. Установка живой изгороди и забора
                Живая изгородь в саду
            2. Установка газона в саду
            3. Посадка деревьев и кустарников
            """
        )


if __name__ == "__main__":
    tb = TomatoBush(5)
    # tb.remove(3)
    # print(tb.find(3))
    Gardener.knowledge_base()
