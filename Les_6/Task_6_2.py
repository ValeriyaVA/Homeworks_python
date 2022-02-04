def get_parse_spam(line: str) -> dict:
    """Составляет словарь, в котором ключ - адрес, а значение - количество запросов с этого адреса"""
    dict_adr = {}
    key = line[:line.find(' - - ')]
    dict_adr[key] = dict_adr.get(key, 0) + 1
    return dict_adr


def find_spam(dict_adress: dict) -> str:
    """Находит адрес с максимальным количеством запросов из словаря"""
    max(dict_adr, key=dict_adr.get)


with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:

spam_adress
find_spam()
print(spam_adress)
