import re


class ComplexNumber:
    def __init__(self, str_number: str):
        assert re.match(r'\d*\.?\d*[+-]?\d*\.?\d*i?', str_number), f'{str_number} - комплексный обед, но не число'
        if '+' in str_number:
            self.number = float(str_number[0:str_number.find('+')])
            self.i_number = float(str_number[str_number.find('+'):-1])
        elif '-' in str_number:
            self.number = float(str_number[0:str_number.find('-')])
            self.i_number = float(str_number[str_number.find('-'):-1])
        else:
            self.number = float(str_number)
            self.i_number = 0

    def __str__(self):
        if self.i_number > 0:
            return str(f'{self.number}+{self.i_number}i')
        elif self.i_number < 0:
            return str(f'{self.number}{self.i_number}i')
        elif self.i_number == 0:
            return str(self.number)

    def __add__(self, other):
        if self.i_number + other.i_number > 0:
            return ComplexNumber(f'{self.number + other.number}+{self.i_number + other.i_number}i')
        elif self.i_number + other.i_number < 0:
            return ComplexNumber(f'{self.number + other.number}{self.i_number + other.i_number}i')
        elif self.i_number + other.i_number == 0:
            return ComplexNumber(f'{self.number + other.number}')

    def __mul__(self, other):
        if self.number * other.i_number + self.i_number * other.number > 0:
            return ComplexNumber(
                f'{self.number * other.number - self.i_number * other.i_number}+{self.number * other.i_number + self.i_number * other.number}')
        elif self.number * other.i_number + self.i_number * other.number < 0:
            return ComplexNumber(
                f'{self.number * other.number - self.i_number * other.i_number}{self.number * other.i_number + self.i_number * other.number}')
        elif self.number * other.i_number + self.i_number * other.number == 0:
            return ComplexNumber(f'{self.number * other.number - self.i_number * other.i_number}')


num1 = ComplexNumber('5+4i')
num2 = ComplexNumber('7.7+2.5i')
num3 = ComplexNumber('3-8.8i')
num4 = ComplexNumber('6+8.8i')
print(num1 + num3)
print(num3 + num4)
print(num1 * num2)
