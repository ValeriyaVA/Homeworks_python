# решаю задачу, как если бы не знала положение значений времени и температуры со знаком +/- в строке или значения вводятся с клавиатуры и я их не знаю, иначе о чём задача?
lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(lst) - 1, -1,-1):
    if lst[i].isdigit() == True:
        if lst[i] == 0:  # если температура 0, то просто пропускаем ход
            continue
        if len(lst[i]) == 1:
            lst[i] = '0' + lst[i]
        lst.insert(i + 1, '"') # переделать через срезы!!!
        lst.insert(i, '"')
    elif lst[i].isdigit() == False:
        for j in range(len(lst[i])):
            if (lst[i][j].isdigit() == True) and (len(lst[i]) == 2):
                lst[i] = lst[i][0] + '0' + lst[i][j]
                lst.insert(i + 1, '"')
                lst.insert(i, '"')
            elif (lst[i][j].isdigit() == True) and (len(lst[i]) > 2):
                lst.insert(i + 1, '"')
                lst.insert(i, '"')
                break
print(lst)

i = 0
while i != len(lst): #нужно забубенить строку!!!
    if lst[i] != '"':
        print(lst[i], end=' ')
        i += 1
    elif lst[i] == '"' and i + 3 <= len(lst):
        print(lst[i] + lst[i + 1] + lst[i + 2], end=' ')
        i += 3
