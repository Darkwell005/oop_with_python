# from modules_packages.work_module_and_package.task_4 import BITS_PER_MEGABYTE
# from modules_packages.work_module_and_package import BITS_PER_MEGABYTE
from modules_packages import BITS_PER_MEGABYTE


# Example
class Math:

    @staticmethod
    def sqrt(value) -> float:
        return value ** (0.5)

    @staticmethod
    def cos():
        pass


if __name__ == '__main__':
    print(__name__)
    Math.sqrt(16)
    mt = Math()
    mt.sqrt(25)

    print(BITS_PER_MEGABYTE)
