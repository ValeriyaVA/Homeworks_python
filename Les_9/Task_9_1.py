import time


def red_light(text):
    print("\033[31m{}".format(text))


def yellow_light(text):
    print("\033[33m{}".format(text))


def green_light(text):
    print("\033[32m{}".format(text))


class TrafficLight:
    __color = {'red': 4, 'yellow': 2, 'green': 3}

    # def running(self):
    #
    #     mode = [red_light, yellow_light, green_light]
    #     if list(self.__color.keys()) != list(TrafficLight.__color.keys()):
    #         raise ValueError('ИИИууууИИИИууууу ОБНАРУЖЕН НАРУШИТЕЛЬ РЕЖИМОВ')
    #     i = 0
    #     for key in self.__color.keys():
    #         mode[i](f'{key} {self.__color[key]} сек')
    #         i += 1
    #         time.sleep(self.__color[key])

    def running(self):

        if list(self.__color.keys()) != list(TrafficLight.__color.keys()):
            raise ValueError('ИИИууууИИИИууууу ОБНАРУЖЕН НАРУШИТЕЛЬ РЕЖИМОВ')
        for key in self.__color.keys():
            print(f'{key} {self.__color[key]} сек')
            time.sleep(self.__color[key])


if __name__ == '__main__':
    traffic = TrafficLight()
    # traffic._TrafficLight__color = {'green': 2, 'yellow': 3, 'red': 4}
    traffic.running()
