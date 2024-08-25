TYPE_OS: int = 1


class DialogWindows:
    name_class: str = "DialogWindows"


class DialogLinux:
    name_class: str = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        some_obj = None

        if TYPE_OS == 1:
            some_obj = super().__new__(DialogWindows)
        elif TYPE_OS == 2:
            some_obj = super().__new__(DialogLinux)
        some_obj.name = args[0]
        return some_obj


if __name__ == "__main__":
    dlg = Dialog("DialogWindows")
    print(type(dlg))
    print(dlg)

    print('-----------------------')
    TYPE_OS = 2
    dlg2 = Dialog("DialogLinux")
    print(type(dlg2))
    print(dlg2)
