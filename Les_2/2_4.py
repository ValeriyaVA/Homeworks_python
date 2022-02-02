# элементы списка - строки из нескольких слов, где последнее имя, которое отделено пробелом. Вывести список из приветствий для каждого имени

def convert_name_extract(list_in: list) -> list:
    list_out = []
    for word in list_in:
        list_out.append('Привет,' + word[word.rfind(' '):].title()+'!')
    return list_out

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)