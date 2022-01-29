import requests
from datetime import datetime


def currency_rates_adv(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    date = content[content.find('Date=')+6:content.find('" name=')]
    result_date = datetime.strptime(date, "%d.%m.%Y")

    if code.upper() not in content:
        result_value = None
    else:
        nominal_value = content[content.find(code.upper()):].split('<Nominal>')[1].split('</Nominal>')[0]
        value = content[content.find(code.upper()):].split('<Value>')[1].split('</Value>')[0]
        result_value = float(value.replace(',', '.')) / int(nominal_value)
    return (result_value, result_date)


kurs, date_value = currency_rates_adv("USD")
print(type(date_value))
# empty = bool(not kurs and not date_value)
# if not empty and not isinstance(kurs, float):
#     raise TypeError("Неверный тип данных у курса")
# if not empty and not isinstance(date_value, type(datetime.date)):
#     raise TypeError("Неверный тип данных у даты")
print(kurs, date_value)