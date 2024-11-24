class A:
    # атрибут, поле, свойство | класса
    SOME_VAR: int = 101

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        print(f"[__new__] {id(obj)}")
        obj.age = 10

        return obj

    def __init__(self, name: str) -> None:
        print(f"[__init__] {id(self)}")
        # атрибут, поле, свойство | экземпляра
        self.name = name

    def __call__(self, *args, **kwargs):
        return "О, меня вызвали"

    def __repr__(self) -> str:
        return "bla bla"

    def __str__(self) -> str:
        return "__from__str__"


a_1 = A("A1")
print(a_1)
a_2 = A("A2")
a_3 = A("A3")

print(
    id(a_1),
    id(a_2),
    id(a_3),
    sep="\n"
)

print(a_1.__dict__)
print(A.__dict__)

print(a_1())
