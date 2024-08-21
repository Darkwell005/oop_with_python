class Factory:
    def build_sequence(self) -> list:
        return []

    def build_number(self, string: str) -> float:
        return float(string)


class Loader:
    def parse_format(self, string: str, factory: "Factory") -> list[float]:
        seq = factory.build_sequence()
        for sub in string.split(", "):
            item = factory.build_number(sub)
            seq.append(item)
        return seq


ld = Loader()
res = ld.parse_format("4, 5, -6.5", Factory())

print(res)
