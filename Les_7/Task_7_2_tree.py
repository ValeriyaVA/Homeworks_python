import os

TEMPLATE = '    '
def make(path_dir: str, structure: str):
    '''
    Функция, которая идёт в заданной папке создаёт структуру папок из файла config.yaml
    Структура: корневые папки записаны без знаков-разделителей в начале.
    Папки одного уровня находятся соответственно на кратном расстоянии по разделителю TEMPLATE = '    '.
    В структуре может присутствовать два типа файлов: *.py и *.html
    :param path_dir: путь, куда создать дерево папок с файлами из config.yaml
    :param structure: путь до файла со структурой
    '''
    with open(structure, 'r', encoding='utf-8') as fr:
        parent_name = fr.readline().replace('\n', '')
        while parent_name:
            print(parent_name)
            if not parent_name.startswith(TEMPLATE):  # обрабатываем корневые папки
                os.mkdir(os.path.join(path_dir, parent_name))
                os.chdir(os.path.join(path_dir, parent_name))
                first_dir = (os.getcwd())
                parent_name = fr.readline().replace('\n', '')
            else:
                i = 1
                while True:
                    print(os.getcwd(), 'куда пишем', i)
                    if parent_name.startswith(TEMPLATE * i) and not os.path.exists(parent_name.strip(TEMPLATE * i)):
                        child_dir_name = parent_name.strip(TEMPLATE * i)
                        os.mkdir(os.path.join(child_dir_name))
                        print(os.getcwd())
                        parent_name = fr.readline().replace('\n', '')
                        print(parent_name)
                        if parent_name.startswith(TEMPLATE * (i+1)):
                            i += 1
                            os.chdir(os.path.join(child_dir_name))
                    elif os.path.exists(os.path.join(path_dir, first_dir, parent_name.strip(TEMPLATE))):
                        parent_name = fr.readline()
                        break
                    elif parent_name.startswith(TEMPLATE) and not parent_name.startswith(TEMPLATE*2):
                        print(parent_name, 'откат')
                        os.mkdir(os.path.join(path_dir, first_dir, parent_name.strip(TEMPLATE)))
                        os.chdir(os.path.join(path_dir, first_dir, parent_name.strip(TEMPLATE)))
                        break


make('D:/Homeworks_python/Les_7/', 'structure_dirs.txt')
