from functools import wraps

def type_logger(calc_cube):
   @wraps(calc_cube)
   def wrapper(*args):
      for i in range(len(args)):

         if i < len(args) - 1:
            print(f'{wrapper.__name__}({args[i]}: {type(args[i])}), ', end='')
         else:
            print(f'{args[i]}: {type(args[i])}')
      return calc_cube(args)
   return wrapper


@type_logger
def calc_cube(args):
   '''
   Очень нужная функция
   :param args: числа, которые возводим в куб
   :return: генераторов кубов
   '''
   for arg in args:
      if isinstance(arg, (int, float)):
         yield arg ** 3
      else:
         yield arg

gege = calc_cube(5.0, 4, 3.7, 'df')
print(calc_cube.__doc__)
# for i in range(4):
#    print(next(gege))
