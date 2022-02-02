# решаю задачу, как если бы не знала положение значений времени и температуры со знаком +/- в строке
my_list = ['в', '7', 'часов', '15', 'минут', 'температура', 'воздуха', 'была', '0', 'градусов']


def convert_list_in_str(list_in: list) -> str:
    for i in range(len(list_in) - 1, -1, -1):
        if list_in[i].isdigit() == True:
            if len(list_in[i]) == 1:
                list_in[i] = '0' + list_in[i]
            list_in[i + 1:i + 1] = '"'
            list_in[i:i] = '"'
        elif list_in[i].isdigit() == False:
            for j in range(len(list_in[i])):
                if (list_in[i][j].isdigit() == True) and (len(list_in[i]) == 2):
                    list_in[i] = list_in[i][0] + '0' + list_in[i][j]
                    list_in[i + 1:i + 1] = '"'
                    list_in[i:i] = '"'
                elif (list_in[i][j].isdigit() == True) and (len(list_in[i]) > 2):
                    list_in.insert(i + 1, '"')
                    list_in.insert(i, '"')
                    break
    i = 0
    str_out = ''
    while i != len(list_in):
        if list_in[i] != '"':
            str_out += list_in[i] + ' '
            i += 1
        elif list_in[i] == '"' and i + 3 <= len(list_in):
            str_out += list_in[i] + list_in[i + 1] + list_in[i + 2] + ' '
            i += 3
    return str_out


result = convert_list_in_str(my_list)
print(result)
