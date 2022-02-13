import re


def parse_list(str_info: str) -> tuple:
    """
    Функция получает построчно считываемые файла данные nginx_logs.txt, парсит из неё данные об
    адресе, дате запрроса, типе запроса, ресурсе, коде и размере
    :param str_info: считанная из файла строка
    :return: tuple(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)
    """
    request_data = re.compile(r'(?P<addr>(?:\d{1,3}\.){3}\d{1,3})\s-\s-\s\['
                              r'(?P<date>\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}\s+[+]\d{4})\]\s"'
                              r'(?P<request_type>\w+)\s(?P<requested_resource>/\w+/\w+_\d{1})\sHTTP/1.1" '
                              r'(?P<response_code>\d{3})\s(?P<response_size>\d+)\s"-"')
    return request_data.findall(str_info)


with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        print(*parse_list(line))
