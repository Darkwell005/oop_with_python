TYPE_OS: int = 1


class DialogWindows:
    name_class: str = "DialogWindows"


class DialogLinux:
    name_class: str = "DialogLinux"


class Dialog:
    __OS: [int, object] = {
        1: DialogWindows,
        2: DialogLinux
    }

    def __new__(cls, *args, **kwargs):
        first, *_ = args
        # TODO:
        _class: object = cls.__OS.get(TYPE_OS)
        instance = super().__new__(_class)
        instance.name = first
        print(args, kwargs)
        return instance

    def __init__(self, name: str) -> None:
        self.name = name


if __name__ == "__main__":
    dlg = Dialog("DialogWindows")
    print(type(dlg))
    print(dlg.name)

    print('-----------------------')
    TYPE_OS = 1
    dlg2 = Dialog("DialogLinux")
    print(type(dlg2))
    print(dlg2.name)
