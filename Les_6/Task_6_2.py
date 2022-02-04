def get_dict_adr(file_name: str) -> dict:
    """
    Считывает из файла построчно данные и записывает в словарь, где:
        ключ - адрес, значение - количество запросов
    :param file_name: передаём название файла логов
    :return: Dict(adress: number of requests)
    """

    dict_adr = {}
    with open(file_name, 'r', encoding='utf-8') as fr:
        for line in fr:
            key = line[:line.find(' - - ')]
            dict_adr[key] = dict_adr.get(key, 0) + 1
    return dict_adr


def find_spam(dict_adress: dict) -> str:
    """Находит адрес с максимальным количеством запросов из словаря"""
    return max(dict_adress, key=dict_adress.get)


spam_adress = find_spam(get_dict_adr('nginx_logs.txt'))
print(spam_adress)
