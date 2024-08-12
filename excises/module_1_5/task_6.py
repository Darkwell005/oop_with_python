from copy import deepcopy


class Graph:
    def __init__(self):
        self.__data: list = []
        self.__is_show: bool = True

    def set_data(self, data: list) -> None:
        self.__data = data.copy()

    def show_table(self) -> str:
        if not self.__is_show_data():
            return " ".join(map(str, self.__data))

    def show_graph(self):
        if not self.__is_show_data():
            print(f"Графическое отображение данных: {self.show_table()}")

    def show_bar(self):
        if not self.__is_show_data():
            print(f"Столбчатая диаграмма: {self.show_table()}")

    def __is_show_data(self) -> bool:
        if not self.__is_show:
            print("Отображение данных закрыто")
            return True

    def set_show(self, fl_show: bool) -> None:
        # if type(fl_show) != bool:
        #     raise TypeError()

        self.__is_show = fl_show


if __name__ == "__main__":
    data_graph = list(map(int, input().split()))
    g1 = Graph()
    g2 = Graph()
    g1.set_data(data_graph)
    g1.show_graph()
    g1.set_show(False)
    g1.show_graph()
