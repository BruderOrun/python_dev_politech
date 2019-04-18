import random


s_str = [''' {}  '''.format("%02d" % i) for i in range(1,10)]


# s_str.form = '''
#            \t| %s | %s | %s |
#            \t-------------
#            \t| %s | %s | %s |
#            \t-------------
#            \t| %s | %s | %s |
#            '''
print(s_str)
print('\n')

field = '| {0[0]} | {0[1]} | {0[2]} |\n' \
         '_________________________\n' \
         '| {0[3]} | {0[4]} | {0[5]} |\n' \
         '_________________________\n' \
         '| {0[6]} | {0[7]} | {0[8]} |\n'.format(s_str)
print(field)
winning_combos = (
        [7, 8, 9], [4, 5, 6], [1, 2, 3], [1, 4, 6], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7])

countt = 1
def step(countt):
    for i in range(1):
        print('Введите номер ячейки X \n' if countt % 2 == 0 else 'Введите номер ячейки O \n')
        try:
            point_step = int(input())
        except:
            print('Вы ввели не целое чило')
            print('Введите снова номер ячейки X \n' if countt % 2 == 0 else 'Введите снова номер ячейки O \n')
            try:
                point_step = int(input())
            except:
                print('Вы ввели не целое чило')
                print('В следующий раз будьте внимательнее \n')
                break
        return point_step

def step_xo():

    r = random.randint(1, 10)
    rs = '{}'.format( "%02d" % r )
    print(rs)

    if field[r] != "X" or "O":
         print(field[r])
step_xo()