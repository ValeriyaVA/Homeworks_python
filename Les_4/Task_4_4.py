import utils
import datetime #что-то непонятное с этим

kurs, date_value = utils.currency_rates_adv("CAD")

empty = bool(not kurs and not date_value)
if not empty and not isinstance(kurs, float):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance(date_value, datetime.date):
    raise TypeError("Неверный тип данных у даты")

print(kurs, date_value)
'''
потыкала разные варианты:

PS D:\Homeworks_python\Les_4> python Task_4_4.py
60.9615 2022-01-29

PS D:\Homeworks_python\Les_4> python Task_4_4.py usd
60.9615 2022-01-29


2) в консоли python??? синтаксическая ошибка?? (╮°-°)╮┳━━┳ ( ╯°□°)╯ ┻━━┻

'''