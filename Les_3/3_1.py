def num_translate_adv(num):
    num_dictionary = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                      'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    num_dictionary_title = {'Zero': 'Ноль', 'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре',
                            'Five': 'Пять',
                            'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Десять'}
    if num.lower() in num_dictionary.keys():
        if num.istitle():
            return num_dictionary_title[num]
        else:
            return num_dictionary[num]
    return None


translate = num_translate_adv('Two')
print(translate)
