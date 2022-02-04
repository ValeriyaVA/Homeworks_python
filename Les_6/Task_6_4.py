import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str):
    """
    Считывает данные из файлов и сохраняет объединенные данные в новый файл users_hobby.txt
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: файл users_hobby.txt
    """
    user_file = open('users.csv', 'r', encoding='utf-8')
    hobby_file = open('hobby.csv', 'r', encoding='utf-8')
    if sum(1 for line_u in open('users.csv', 'r', encoding='utf-8')) < sum(
            1 for line_h in open('hobby.csv', 'r', encoding='utf-8')):
        sys.exit([1])
    elif sum(1 for line_u in open('users.csv', 'r', encoding='utf-8')) >= sum(
            1 for line_h in open('hobby.csv', 'r', encoding='utf-8')):

        user_lines = user_file.readline()
        hobby_lines = hobby_file.readline()


return dict_user_hobby
