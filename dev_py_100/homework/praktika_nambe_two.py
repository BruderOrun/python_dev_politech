# a = int(input(int))
# s = input(str)
#
# print(s * a)



def stairs(g):

    n = ''
    for i in range(g):
        n += '=' * i + '\n'
    return n
print(stairs(6))


def revers_stairs(g, s = '='):
    n = ''
    for i in range(g):
        n += ' ' * (g-i) + (s * i) + '\n'
    return n
print(revers_stairs(7))





wor = 0
def amount_repetitions_letters():
    f = 'dfeeggrfsfsfsf'
    zen_wor = dict()
    for i in f:
        if i not in zen_wor:
            zen_wor[i] = 0
        zen_wor[i] += 1
    return zen_wor
print(amount_repetitions_letters())


""" __________________________________________________________________ """

""" __________________WHILE________________________________________________ """


def wil_l():
    day = 0
    a = 1000

    while a >= 0:
        sum_day = 2*day
        a -= sum_day
        day += 1

    print(f"Day {day}, todau run {sum_day}, left to run {a} ")


wil_l()


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

""" ____________________________________________________________________"""

""" _________________________FOR___________________________________________"""



"""
1, 1, 2, 3, 5, 8, 13
"""

def for_one(n):
    const_1 = const_2  = 1
    sum_prog = 0
    for i in range(n):
        if n < 3:
            sum_prog = 1
        else:
            i += 2
            sum_prog = const_2 + const_1
            const_1 = const_2
            const_2 = sum_prog
    print(sum_prog)


print(for_one(4))


"""1, 1, 1, 3, 5, 9, 17…"""
def for_two(n):
    const_1 = const_2 = const_3 = 1
    sum_prog = 0
    for i in range(n):
        if n < 3:
            sum_prog = 1
        else:
            i += 2
            sum_prog = const_3 + const_2 + const_1
            const_1 = const_2
            const_2 = const_3
            const_3 = sum_prog
            print(sum_prog)
print(for_two(4))

def for_three(n):
    roots = [ i**2 for i in range(n) if i % 2 == 0]

    return  roots
print(for_three(29))
# """ доделать генератором"""

def  for_zvez():
    a = 4
    b = 5
    c = 'k'
    d = ' '
    prom = print(c + d * a)

    print(a * c)
    for i in range(b-2):

        prom
    print(a * c)

for_zvez()





import  random



def chet_nechet():
    n = random.randint(1, 10)

    


""" ____________________________________________________________________"""

""" _________________________IF___________________________________________"""



def vvod():
    try:
        g = int(input("Dведите Ваш вариант, целое число"))
    except (TypeError, ValueError):
        print('Вы ошиблись попробуйте всеже ввести число int')
    return g


def game():
    # g = vvod()
    n = random.randint(1, 10)
    col_vo_part = 0
    col_vo_hodov = 0
    itog = list()

    for i in range(5):
            col_vo_hodov +=i
            g = int(input("Dведите Ваш вариант, целое число"))
            if g > n:
                print('Многовато будет')

                continue
            if  g < n:
                print('Многовато будет')
                continue
            else:
                print( 'Урааа Вы выиграли')
                quit()

    return col_vo_part, col_vo_hodov, n, itog

val = game()

print(f'Вы сьиграли {val[0]} партий, Ходов сделано  {val[1]}, Вы угадывали число {val[2]}, {val[3]}')


""" ____________________________________________________________________"""

""" _________________________Система счисления___________________________________________"""


