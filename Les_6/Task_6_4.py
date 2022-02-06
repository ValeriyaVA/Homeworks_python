import sys


def create_user_hobby(path_users_file: str, path_hobby_file: str, result_file: str):
    """
    Считывает данные из файлов и сохраняет объединенные данные в новый файл users_hobby.txt
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :param result_file: название выходного файла txt со списком в формате: фИО: хобби
    """
    user_file = open(path_users_file, 'r', encoding='utf-8')
    hobby_file = open(path_hobby_file, 'r', encoding='utf-8')
    users_hobby = open(result_file, 'w', encoding='utf-8')
    if sum(1 for line_u in open(path_users_file, 'r', encoding='utf-8')) < sum(
            1 for line_h in open(path_hobby_file, 'r', encoding='utf-8')):
        sys.exit([1])
    elif sum(1 for line_u in open(path_users_file, 'r', encoding='utf-8')) >= sum(
            1 for line_h in open(path_hobby_file, 'r', encoding='utf-8')):
        for line in hobby_file:
            print("{}: {}".format(user_file.readline().rstrip(), line), file=users_hobby, end='')
        print(file=users_hobby)
        for line in user_file:
            print("{}: {}".format(line.rstrip(), None), file=users_hobby, end='\n')
    user_file.close()
    hobby_file.close()
    users_hobby.close()


create_user_hobby('users.csv', 'hobby.csv', 'users_hobby.txt')
