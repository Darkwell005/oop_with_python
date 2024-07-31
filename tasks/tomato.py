class Tomato:
    states = {}

    def __init__(self, _index, _state=states[0]):
        self._index = _index
        self._state = _state

    def grow(self):
        pass

    def is_ripe(self):
        pass


class TomatoBush:
    def __init__(self, quantity):
        pass
        self.tomatoes = ...

    def graw_all(self):
        pass

    def all_are_ripe(self):
        pass

    def give_away_all(self):
        pass


class Gardener:
    def __init__(self, name, _plant):
        self.name = name

    def work(self):
        pass

    def harvest(self):
        pass

    @staticmethod
    def knowledge_base():
        pass
