# Вывести на экран цены из спискка через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
from random import uniform

def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    str_out = ''
    for i in range(len(list_in)):
        if i != len(list_in) - 1:
            rub = int(list_in[i])
            kop = str(list_in[i])[str(list_in[i]).index('.')+1:]
            if len(kop) < 2:
                kop = '0' + kop
            str_out += ('%d руб %s коп, ' % (rub, kop))
        elif i == len(list_in) - 1:
            rub = int(list_in[i] * 100 // 100)
            kop = list_in[i] * 100 % 100
            str_out += ('%s руб %d коп' % (rub, kop))
    return str_out

def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()

def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    sort_prices(list_in)
    list_in.reverse()

def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_out = []
    sort_price_adv(list_in)
    for i in range(5):
        list_out.append(list_in[i])
    return list_out

my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)
id_my_list = id(my_list)
sort_prices(my_list)
print(my_list)
id_sorted_my_list= id(my_list) # зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
sort_price_adv(my_list)
print(id_sorted_my_list == id_my_list)
print(my_list)
result_4 = check_five_max_elements(my_list)
print(result_4)