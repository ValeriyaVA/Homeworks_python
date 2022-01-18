# вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах
def convert_time(sec):
    if sec >= 86400:
        days = sec // 86400
        hours = (sec % 86400) // 3600
        mins = ((sec % 86400)) % 3600 // 60
        secs = (((sec % 86400)) % 3600) % 60
        answer = str(days) + ' дн ' + str(hours) + ' час ' + str(mins) + ' мин ' + str(secs) + ' сек '
    elif 3600 <= sec < 86400:
        hours = sec // 3600
        mins = sec % 3600 // 60
        secs = sec % 3600 % 60
        answer = str(hours) + ' час ' + str(mins) + ' мин ' + str(secs) + ' сек '
    elif 60 <= sec < 3600:
        mins = sec // 60
        secs = sec % 60
        answer = str(mins) + ' мин ' + str(secs) + ' сек '
    elif 0 <= sec < 60:
        answer = str(sec) + ' сек '
    else:
        answer = 'неверный формат ввода'
    return answer

duration = int(input('Convert seconds to days, hours and minutes: '))
result = convert_time(duration)
print(result)
