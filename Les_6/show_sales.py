import sys

sales = open('bakery.csv', 'r', encoding='utf-8')


def seek_move(seek: int):
    '''
    Функция переводит курсор в файле на заданный с клавиатуры номер строки
    :param seek: номер строки, на которую нужно перевести курсор
    '''
    i = 2
    while i <= seek:
        sales.readline()
        i += 1


def print_sales(list_in):
    if len(list_in) == 1:
        for line in sales:
            print(line, end='')
    elif len(list_in) <= 2 and int(list_in[1]) <= sum(1 for line in open('bakery.csv', 'r', encoding='utf-8')):
        seek_move(int(list_in[1]))
        for line in sales:
            print(line, end='')
    elif len(list_in) == 3 and int(list_in[1]) and int(list_in[2]) <= sum(
            1 for line in open('bakery.csv', 'r', encoding='utf-8')):
        seek_move(int(list_in[1]))
        j = (sales.tell() + 1) // 21
        while j < int(list_in[2]):
            print(sales.readline(), end='')
            j += 1
    elif int(sys.argv[2]) >= int(list_in[1]):
        print('Невозможно осуществить вывод в таком диапазоне строк')
    else:
        print('Введённые числа не соответствуют количеству строк в файле')


print_sales(sys.argv)
sales.close()
