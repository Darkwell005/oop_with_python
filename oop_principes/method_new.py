class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            new_instance = super().__new__(cls)
            cls.__instance = new_instance

        return cls.__instance


s_1 = Singleton()
s_2 = Singleton()
s_3 = Singleton()


print(
    id(s_1),
    id(s_2),
    id(s_3),
    sep="\n"
)

