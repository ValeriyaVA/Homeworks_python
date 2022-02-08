import os

TEMPLATE = '    '
def make(path_dir: str, structure: str):

    with open(structure, 'r', encoding='utf-8') as fr:
        j = 0
        while j <= sum(1 for line in structure):
            parent_name = fr.readline().replace('\n', '')
            print(parent_name)
            if not parent_name.startswith(TEMPLATE):  # обрабатываем корневые папки
                os.mkdir(os.path.join(path_dir, parent_name))
                os.chdir(os.path.join(path_dir, parent_name))
                first_dir = (os.getcwd())
                j += 1
            else:
                i = 1
                while True:
                    print(os.getcwd(), i)
                    j += 1
                    if parent_name.startswith(TEMPLATE * i):
                        child_dir_name = parent_name.strip()
                        os.mkdir(os.path.join(child_dir_name))
                        os.chdir(os.path.join(child_dir_name))
                        i += 1
                    else:
                        os.chdir(os.path.join(path_dir, first_dir))
                        break


make('D:/Homeworks_python/Les_7/', 'structure_dirs.txt')
