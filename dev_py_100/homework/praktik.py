import os
import math
# import numpy as np
import random
from os.path import isfile, join

#
'''
1.	Найти самый часто встречающийся элемент в двумерном массиве (используя список или numpy array)
1 2 3 4 5
1 2 3 3 5
1 2 3 3 3
Ответ - 3

def printMatrix ( matrix ):
   for row in matrix:
      for x in row:
          print ( "{:4d}".format(x), end = "" )
      print ()
'''
def two_m():
    g = [[i ** 2 if i % 2 == 0 else i * 5 - 1 for i in range(8)] for i in range(1)]

    di = [[i ** 2 if i % 2 == 3 else i * 2 - 13 for i in range(6)]  for i in range(2) ] + g*3
    print(f'Массив {di}')

    cw = dict()

    for d in di:
        for x in d:
            if x not in cw:
                cw[x] = 0
            cw[x] += 1
    print(f'Кол-во повторений {cw}')
    print(f'Макс повторений {max(cw.values())}')
    for k, v in cw.items():
        if v == max(cw.values()):
            return k
# print(f'Самое часто повторяемое число {two_m()}')



''' 2) Найти индексы тех пар элементов списка, которые в сумме дают 0. '''


def para():

    sp = [-3,-2,3,0,6,-6,-8,8]
    sl = list()
    sk = list()
    for i in range(len(sp)):
        for j in range(i+1, len(sp)):
            # print(sp[i])
            # print(sp[j])
            if sp[i]+sp[j] == 0:
                sl.append(sp[i])
                sk.append(i)


    return  sp, sk
d = para()
print(f'Массив {d[0]}, индексы пар {d[1]} ')

print('\n')

'''
3.  Найти все ключи словаря, значения которых максимальны для своего типа (строки, числа, списки) в этом списке.
 Пример: {“L”:3, “J”:[1,2], “M”:5, ”C”:3, “F”:”aqws”, “H”:4, “U”:”yhsa”, “O”:[2,1]}
 Ответ: “M”, “U”, “O”
 
'''


from itertools import chain
import operator

def keyss():
    di = {'L':3, 'J':[1,2], 'M':5, 'C':3, 'F':'aqws', 'H':4, 'U':'yhsa', 'O':[2,1]}
    inn = list()
    stt = list()
    lii = list()

    for i in di:
        if type(di[i]) == int:
            inn.append(di[i])
            intt = max(inn)
            if intt == di[i] :
                int_max = i
        if type(di[i]) == str:
            stt.append(di[i])
            sttt = max(stt)
            if sttt == di[i] :
                str_max = i
        if type(di[i]) == list:
            lii.append(di[i])
            liis = max(lii)
            if liis == di[i] :
                lii_max = i


    print(int_max)
    print(str_max)
    print(lii_max)


keyss()

print('\n')

'''
4.  Создать функцию, которая принимает на вход функцию и массив и к каждому элементу массива применяет функцию и
 возвращает массив
'''
# TODO only old sintax  без мап и лямбда
# todo True
b_mas = [1, 24, 1, 2]

def pervaya(a):
    return a+1

def a_b(b, b_mas):
    mas_it = list()
    for i in range(len(b_mas)):
       mas_it.append(b(b_mas[i]))
    return mas_it

import math
print(a_b(math.cos, b_mas))

#
# b_mas = [1, 24, 1, 2]
#
# def pervaya(a):
#     a = a **3
#     return a
#
# def a_b(a, b_mas):
#
#     ma = pervaya(b_mas)
#
#     return ma
#
# print(a_b())
print('\n')


''' 5) Создать список, который для всех чисел от a до b: для четных чисел содержит квадрат числа, для нечетных –
удвоенное число -1.
Пример: a = 1 b = 6 Результат: [1, 4, 5, 16, 9, 36]
# '''
def tfr():
    a = 1
    n = 7

    g = [i**2 if i % 2 == 0 else i*2 - 1 for i in range(a, n)]

    return g

print(tfr())

print('\n')
'''
# 6. Создать функцию переводящую английский алфавит в азбуку морзе
#    Пример: «I am liuba» Результат: .. .- -- .-.. .. ..- .-- .-
# '''
    # word = 'hello sailor'
    # morz = {'a': '• – ', 'e': '• ', 'i': '• • ', 'l': '• – • • ', 'o': '– – – ', 'r': '• – • ', 's': '• • • ', ' ': '_ '}
    # word_dict = {i: word[i]  for i in range(len(word))}


# TODO one for  пройти по хелло
# todo True
def morze():
    word = 'hello sailor'
    morz = {'a': '• – ', 'e': '• ', 'i': '• • ', 'l': '• – • • ', 'o': '– – – ', 'r': '• – • ', 's': '• • • ',
            ' ': '_ '}

    res = list()
    for i in word:
        if i in morz.keys():
            res.append(morz[i])
    return res

print(morze())

#     for i in morz:
#         for j in word_dict:
#             if i == word_dict[j]:
#                 word_dict[j] = morz[i]
#
#     return word_dict
print('\n')



'''
7) Сгенерировать список случайных чисел от 0 до 1, произвольной длинны, сумма чисел списка должны быть больше 100
# (при этом сумма чисел списка без последнего элемента должна быть меньше 100)
'''
import itertools
# TODO while and 2 lines (+1)

def ra():
    l = []
    while sum(l) < 100:
        l.append(random.sample())
        # list_zan = [random.randint(0, 1) for i in range(200)]
        # if sum(list_zan) == 100 and  sum(list_zan) - list_zan[199] == 99:
        #     return list_zan
print(f'список {ra()} \n сумма списка {sum(ra())} \n  последний элимент {ra()[199]}')

#
#
#     for i in range(True) :
#
#         list_zan = [random.randint(0, 1) for i in range(200)]
#         summ = sum(list_zan)
#         if summ == 100:
#             if summ - int(max(len(list_zan))) == 99:
#                 break
#             else:
#                 continue
#         else:
#             continue
#
#
#     return list_zan
#
# print('ff')
# print(ra())
# print(ra()[-1::])

# and list_zan[:-1:] == 1 :

# def spis():
#     list_zan = [random.randint(0,1) for i in range(20)]
#
#
#     return list_zan
# print(spis())
# print(sum(spis()))
#


'''  8) Есть число, оно гарантированно степень двойки – узнать какая это степень двойки.'''

def kv_s(n):
    # i = 0
    # cq = 0
    # while True:
    #     cq = 2 ** i
    #     if cq == n:
    #         break
    #     i += 1
    #
    # return i
    i = 0
    cq = 0
    while  2 ** i != n:
        i += 1

    return i

print(kv_s(64))
print('\n')



''' 9) Создать список, состоящий из чисел на 1 меньше степеней двойки '''
# TODO
# todo True
def sp():
    spis = [2**i -1 for i in range(9)]

    return spis
print(sp())

'''10)  Найти максимальную разницу между соседними числами в массиве'''

#TODO maxx!
#  todo True
def razn():
    spis = [i ** 2 for i in range(9)]

    fr = map(lambda x: abs(spis[x] - spis[x + 1]), range(len(spis) - 1))
    return fr

print(max(razn()))

#     spis = [i**2 for i in range(9) ]
#     v = list()
#     for i in range(len(spis)-1):
#         v.append(spis[i]-spis[i+1])
#         v.append(abs(v[i]))
#
#
#     return v
#
# print(max(razn()))


'''11*) Найти самое короткое название файла в папке (не в подпапках)
'''
#TODO check if file
# todo True

def os_os():
    dir = '/Users/norunov/Desktop/config'
    files = os.listdir(dir)

    only_files = [i for i in files if isfile(join(dir, i))]

    return only_files

print(os_os())


# import os
# df = list()
#
# def os_os():
#     dir = '/Users/norunov/Desktop/23'
#     files = os.listdir(dir)
#     print(files)
#     d = { len(i):i for i in files   }
#     df = max((d))
#     #
#     # for i in d.items():
#     #     if d.keys() ==  df:
#     #         print(i)
#
#     # for i in d.items():
#     #     if int(max(d.keys())) ==  int(d.keys()):
#     #         print(i)
# os_os()