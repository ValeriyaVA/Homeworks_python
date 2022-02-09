import os

TEMPLATE = '....'
with open(structure, 'r', encoding='utf-8') as fr:
    parent_name = fr.readline().replace('\n', '')
    while parent_name:
        print(parent_name)
        if not parent_name.startswith(TEMPLATE):  # обрабатываем корневые папки
            os.mkdir(os.path.join(path_dir, parent_name))
            os.chdir(os.path.join(path_dir, parent_name))
            first_dir = (os.getcwd())
            parent_name = fr.readline()
        else:
            i = 1
            while True:
                print(os.getcwd(), 'куда пишем', i)
                if parent_name.startswith(TEMPLATE*i):
                    parent_path = parent_name.strip(TEMPLATE * i)
                    os.mkdir(parent_path)
                    print(os.getcwd())
                    parent_name = fr.readline().replace('\n', '')
                    print(parent_name)
                    if parent_name.startswith(TEMPLATE*(i+1)):
                        i += 1
                        os.chdir(parent_path)
                    else:




make('D:/Homeworks_python/Les_7/', 'structure_dirs.txt')