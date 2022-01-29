import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    if code.upper() not in content:
        result_value = None
    else:
        nominal_value = content[content.find(code.upper()):].split('<Nominal>')[1].split('</Nominal>')[0]
        value = content[content.find(code.upper()):].split('<Value>')[1].split('</Value>')[0]
        result_value = float(value.replace(',', '.')) / int(nominal_value)
    return result_value


print(currency_rates("usd"))
print(currency_rates("noname"))