class AppStore:
    # TODO: 1. Почему словарь?
    #  В словаре Вы храните название приложения, нужно хранить сам объект,
    #  лучше использовать список. Тогда Вам нужно будет в списке найти
    #  элемент и у него изменить атрибует blocked на True
    apps: dict = {}

    def add_application(self, app: "Application") -> None:
        self.apps[app.name] = app.blocked

    def remove_application(self, app: "Application") -> None:
        # INFO: 1. Здесь не нужна проверка, если в методе произойдет исключение,
        # то следующая строка не будет выполнена
        self.__is_app_not_exists(app)
        self.apps.pop(app.name)

    def block_application(self, app: "Application") -> None:
        self.__is_app_not_exists(app)
        self.apps[app.name] = True

    def total_apps(self) -> int:
        return len(self.apps)

    def __is_app_not_exists(self, app) -> None:
        if app.name not in self.apps:
            raise KeyError("Такого приложения нету в магазине")


class Application:
    def __init__(self, name: str, blocked=False):
        self.name = name
        self.blocked = blocked


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
