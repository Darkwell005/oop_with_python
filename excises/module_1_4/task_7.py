import sys


class StreamData:
    def _is_same_length(self, fields, lst_values) -> bool:
        return len(fields) == len(lst_values)

    def create(self,
               fields: tuple[str, ...],
               lst_values: list[str]) -> bool:
        if not self._is_same_length(fields, lst_values):
            return False

        for key, value in zip(fields, lst_values):
            self.__dict__[key] = value
        return True


class StreamReader:
    FIELDS: tuple[str, ...] = ("id", "title", "pages")

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


if __name__ == '__main__':
    sr = StreamReader()
    data, result = sr.readlines()
    print(data.__dict__)
