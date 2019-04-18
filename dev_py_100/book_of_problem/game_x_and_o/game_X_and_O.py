import itertools


def width(args = 3):
    # try:
    #     args = int(input('Введите ширину поля, поле принимает только int'))
    # except (TypeError, ValueError):
    #     print('Вы ввели не int')
    #     print('Научитесь нажимать на клавиши')
    #     quit()
    # else:args
    return args

def height(args = 3):
    # try:
    #     args = int(input('Введите ширину поля, поле принимает только int'))
    # except (TypeError, ValueError):
    #     print('Вы ввели не чило')
    #     print('Научитесь нажимать на клавиши')
    #     quit()
    return args


s = range(width() * height())
s_str = {i : '{}'.format("%02d" % i) for i in s}


def field_cre(s_str):
    print()
    field = '| {0[0]}  | {0[1]}  | {0[2]}  |\n' \
            '____________________\n' \
            '| {0[3]}  | {0[4]}  | {0[5]}  |\n' \
            '____________________\n' \
            '| {0[6]}  | {0[7]}  | {0[8]}  |\n'.format(s_str)
    field_print = print(field)
    return field_print
    # def fil():
    #     for i in range(1):
    #         print(f" [ {s_str.get((0))} ] " + f" [ {s_str.get(1)} ] " + f" [ {s_str.get(2)} ] \n")
    #         print(f" [ {s_str.get((3))} ] " + f" [ {s_str.get(4)} ] " + f" [ {s_str.get(5)} ] \n")
    #         print(f" [ {s_str.get((6))} ] " + f" [ {s_str.get(7)} ] " + f" [ {s_str.get(8)} ] \n")
    # return fil()

#     width = 3
#     height = 3
#     s = range(width * height)
#     s_str = [' {} '.format("%02d" % i) for i in s]
#     matrix = np.array(s_str).reshape(width, height)
#     for row in matrix:
#         print()
#         print(list(row))

def step(*g):
    for i in range(1):
        print('Введите номер ячейки X  \n' if countt % 2 == 0 else 'Введите номер ячейки O \n')
        try:
            point_step = int(input())
        except:
            print('Вы ввели не целое число')
            print('Введите снова номер ячейки X \n' if countt % 2 == 0 else 'Введите снова номер ячейки O \n')
            try:
                point_step = int(input())
            except:
                print('Вы ввели не целое число')
                print('В следующий раз будьте внимательнее \n')
                break
        return point_step
countt = 1
a_count = 0

def cell_replacement():
    x  = ' X'
    y  = ' O'
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
    print()
    st = step()
    st_fr = '{}'.format("%02d" % int(st))
    minus_count = 0

    if countt % 2 == 0:
        ono = ' X'
    else:
        ono = ' O'


    if s_str[st] == x:
            print('Alarm, Alarm !!!!!!!')
            print('Вы выбрали уже занятую клетку \n')
    if s_str[st] == y:
        print('Alarm, Alarm !!!!!!!')
        print('Вы выбрали уже занятую клетку \n')


    if st_fr == s_str[st]:
        s_str.update({st: ono})

for i in itertools.count():
    field_cre(s_str)
    cell_replacement()
    countt+=1





