import sys


class ListObject:
    def __init__(self, data):
        self._next_obj = None
        self._data = data

    def link(self, obj: 'ListObject'):
        self._next_obj = obj
        # print(obj._next_obj)

    def __repr__(self):
        return self._data


if __name__ == "__main__":
    lst_in = list(map(str.strip, sys.stdin.readlines()))
    # lst_in = ["10", "20", "30", "40"]
    if lst_in:
        first, *others = lst_in
        # first = list[0]
        # others = list[1:]
        head = ListObject(first)
        prev = head
        for value in others:
            obj = ListObject(value)
            prev.link(obj)
            prev = obj
    else:
        print("Введите что-нибудь")
