from pprint import pprint


class Translator:
    def add(self, eng: str, rus: str) -> None:
        if "data" not in self.__dict__:
            self.data = {}
        self.data.setdefault(eng, [])
        if rus not in self.data[eng]:
            self.data[eng].append(rus)

    def remove(self, eng) -> None:
        if eng in self.data:
            self.data.pop(eng)

    def translate(self, eng) -> dict:
        pprint(self.data)
        return self.data.get(eng, ["Ключ не найден"])


if __name__ == '__main__':
    # TODO: Данные в БД должны быть в едином виде

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
