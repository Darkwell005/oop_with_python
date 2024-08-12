from pprint import pprint


class Translator:
    def add(self, eng: str, rus: str) -> None:
        if "data" not in self.__dict__:
            self.data = {}
        self.data.setdefault(eng.lower(), [])
        if rus.lower() not in self.data[eng.lower()]:
            self.data[eng].append(rus)

    def remove(self, eng) -> None:
        if eng.lower() in self.data:
            self.data.pop(eng)

    def translate(self, eng) -> dict:
        pprint(self.data)
        return self.data.get(eng.lower(), ["Ключ не найден"])


if __name__ == '__main__':

    tr = Translator()
    tr.add("tree", "дерево")
    tr.add("car", "машина")
    tr.add("car", "автомобиль")
    tr.add("leaf", "лист")
    tr.add("river", "река")
    tr.add("go", "идти")
    tr.add("go", "ехать")
    tr.add("go", "ходить")
    tr.add("Go", "ходить")
    tr.add("milk", "молоко")
    tr.remove("car")
    print(*tr.translate("go"))
