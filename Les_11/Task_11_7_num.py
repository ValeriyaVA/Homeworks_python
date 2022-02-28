class ComplexNumber:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        if self.y > 0:
            return f'{self.x}+{self.y}i'
        elif self.y < 0:
            return f'{self.x}{self.y}i'
        elif self.y == 0:
            return f'{self.x}'

    def __add__(self, other):
        return ComplexNumber(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return ComplexNumber(self.x*other.x - self.y*other.y, self.x*other.y + self.y*other.x)

num1 = ComplexNumber(5, 4)
num2 = ComplexNumber(7.7, 2.5)
num3 = ComplexNumber(3, 8.8)
num4 = ComplexNumber(6, -8.8)
print(num1 + num3)
print(num3 + num4)
print(num1 * num2)