class CLock:
    def __init__(self):
        self.__time = 0

    def set_time(self, tm: int) -> None:
        if self.__check_time(tm):
            self.__time = tm
        raise ValueError("Указано некорректное число")

    def get_time(self) -> int:
        return self.__time

    def __check_time(self, tm: int) -> bool:
        if 0 <= tm < 100000:
            return True
        return False


clock = CLock()
