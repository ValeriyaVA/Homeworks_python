from abc import abstractmethod


class Clothes:
    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):
    def __init__(self, size: float):
        self.size = size

    @property
    def calculate(self):
        return "%.2f" % (self.size / 6.5 + 0.5)


class Costume(Clothes):
    def __init__(self, height: float):
        self.height = height

    @property
    def calculate(self):
        return "%.2f" % (2 * self.height + 0.3)


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3
