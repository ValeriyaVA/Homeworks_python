import os


def make(path_dir: str, structure: str):
    '''
    Функция, которая идёт в заданной папке создаёт структуру папок из файла с необходимой структурой.
    Синтаксис структуры: папки одного уровня находятся на одинаковом отступе от начала строки,
    дочерние папки отделены от родительской 4 дополнительными пробелами
    :param path_dir: путь, по которому создаём папки по струтуре из заданного файла
    :param dir_structure: файл, где хранится структура создаваемых каталогов
    '''
    with open(structure, 'r', encoding='utf-8') as fr:
        for line in fr:
            # print(parent_dir)
            if not line.startswith('    '):
                parent_dir = line.replace('\n', '')
                # print(os.path.join(path_dir, parent_dir))
                os.mkdir(os.path.join(path_dir, parent_dir))
            else:
                # print(os.path.join(path_dir, parent_dir, line.strip()))
                os.mkdir(os.path.join(path_dir, parent_dir, line.strip()))


make('D:/Homeworks_python/Les_7/', 'structure_dirs.txt')
