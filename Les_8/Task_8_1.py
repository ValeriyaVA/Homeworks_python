import re


def email_parse(email: str) -> dict:
    """
    Функция при помощи регулярного выражения извлекает
    имя пользователя и почтовый домен из переданного адреса и возвращает их в виде словаря,
    в котором ключи - username и domain, а значения - соответствующие строки из распарсенной строки.
    Если адрес не валидный, отдаёт ошибку в виде:
        ValueError: wrong email: adress
    На разных доменах к имени разные требования, для определённости возьмём такие:
        состоит из трёх букв и более (по идее, ограничение сверху тоже возможно)
        может включать буквы любого регистра и цифры
        может включать нижнее подчеркивание, тире, точку, но не в начале и в конце
        нельзя использовать подряд два спецсимвола
    Что касательно доменов:
        домен и субдомены состоят из двух и более букв

    :param email: адрес, который передаём на проверку
    :return: Dict('username': str, 'domain': str)
    """
    dict_adress = {'username': None, 'domain': None}
    # RE_MAIL = re.compile(r'^[a-zA-Z0-9_.-]{3,}@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]{2,})+$')
    RE_MAIL = re.compile(r'^[^_.-][a-zA-Z0-9_.-]{3,}[^_.-]@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]{2,})+$')
    # RE_MAIL = re.compile(r'^[a-zA-Z0-9_.-]{3,}@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]{2,})+$')
    if not RE_MAIL.match(email):
        raise ValueError(f'wrong email: {email}')
    else:
        dict_adress['username'], dict_adress['domain'] = email.split('@')
    print(dict_adress)


# (?!([-._])\1+$)^[a-zA-Z0-9_.-]{3,}

if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    # email_parse('valeriia.vorobkalo@chemistry.msu.ru')
    # email_parse('someone@geekbrainsru')