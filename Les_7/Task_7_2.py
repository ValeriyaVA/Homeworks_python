import os


def make(path_dir: str, structure: str):
    with open(structure, 'r', encoding='utf-8') as fr:
        for line in fr:
            parent_name, daughter_str = line.split(': ')
            daughter_names = daughter_str.rstrip().split(' ')
            if not os.path.exists(os.path.join(path_dir, parent_name)):
                os.mkdir(os.path.join(path_dir, parent_name))
                for sub_dir in daughter_names:
                    os.mkdir(os.path.join(path_dir, parent_name, sub_dir))
            else:
                for sub_dir in daughter_names:
                    os.mkdir(os.path.join(path_dir, parent_name, sub_dir))

make('D:/Homeworks_python/Les_7/', 'new_structure')
