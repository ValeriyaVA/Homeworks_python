def get_uniq_numbers(src: list):
    dict_nums = {}
    for x in src:
        dict_nums[x] = dict_nums.get(x, 0) + 1  # считаем в значениях количество повторов числа по по ключу числа
    new_list = [x for x in src if dict_nums[x] == 1] # формируем список из ключей, в которых значение == 1

    return new_list


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
