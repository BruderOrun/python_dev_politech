
''' Страница 6'''
'''
1. Сгенерировать [тип] размера (N  + 2) * 2 (если есть ключи – пусть совпадают с индексами, например) 
пример: [0,1,2,3] или [2,2,2,2]

'''

from collections import Counter
def gen():
    n = 3

    mas = [ i for i in range((n + 2) * 2)]
    return mas

print(gen())

"""
2. Продублировать все значения из сгенерированного [тип], 
и каждое из продублированных увеличить на 1. Пример [0,1,2,3,1,2,3,4] или [2,2,2,2,3,3,3,3]
"""
def doubles():
    tip = gen()

    tip_pl = [(tip[i] + 1) for i in range(len(tip))]


    sum = tip + tip_pl
    return sum

print(doubles())


'''
3. Выбрать из пункта 2 значения, начиная со второго по убыванию числа и до предпоследнего числа. Пример[3,1,2,3]

'''
def slise():

    sl = doubles()[max(doubles())-2:-1]

    return sl
print(slise())
'''
4. Выбрать из пункта 2 только те значения, индексы (ключи) которых в остатке от деления на 3 дают 1. Пример [1, 1, 4]
'''

def index():

    fl =  [ i for i in doubles() if doubles()[i] % 3 == 1]
    return  fl
print(index())
'''
5. Выбрать из пункта 2 любую треть чисел (округляя по правилам округления)

'''
def odna_treti():

    itog = doubles()[::3]

    return itog

print(odna_treti())

"""  Страница 7 """

''' input: натуральное число N.  output: "крылечко" из знаков "=": в первой строке 1, во второй 2, в N-й N. '''

def stairs(g):

    n = ''
    for i in range(g):
        n += '=' * i + '\n'
    return n
print(stairs(6))


#  перевернутое крылечко


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
