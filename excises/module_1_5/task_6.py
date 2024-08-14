class Graph:
    def __init__(self):
        self.__data: list = []
        self.__is_show: bool = True

    def set_data(self, data: list) -> None:
        self.__data = data.copy()

    def show_table(self):
        self.__check_show_data('')

    def show_graph(self):
        self.__check_show_data("Графическое отображение данных:")

    def show_bar(self):
        self.__check_show_data("Столбчатая диаграмма:")

    def _table_data(self) -> str:
        return " ".join(map(str, self.__data))

    def __check_show_data(self, msg: str):
        if not self.__is_show:
            print("Отображение данных закрыто")
        else:
            print(msg, self._table_data())

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
    g1.show_table()
    g1.set_show(False)
    g1.show_graph()
