class AppStore:
    apps: dict = {}

    def add_application(self, app: "Application") -> None:
        self.apps[app.name] = app.blocked

    def remove_application(self, app: "Application") -> None:
        if not self.__is_app_not_exists(app):
            self.apps.pop(app.name)

    def block_application(self, app: "Application") -> None:
        if not self.__is_app_not_exists(app):
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
