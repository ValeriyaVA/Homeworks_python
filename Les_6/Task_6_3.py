import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    dict_user_hobby = {}
    with open('users.csv', 'r', encoding='utf-8') as fr:
        user_lines = fr.read().split('\n')
        dict_user_hobby = dict.fromkeys(user_lines)
    with open('hobby.csv', 'r', encoding='utf-8') as frr:
        hobby_lines = frr.read().split('\n')
        if len(hobby_lines) > len(user_lines):
            sys.exit([1])
        elif len(hobby_lines) <= len(user_lines):
            for i in range(len(hobby_lines)):
                dict_user_hobby[user_lines[i]] = hobby_lines[i].split(',')
    return dict_user_hobby


dict_out = prepare_dataset('users.csv', 'hobby.csv')

with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
