def get_dict_adr(file_name: str) -> dict:
    '''Создаёт словарь: ключи - адреса, значения - количество запросов
    В функцию передаём названия файла логов
    '''

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
