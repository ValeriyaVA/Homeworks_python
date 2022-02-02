''' Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке'''
from random import randint


# src = [randint(0, 50000) for i in range(100000)]   # генератор случайных целых чисел для проверки работы программы

def get_uniq_numbers(src: list):
    unique_num = set()
    tmp = set()
    for num in src:
        if num not in tmp:
            unique_num.add(num)
        else:
            unique_num.discard(num)
        tmp.add(num)

    # сохранение последовательности элементов
    unique_num_ord = [el for el in src if el in unique_num]
    return unique_num_ord


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
