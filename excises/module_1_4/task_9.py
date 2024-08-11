import sys


class DataBase:
    lst_data = []
    FIELDS = ("id", "name", "old", "salary")

    def insert(self, data):
        for x in data:
            self.lst_data.append(dict(zip(self.FIELDS, x.split())))

    def select(self, a, b):
        return self.lst_data[a:b + 1]


if __name__ == "__main__":
    lst_in = list(map(str.strip, sys.stdin.readlines()))
