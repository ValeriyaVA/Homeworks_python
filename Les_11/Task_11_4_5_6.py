class EquipmentWarehouse:
    num = 0
    dict_equipment = {'Сканеры': [], 'Принтеры': [], 'Ксероксы': []}

    @classmethod
    def count(cls):
        cls.num += 1

    def full_inventory(self):
        if isinstance(self, Scanner):
            EquipmentWarehouse.dict_equipment['Сканеры'].append(
                (self.name, self.price, self.number_lists, self.number_equip, self.work))
        elif isinstance(self, Printer):
            EquipmentWarehouse.dict_equipment['Принтеры'].append((self.name, self.price, self.number_lists,
                                                                  self.number_equip, self.work,))
        elif isinstance(self, Xerox):
            EquipmentWarehouse.dict_equipment['Ксероксы'].append((self.name, self.price, self.number_lists,
                                                                  self.number_equip, self.work))

    def __init__(self, name, price, number_lists, number_equip, work=True):
        """
        Конструктор базового класса определяет общие для всех подклассов параметры:
        :param name: название модели оборудования
        :param price: цена оборудования
        :param number_lists: количество листов в оборудовании
        :param work: работает/не работает, по дефолту работает
        :param number_equip: количество данного оборудования на складе
        """
        self.name = name
        self.price = price
        self.number_lists = number_lists
        self.number_equip = number_equip
        self.work = work
        self.count()
        self.full_inventory()

    @staticmethod
    def store_info():
        return f'Сканеров {Scanner.num}, принтеров {Printer.num}, ксероксов {Xerox.num}'


class Printer(EquipmentWarehouse):
    num = 0

    def __init__(self, name, price, number_lists, number_equip, type_print, work=True, two_side_print=False):
        """
        Конструктор принтера имеет те же параметры, что и базовый класс,
        кроме того, имеет характеристики:
        :param two_side_print: флаг, определяющий наличие двухсторонней печати, по дефолту её нет
        :param type_print: строка с типом принтера по способу печати: матричный/струйный/лазерный
        """
        super().__init__(name, price, number_lists, number_equip, work)
        self.type_print = type_print
        self.two_side_print = two_side_print


class Scanner(EquipmentWarehouse):
    num = 0

    def __init__(self, name, price, number_lists, number_equip, resolution, work=True, usb_save=False):
        """
        Конструктор сканера имеет те же параметры, что и базовый класс,
        кроме того, имеет характеристики:
        :param resolution: разрешающая способность сканера, например, строка формата '1200*1200 dpi'
        :param usb_save: возможность сохранять сразу на usb-носитель, по дефолту нет
        """
        super().__init__(name, price, number_lists, number_equip, work)
        self.resolution = resolution
        self.usb_save = usb_save


class Xerox(EquipmentWarehouse):
    num = 0

    def __init__(self, name, price, number_lists, number_equip, color, work=True, ):
        """
        Конструктор ксерокса имеет те же характеристики, что и базовый класс,
        кроме того, имеет характеристику:
        :param color: возможность цветной копии, по дефолту нет
        """
        super().__init__(name, price, number_lists, number_equip, work)
        self.color = color


x1 = Printer('name_x1', 10000, 100, 10, 'matrix')
x2 = Printer('name_x2', 15000, 1000, 10, 'jet')
y1 = Scanner('name_y1', 20000, 200, 10, '1200*1200')
y2 = Scanner('name_y2', 2300, 100, 5, '300*600')
y3 = Scanner('name_y3', 1000, 200, 5, 'unknown', work=False)
z1 = Xerox('name_z1', 40000, 200, 10, color=True)
print(EquipmentWarehouse.store_info())
print(EquipmentWarehouse.dict_equipment)
