import sys


class ListObject:
    def __init__(self, data):
        self._next_obj = None
        self._data = data

    def link(self, obj: 'ListObject'):
        self._next_obj = obj
        print(obj._next_obj)




if __name__ == "__main__":
    lst_in = list(map(str.strip, sys.stdin.readlines()))
    head_obj = ListObject("hello")
    second_obj = ListObject("world")
    head_obj.link(second_obj)
    print(head_obj._next_obj)
    print(second_obj)
