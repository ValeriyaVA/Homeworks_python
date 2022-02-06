import sys

with open('bakery.csv', 'a+', encoding='utf-8') as fa:
    if float(sys.argv[1].replace(',', '.')) or int(sys.argv[1]):
        # записываем в файл число и дополняем пробелами до длины строки в 15 символов
        fa.write(f'{sys.argv[1].ljust(20)}\n')
# вообще тут надо ловить ошибку ValueError: could not convert string to float или int, но этого не было в лекциях