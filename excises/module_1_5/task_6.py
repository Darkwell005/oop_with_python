from copy import deepcopy


class Graph:
    def __init__(self):
        self.__local_data = []
        self.__is_show = True

    def set_data(self, data: list) -> None:
        self.__local_data = data.copy()

    def show_table(self) -> str:
        return " ".join(map(str, self.__local_data))

    def show_graph(self):
        pass

    def show_bar(self):
        pass

    def set_show(self, fl_show: bool) -> None:
        # if type(fl_show) != bool:
        #     raise TypeError()

        self.__is_show = fl_show


if __name__ == "__main__":
    g1 = Graph()
    g2 = Graph()
