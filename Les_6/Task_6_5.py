import sys

import Task_6_4

'''
Введите названия файлов через пробел строго в этом порядке: список пользователей, список хобби, куда объдинить данные. 
Файлы должны лежать в этой же папке
'''

if len(sys.argv) == 1:
    print("Где имена файлов?!")
    sys.exit()
elif len(sys.argv) > 4:
    print('Слишком много имён, до свиданья')
    sys.exit()
elif len(sys.argv) < 4:
    print('Нужно больше имён, попробуйте ещё раз')
    sys.exit()
Task_6_4.create_user_hobby(sys.argv[1], sys.argv[2], sys.argv[3])