# элементы списка - строки из нескольких слов, где последнее имя. Вывести "Привет, {имя}!" для всего списка имён

def convert_name_extract(list_in: list) -> list:
    for word in employees_list:
    list_out = []
    list_out.append('Привет,' + word[word.rfind(' '):].title()+'!')

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)