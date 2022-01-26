def thesaurus(lst_in):
    dict_out = {}
    lst_uniq = set(lst_in)
    for i in lst_uniq:
        if i[0] in dict_out.keys():
            dict_out[i[0]] += [i]
        else:
            dict_out[i[0]] = [i]
    sorted_dict = sorted(dict_out.items())
    return dict(sorted_dict)


def thesaurus_adv(*args):
    surnames = {}
    for i in args:
        Surname = i[i.rfind(' '):]
        if Surname[1] in surnames.keys():
            surnames[Surname[1]] += [i]
        else:
            surnames[Surname[1]] = [i]
    for i in surnames.keys():
        lst_sur = surnames[i]
        surnames[i] = thesaurus(lst_sur)
    sorted_dict = sorted(surnames.items())
    return dict(sorted_dict)

result = thesaurus_adv("Иван Сергеев", 'Илья Иванов', 'Илья Инг', "Инна Серова", "Петр Алексеев", "Илья Иванов",
                       "Анна Савельева", "Елизавета Баранова", "Фёдор Бугаёв", "Андрей Иволгин", "Нина Петрова",
                       "Денис Ревин")
print(result)
