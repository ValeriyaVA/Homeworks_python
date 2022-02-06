import sys

sales = open('bakery.csv', 'r+', encoding='utf-8')


def seek_move(seek: int):
    '''
    Функция переводит курсор в файле на заданный с клавиатуры номер строки
    возвращает заменяемую строку и положение курсора
    :param seek: номер строки, на которую нужно перевести курсор
    :return: заменяемая строка, положение курсора
    '''
    i = 2
    while i <= seek:
        sales.readline()
        i += 1
    start_change = sales.tell()
    return sales.readline(), start_change


def change_sale(number: int, new_sale: str):
    """
    Функция принимает номер строки и значение. По данному номеру вносит в строке изменение значения
    :param number: номер строки, в которой хотим внести изменение
    :param new_sale: значение, на которое хотим заменить
    """
    if number > sum(1 for line in open('bakery.csv')):
        sys.exit(['Количество строк меньше заданного числа, изменение невозможно'])
    old_sale, start = seek_move(number)
    sales.seek(start)
    line = sales.readline()
    replaced_content = line.replace(old_sale, new_sale.ljust(20) + '\n')
    sales.seek(start)
    sales.write(replaced_content[:len(replaced_content) - 1])


if int(sys.argv[1]) and (float(sys.argv[2].replace(',', '.')) or int(sys.argv[2])):
    change_sale(int(sys.argv[1]), sys.argv[2])
sales.close()
