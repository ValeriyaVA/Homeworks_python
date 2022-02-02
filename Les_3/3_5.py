import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count, repeat=True, **kwargs) -> list:
    """
    Возвращает список шуток в количестве count
    параметр repeat определяет разрешение на повторы слов
    количество шуток без повторов не превышает количество слов в самом коротком списке
    """
    list_out = []
    if repeat == True:
        for i in range(count):
            list_out.append(' '.join(random.choice(kwargs[j]) for j in kwargs.keys()))
    elif repeat == False:
        for i in range(count):
            noun, adverb, adjective = [random.choice(kwargs[j]) for j in kwargs.keys()]
            list_out.append(' '.join([noun, adverb, adjective]))
            kwargs['nouns'].remove(noun)
            kwargs['adverbs'].remove(adverb)
            kwargs['adjectives'].remove(adjective)

    return list_out


print(get_jokes(4, False, nouns=nouns, adverbs=adverbs, adjectives=adjectives))