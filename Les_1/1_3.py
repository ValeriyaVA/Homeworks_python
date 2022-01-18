def transform_string(n):
    if 10 <= n <= 20:
        return str(n) + ' процентов'
    elif n % 10 == 1:
        return str(n) + ' процент'
    elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
        return str(n) + ' процента'
    else:
        return str(n) + ' процентов'

for i in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(i))