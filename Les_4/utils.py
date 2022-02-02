import requests
import datetime


def currency_rates_adv(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    content = requests.api.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    date = content[content.find('Date=') + 6:content.find('" name=')]
    result_date = datetime.datetime.strptime(date, "%d.%m.%Y").date()

    if code.upper() not in content:
        result_value = None
    else:
        nominal_value = content[content.find(code.upper()):].split('<Nominal>')[1].split('</Nominal>')[0]
        value = content[content.find(code.upper()):].split('<Value>')[1].split('</Value>')[0]
        result_value = float(value.replace(',', '.')) / int(nominal_value)
    return (result_value, result_date)
