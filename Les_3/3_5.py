import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = []
    for l in range(count):
        i = random.choice(nouns)
        j = random.choice(adverbs)
        k = random.choice(adjectives)
        list_out.append(' '.join([i,j,k]))
    return list_out


print(get_jokes(3))
