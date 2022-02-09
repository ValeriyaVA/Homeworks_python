import os


def make(path_dir: str, structure: str):
    '''
    Функция, которая идёт в заданной папке создаёт структуру папок из файла с необходимой структурой.
    Синтаксис структуры: в строке первая папка родительская. Через двоеточие её наследники.
    В следущих строкахв том же порядке, что и в материнской папке, по аналогии выписаны наследники дочерних папок
    Новая ветвь наследования отделена пустой строкой
    :param path_dir: путь, по которому создаём папки по струтуре из заданного файла
    :param dir_structure: файл, где хранится структура создаваемых каталогов
    '''
    dict_dirs = {}
    with open(structure, 'r', encoding='utf-8') as fr:
        list_keys = []
        for line in fr:
            if line == '':
                dict_dirs = {}
            key, value = line.split(': ')
            child_dirs = value.rstrip().split(' ')
            if key not in dict_dirs.keys():
                dict_dirs[key] = child_dirs
                list_keys.append(key)
            else:
                dict_dirs[key] += child_dirs
    print(dict_dirs)


make('D:/Homeworks_python/Les_7/', 'new_structure.txt')
