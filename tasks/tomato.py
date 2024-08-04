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
        self._state = self.states[self.__count]

    def grow(self) -> None:
        self.__count += 1
        self._state = self.states[self.__count]

    def is_ripe(self) -> bool:
        return self._state == self.states[3]


class TomatoBush:
    def __init__(self, quantity):
        self.tomatoes: list[Tomato] = [
            Tomato(i) for i in range(quantity)
        ]

    def graw_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        pass

    def give_away_all(self) -> None:
        pass


class Gardener:
    def __init__(self, name: str, plant: "TomatoBush") -> None:
        self.name = name
        self._plant = plant

    def work(self):
        # self._plant.tomatoes
        pass

    def harvest(self):
        pass

    @staticmethod
    def knowledge_base() -> None:
        pass



