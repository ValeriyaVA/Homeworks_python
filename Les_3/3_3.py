# def thesaurus(*args):
#     names = {}
#     for i in args:
#         if i[0] in names.keys():
#             names[i[0]] += [i]
#         else:
#             names[i[0]] = [i]
#     return names


def thesaurus_adv(*args):
    surnames = {}
    names = {}
    for i in args:
        Name, Surname = (str(j) for j in i.split())
        if Surname[0] in surnames.keys():
            surnames[Surname[0]] += [i]
        else:
            surnames[Surname[0]] = [i]
    return surnames

result = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(result)
