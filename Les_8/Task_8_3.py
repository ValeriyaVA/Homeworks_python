from functools import wraps

def type_logger(calc_cube):
   @wraps(calc_cube)
   def wrapper(*args):
      for i in range(len(args)):
         if  i < len(args) - 1:
            print(f'{wrapper.__name__}({args[i]}: {type(args[i])}), ', end='')
         elif i == len(args) - 1:
            print(f'{wrapper.__name__}({args[i]}: {type(args[i])})')
      # for i in range(len(args)): # если раскомментировать, посчитает кубы
      #    calc_cube(args[i])
   return wrapper


@type_logger
def calc_cube(x):
   '''
   Очень нужная функция
   :param args: числа, которые возводим в куб
   :return: печатает куб числа
   '''
   print(x**3)


calc_cube(5.0, 4, 3.7)
# print(calc_cube.__doc__)

