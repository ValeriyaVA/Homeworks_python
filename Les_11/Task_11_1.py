import time
import re


class Date:

    def __init__(self, date_str: str):
        assert re.match(r'^(\d{2}-){2}\d{4}$', date_str), f'Неправильный формат даты'
        self.date_str = date_str

    @classmethod
    def extract_number(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        return day, month, year

    @staticmethod
    def validate_date(date_str):
        try:
            time.strptime(date_str, '%d-%m-%Y')
        except ValueError:
            print(f'{date_str} is invalid')
        else:
            print(f'{date_str} is valid')


date = Date('12-12-2022')
date.validate_date(date.date_str)
print(date.extract_number(date.date_str))
fake_date = Date('29-02-2022')
fake_date.validate_date(fake_date.date_str)
print(fake_date.extract_number(fake_date.date_str))
print(Date.extract_number('23-02-2021'))
Date.validate_date('28-02-2022')
