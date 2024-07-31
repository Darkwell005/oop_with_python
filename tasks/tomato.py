class Tomato:
    states: dict[int, str] = {
        0: "Отсутствует",
        1: "Цветение",
    }

    def __init__(self, index: int) -> None:
        self._index = index
        self.__count = 0
        self._state = self.states[self.__count]

    def grow(self):
        pass

    def is_ripe(self) -> bool:
        pass


class TomatoBush:
    def __init__(self, quantity):
        self.tomatoes: list[Tomato] = [
            Tomato(i) for i in range(quantity)
        ]

    def graw_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self) -> bool:
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
