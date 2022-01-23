def thesaurus(*args):
    names = {}
    print(args, 'the', '\n')
    for i in args:
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
            surnames[Surname[0]] += {i}
        else:
            surnames[Surname[0]] = [i]
    for i in surnames.keys():
        lst = thesaurus(surnames[i])
        print(lst, 'adv')
    return surnames

result = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(result)
