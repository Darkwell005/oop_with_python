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
