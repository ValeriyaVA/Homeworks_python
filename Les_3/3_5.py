import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = []
    # lst.append(nouns)
    # lst.append(adverbs)
    # lst.append(adjectives)
    for i in range(count):
        i = random.choices(nouns)
        j = random.choices(adverbs)
        k = random.choices(adjectives)
        list_out.append(list(i, j, k))
    return list_out


print(get_jokes(3))

