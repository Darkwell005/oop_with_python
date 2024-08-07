class Translator:
    def add(self, eng: str, rus: str) -> None:
        if "translate" not in self.__dict__:
            self.translate = {}
        self.translate.setdefault(eng, [])
        if rus not in self.translate[eng]:
            self.translate[eng].append(rus)

    def remove(self, eng) -> None:
        if eng in self.translate:
            self.translate.pop(eng)

    def translate(self, eng) -> dict:
        return self.translate[eng]


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
print(*tr.translate.get("go"))
