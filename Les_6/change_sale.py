import sys

sales = open('bakery.csv', 'r+', encoding='utf-8')


def seek_move(seek: int):
    '''
    Функция переводит курсор в файле на заданный с клавиатуры номер строки и возвращает
    кортеж с заменяемой строкой и курсором
    :param seek: номер строки, на которую нужно перевести курсор
    :return: заменяемая строка и курсор на неё'''
    i = 2
    while i <= seek:
        sales.readline()
        i += 1
    return sales.readline()


def change_sale(number: int, new_sale: str):
    """
    Функция принимает номер строки и значение. По данному номеру вносит в строке изменение значения
    :param number: номер строки, в которой хотим внести изменение
    :param new_sale: значение, на которое хотим заменить
    """
    old_sale = seek_move(number)
    print(old_sale)
    replaced_content = ""
    sales.seek(sales.tell() - 22)
    i = sales.tell() // 22
    print(i)
    while i + 1 <= sum(1 for line in open('bakery.csv')):
        line = sales.readline()
        new_line = line.replace(old_sale, new_sale.ljust(20)+'\n')
        replaced_content = replaced_content + new_line
        i += 1
    print(replaced_content)
    # sales.write(replaced_content)

change_sale(8, '123456')
# вообще тут надо ловить ошибку ValueError: could not convert string to float или int, но этого не было в лекциях
# if int(sys.argv[1]) and (float(sys.argv[2].replace(',', '.')) or int(sys.argv[2])):
#     change_sale(int(sys.argv[1]), sys.argv[2])
