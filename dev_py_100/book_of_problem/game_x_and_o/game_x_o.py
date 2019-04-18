import itertools

x = ' X'
y = ' O'


def width(args):
    return args


def height(args):
    return args


s = range(width(3) * height(3))
s_str = {i: '{}'.format("%02d" % i) for i in s}


def field_cre(s_str):  # todo Функуия выводит список s_str хранящий состояние поля.
    print()
    field = '| {0[0]}  | {0[1]}  | {0[2]}  |\n' \
            '____________________\n' \
            '| {0[3]}  | {0[4]}  | {0[5]}  |\n' \
            '____________________\n' \
            '| {0[6]}  | {0[7]}  | {0[8]}  |\n'.format(s_str)
    return print(field)


def step():
    for _ in itertools.count():
        print('Введите номер ячейки X  \n' if g % 2 == 0 else 'Введите номер ячейки O \n')
        try:
            point_step = int(input())
        except:
            print('Вы ввели не целое число')
            print('Введите снова номер ячейки X \n' if g % 2 == 0 else 'Введите снова номер ячейки O \n')
            continue
        if point_step >= 10:
            print('Вы ввели не целое число или число более 9')
            continue
        break
    return point_step


def proverka():

    for i in range(0, 7, 3):
        if s_str[i] == x:
            if s_str[i + 1] == x:
                if s_str[i + 2] == x:
                    print('Выиграл Х')
                    quit()
    for i in range(0, 4):
        if s_str[i] == x:
            if s_str[i + 3] == x:
                if s_str[i + 6] == x:
                    print('Выиграл Х')
                    quit()
    for i in range(1):
        if s_str[i] == x:
            if s_str[i + 4] == x:
                if s_str[i + 8] == x:
                    print('Выиграл Х')
                    quit()
    for i in range(1):
        if s_str[i + 2] == x:
            if s_str[i + 4] == x:
                if s_str[i + 6] == x:
                    print('Выиграл Х')
                    quit()
    for i in range(0, 7, 3):
        if s_str[i] == y:
            if s_str[i + 1] == y:
                if s_str[i + 2] == y:
                    print('Выиграл O')
                    quit()
    for i in range(0, 4):
        if s_str[i] == y:
            if s_str[i + 3] == y:
                if s_str[i + 6] == y:
                    print('Выиграл O')
                    quit()
    for i in range(1):
        if s_str[i] == y:
            if s_str[i + 4] == y:
                if s_str[i + 8] == y:
                    print('Выиграл O')
                    quit()
    for i in range(1):
        if s_str[i + 2] == y:
            if s_str[i + 4] == y:
                if s_str[i + 6] == y:
                    print('Выиграл O')
                    quit()
    return


def cell_replacement():

    sss = step()

    print()
    st_fr = '{}'.format("%02d" % int(sss))

    if g % 2 == 0:
        ono = ' X'
    else:
        ono = ' O'

    if s_str[sss] == x:
            print('Alarm, Alarm !!!!!!!')
            print('Вы выбрали уже занятую клетку \n')
    if s_str[sss] == y:
        print('Alarm, Alarm !!!!!!!')
        print('Вы выбрали уже занятую клетку \n')

    if st_fr == s_str[sss]:
        s_str.update({sss: ono})


if __name__ == "__main__":
    for g in itertools.count():
        field_cre(s_str)
        proverka()
        cell_replacement()
