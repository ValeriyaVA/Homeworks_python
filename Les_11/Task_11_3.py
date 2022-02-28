class AppList:
    def __init__(self):
        self.my_list = []

    def __str__(self):
        return str(self.my_list)

    def append_value(self):
        check = 'y'
        while True:
            if check == 'n':
                print('Ну и пожалуйста, ну и не нужно!')
                break
            elif check not in ('y', 'n'):
                check = input('Вы ткнули не ту букву. Попробуете ещё раз? y/n ')
            elif check == 'y':
                try:
                    value = input('Введите значение, может быть добавлю в список ')
                    if isinstance(float(value), float) or isinstance(int(value), int):
                        self.my_list.append(value)
                except ValueError:
                    print(f'Такое не добавлю')
                check = input('Добавите ещё значение? y/n ')


if __name__ == '__main__':
    lst_nums = AppList()
    lst_nums.append_value()
    print(lst_nums)
