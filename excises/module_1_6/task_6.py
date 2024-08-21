class AbstractCLass:
    def __new__(cls, *args, **kwargs):
        return "Ошибка нельзя создавать объекты абстрактного класса"


obj = AbstractCLass()
