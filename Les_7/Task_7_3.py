import os
import shutil


def create_templates(start_path: str):
    '''
    Функция находит в папке my_project все папки с именем templates и копирует их в отдельную папку в my_project
    :param start_path: передаём путь, где ищем папку my_project
    '''
    os.chdir(start_path)
    paths_templates = [] # сюда закинем пути, где нашлись templates
    for root, dirs, files in os.walk(start_path):
        if 'templates' in dirs:
            paths_templates.append(os.path.join(root, 'templates'))
    os.mkdir('templates')
    for path in paths_templates:
        shutil.copytree(path, 'templates', dirs_exist_ok=True)


create_templates(os.path.join(os.getcwd(), 'my_project'))
