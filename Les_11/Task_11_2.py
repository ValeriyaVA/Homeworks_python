class Division:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def try_division(numerator, denominator):
        try:
            return numerator / denominator
        except ZeroDivisionError:
            return f'Делю на ноль, но не сегодня'
        except TypeError:
            return f'Я делю только числа!'


if __name__ == '__main__':
    div = Division.try_division(100, '5')
    print(div)
    print(Division.try_division(35, 7))
    print(Division.try_division(7, 0))


# class Division_err(Exception):
#     pass
#
#
# try:
#     val1, val2 = map(float, input("Введите два числа: ").split(' '))
#     if val2 == 0:
#         raise Division_err("Да не делю я на ноль!")
#     elif not isinstance(val2, (float, int)):
#         raise Division_err('Могу делить только числа!')
# except Division_err as e:
# else:
#     print(val1 / val2)
