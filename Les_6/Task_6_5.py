import sys

import Task_6_4

'''
Введите названия файлов через пробел: список пользователей, список хобби, куда объдинить данные. 
Файлы должны лежать в этой же папке
'''

if len(sys.argv) == 1:
    print("Где имена файлов?!")
    sys.exit(1)
elif len(sys.argv) > 4:
    print('Слишком много имён, до свиданья')
    sys.exit(2)
elif len(sys.argv) < 4:
    print('Нужно больше имён')

Task_6_4.create_user_hobby(sys.argv[1], sys.argv[2], sys.argv[3])
# print(sys.argv)