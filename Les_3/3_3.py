def thesaurus(lst_in):
    names = {}
    for i in lst_in:
        if i[0] in names.keys():
            names[i[0]] += [i]
        else:
            names[i[0]] = [i]
    return names


def thesaurus_adv(*args):
    surnames = {}
    for i in args:
        Name, Surname = (str(j) for j in i.split())
        if Surname[0] in surnames.keys():
            surnames[Surname[0]] += [i]
        else:
            surnames[Surname[0]] = [i]
    for i in surnames.keys():
        lst_sur = surnames[i]
        surnames[i] = thesaurus(lst_sur)
    return surnames

result = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Елизавета Баранова", "Фёдор Бугаёв", "Андрей Иволгин", "Нина Петрова","Денис Ревин")
print(result)