# a) Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
odd_cube = []
for i in range(1, 1000):
    if i % 2 != 0:
        odd_cube.append(i ** 3)  # собрала список из кубов нечётных чисел
print(odd_cube)


def sum_div_seven(dataset):
    sum = 0
    for number in dataset:
        sum_digit = 0  # переменная для хранения суммы разрядов каждого элемента списка
        while number > 0:
            digit = number % 10
            sum_digit += digit
            number = number // 10
        if sum_digit % 7 == 0:
            sum += sum_digit
    return sum


def new_sum_div_seven(dataset):
    for i in range(len(dataset)):
        dataset[i] += 17
    print(dataset)
    return sum_div_seven(dataset)

result_1 = sum_div_seven(odd_cube)
print(result_1)
result_2 = new_sum_div_seven(odd_cube)
print(result_2)

