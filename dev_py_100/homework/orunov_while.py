
''' Страница 8 '''



'''
1. Каждый день я пробегаю «следующую степень двойки» км. Сколько дней пройдет, пока я в сумме пробегу 1000 км? 10000
 км?
'''
def wil_l():
    day = 0
    a = 1000

    while a >= 0:
        sum_day = 2*day
        a -= sum_day
        day += 1

    out = (f"Day {day}, todau run {sum_day}, left to run {a} ")


    return out

print(wil_l())


'''
2. Каждый день я пробегаю «следующее простое число» км. Сколько дней пройдет, пока я в сумме пробегу 1000 км? 10000 км?
'''


def next(n):
    lst = []
    k = 0
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            lst.append(i)
        else:
            k = 0

def wil_l():

    day = 0
    a = 1000
    nex = next(a)
    while a >= 0:
        day_run = nex[day]
        a -= day_run
        day += 1

    out = (f"Day {day}, left to run {a} ")


    return out

print(wil_l())

'''
3. Начав тренировки, спортсмен в первый день пробежал 10 км. Для увеличения выносливости ему необходимо повышать 
норму бега через одну тренировку на 15% от нормы предыдущей тренировки. Спортсмен трени­руется каждый день. 
Какой суммарный путь он пробежит за 30 дней.

'''

def beg():
    day = 1

    while day < 30:
        norm = 10
        day_tren_plus = norm + norm * 0.15
        if day % 2 == 0:
            norm = day_tren_plus
        way = day * norm
        day += 1
        ex = (f"Day {day}, way {way}")
    return  ex
print(beg())
