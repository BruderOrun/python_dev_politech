'''

Автор задумывает число (натуральное, из интервала от 1 до 100). Пользователь это число отгадывает:
вводит свои варианты, получает ответы "больше, "меньше" или "да, это оно".

    Уровень 1: играется всего одна партия
    Уровень 2: в конце игры у пользователя спрашивают, хочет ли он сыграть ещё. Ведётся подсчёт партий.
    Уровень 3: у пользователя есть лимит в 50 ходов на все партии, пока он его не исчерпал - играет.
    Ведётся подсчёт законченных партий.


'''
import random


def vab_1(*g):
    try:
        g = int(input('''Давайте сьиграем, введите Ваш вариант,\n целое число от 1 до 10 !!!! \n '''))
    except (TypeError, ValueError):
        print('Выошиблись, введите значение типа int')
    return g

def vab_2(*gr):
    try:
        gr = int(input('Вводите 2 раза для надежности'))
    except (TypeError, ValueError):
            print('Может еще разочек )))  ')
    return gr

def rand():
    n = random.randint(1, 10)
    return n

def game():
    col_vo_part = 0
    col_vo_hodov = 0
    col_vo_vair = 0
    itog = list()
    limits = 50

    for i in range(limits):

        # print(f'part {col_vo_part}')
        n = rand()

        for i in range(limits):

                col_vo_hodov += 1

                limits -= 1
                print(f'limit{limits}')
                print(f'col_vo_hodov {col_vo_hodov}')
                print(f'iskomoe {n}')
                g = vab_1()
                if type(g) != int:
                    continue
                if g > n:
                    print('Многовато будет\n')
                    continue
                if  g < n:
                    print('Маловато будет \n')
                    continue
                else:
                    print( 'Урааа Вы выиграли\n')
                    col_vo_vair += 1
                    print(f'colvo vaigr {col_vo_vair}')
                    col_vo_part += 1
                    for i in range(1):
                        print(f'Вам понравилось?, играем дальше \n Ваш кредитный лимит { limits } ходов. \n если хотите играть дальше, выберите   ( 1 ), для выхода, любую  ' )
                        vab_2()
                        n = rand()

                        if vab_2() == 1:
                            continue
                        else:
                            print('Очень жаль, может в другой раз')
                        quit()
                    continue
    return col_vo_part, col_vo_hodov, n, itog

val = game()

print(f'Вы закончили {val[0]} партий, Ходов сделано  {val[1]}')