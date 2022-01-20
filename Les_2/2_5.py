# Вывести на экран цены из спискка через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
import random

prices = []
for i in range(20):
    price = str(format(random.uniform(0, 20), ".2f"))
    prices.append(price)
print(prices)

