import random
import numpy as np
import itertools
import os.path
from os.path import isfile, join

'''11*) Найти самое короткое название файла в папке (не в подпапках)
'''

import os
df = list()
#TODO check if file
def os_os():
    dir = '/Users/norunov/Desktop/config'
    files = os.listdir(dir)
    # print(files)
    # d = [i for i in files if i == os.path.isfile(files)]
    # print(d)


    onlyfiles = [f for f in files if isfile(join(dir, f))]
    print(onlyfiles)
    #
    # for i in d.items():
    #     if d.keys() ==  df:
    #         print(i)

    # for i in d.items():
    #     if int(max(d.keys())) ==  int(d.keys()):
    #         print(i)
os_os()



# def ra():
#     while itertools.count:
#
#         list_zan = [random.randint(0, 1) for i in range(200)]
#         if sum(list_zan) == 100 and  sum(list_zan) - list_zan[199] == 99:
#             return list_zan
#
#
#
# print(f'список {ra()} \n сумма списка {sum(ra())} \n  последний элимент {ra()[199]}')
#

#
#
# list_zan = list()
# list_zan = [random.randint(0, 1) if i[0] == 0  else i[199] == 1 for i in range(200)]
# print(list_zan)



# sum = 100
# n = 3
# a = np.random.multinomial(sum, np.ones(n)/n, size=1)[0]
# # print (Argentina)
# # print(sum(Argentina))
# print(a)


# import numpy as np
# import matplotlib.pyplot as plt
# # st = 'key'
# # sd = 'another_value'
# # my_dict = {st: 'value'}
# # my_dict.update({'another_key': sd})  # Дополняем.
# # my_dict.update({st: 'yet_another_value'})
# #
# # print(my_dict)
# #
# # #
# # s_str = {0: 'X', 1: 'C', 2: 'X', 3: 'f', 4: 'X', 5: 'd', 6: 'X', 7: 'k', 8: 'X'}
# # for i in range(0,7,3):
# #     x = list
# #     if s_str[i] == 'X':
# #         if s_str[i+1] == 'X':
# #             if s_str[i+2] == 'X':
# #                 print(x)
# # for i in range(0,4):
# #     x = list
# #     if s_str[i] == 'X':
# #         if s_str[i+3] == 'X':
# #             if s_str[i+6] == 'X':
# #                 print(x)
# #                 break
# # for i in range(1):
# #     x = list
# #     if s_str[i] == 'X':
# #         if s_str[i+4] == 'X':
# #             if s_str[i+8] == 'X':
# #                 print(x)
# #                 break
# # for i in range(1):
# #     x = list
# #     if s_str[i+2] == 'X':
# #         if s_str[i+4] == 'X':
# #             if s_str[i+6] == 'X':
# #                 print(x)
# #                 break
#
#
#
# # # todo
# # #  Двумерный массив пикселей:
# # smile = [[0, 0, 1],
# #          [0, 1, 0],
# #          [1, 0, 0]]
# #
# # fig, ax = plt.subplots()
# #
# # ax.imshow(smile)
# #
# # fig.set_figwidth(6)    #  ширина и
# # fig.set_figheight(6)    #  высота "Figure"
# #
# # plt.show()
#
#
# # import numpy as np
# # ''' Найти элемент в двумерном массиве Python
# # '''
# # m = []
# # rows = eval(input("How many rows in the list:"))
# # for row in range(rows):
# #     m.append([])
# #     value = eval(input("Enter a row:"))
# #     m[row].append(value)
# # m = np.array(m)
# # print(m)
# # M = np.amax(m)
# # print(M)
# # index = np.where(M)
# # print(index)
#
#
#
#
#
# # reversed_dict = {x: y for y, x in dictionary.items()}
# #
# # result = [reversed_dict[x] for x in list(set(dictionary.values()) & set(lst))]
# #
# # print(reversed_dict)
# # print(result)
# #
# #
# # f = list(filter(lambda x: dictionary[x] in lst, dictionary))
# # print(f)
# # #
# # def morze():
# #     word = 'hello sailor'
# #     morz = {'a': '• – ', 'e': '• ', 'i': '• • ', 'l': '• – • • ', 'o': '– – – ', 'r': '• – • ', 's': '• • • ', ' ': '_ '}
# #     word_dict = {word[i]  for i in range(len(word))}
# #     print(word_dict)
# #
# # # TODO one for  пройти по хелло
# #     g = list(filter(lambda x: morz[x] in word_dict, morz))
# #     print(g)
# #         print(word_dict[morz])
# #         if word_dict[morz] in morz
#         # if word_dict[i] in morz.keys():
#         #     word_dict[i] = morz.values()
#         #     print(word_dict)
#
# #     for i in morz:
# #         for j in word_dict:
# #             if i == word_dict[j]:qœœ
# #                 word_dict[j] = morz[i]
# #
# #     return word_dict
#
#
#
#
# # import os
# # df = list()
# # def os_os():
# #     dir = '/Users/norunov/Desktop/23'
# #     files = os.listdir(dir)
# #     print(files)
# #     d = { len(i):i for i in files   }
# #     print(max(d))
# #     df = list
# #     df = max((d))
# #     print(df)
# #     for k, v in d.items():
# #
# #         if d[k] ==  df:
# #             print(d.keys())
# #             print(d[k])
# #
# #             ssd = d[v]
# #             print(ssd)
# #
# #             print(d[v])
# #
# #             print(d.values())
# #             print(d[k])
# #
#
#
#     # for i in range(len(d)):
#     #     if d.keys() == df:
#     #         print(d.values())
#
#
#
# # os_os()
# # dir = os.walk('C:\prim')
# # print(dir)
# #
# # def getsubs(dir):
# #
# #     dirs = []
# #
# #     files = []
# #
# #     zen_map = dict()
# #
# #     for filenames in os.listdir(dir):
# #
# #         files.append(filenames)
# #
# #     # for word in files:
# #     #     cleaned_word = word.strip('| * ; ! , : / ').lower()
# #     #     if cleaned_word not in zen_map:
# #     #         zen_map[cleaned_word] = 0
# #     #
# #     #     zen_map[cleaned_word] += 1
# #     #
# #     # return zen_map
# #
# # print(getsubs(dir))
#
# #
# # def sp():
# #     spis = [(2**(2*i)) for i in range(9) if i > 0]
# #
# #     return spis
# # print('fff')
# # print(sp())
#
# '''
#
#  8) Есть число, оно гарантированно степень двойки – узнать какая это степень двойки.
# '''
# #
# # def kv_s(n):
# #     i = 0
# #     cq = 0
# #     while True:
# #         cq = 2 ** i
# #         if cq == n:
# #             break
# #         i += 1
# #
# #     return i
# #
# # print(kv_s(18))
# #
# # a = [lambda x, y: 2 ** y for y in range(10)]
# # n = iter(a)
# # print(next(n))
# # print(next(n))
#
#
# #
# # # ''' 9) Создать список, состоящий из чисел на 1 меньше степеней двойки '''
# # #
# # # def sp():
# # #     spis = [(2**(2*i)) for i in range(9) if i > 0]
# # #
# # #     return spis
# # # print(sp())
# #
# # '''10)  Найти максимальную разницу между соседними числами в массиве'''
# #
#
#     # for i in range(lena-1
#     #     if max < abs ()
# # def razn():
# #     spis = [i**2 for i in range(9) ]
# #     v = list()
# #     for i in range(len(spis)-1):
# #         v.append(spis[i]-spis[i+1])
# #         v.append(abs(v[i]))
# #
# #
# #     return v
# #
# # print(max(razn()))
#
#
#
# # rows = eval(input("How many rows in the list:"))
# # m = []
# # for row in range(rows):
# #   value = eval(input("Enter a row:"))
# #   m.append(value)
# #
# # large = m[0][0]
# # x = 0
# # y = 0
# #
# # for i in range(0, rows):
# #   for j in range(0, len(m[i])):
# #     if(large < m[i][j]):
# #      large = m[i][j]
# #      y = i
# #      x = j
# # print(x, y, large)
# # def for_zvez():
# #     a = 6
# #     b = 7
# #     c = '*'
# #     d = '  '
# #     prom = c + ((d * a)-2) + c
# #
# #     print(a * c)
# #
# #     for i in range(b-2):
# #
# #         print(prom)
# #
# #     print(a * c)
# #
# #
# # for_zvez()
# #
# # def chis():
# #     n = 3
# #
# #     #
# #     # count = 1
# #     # n //= 10
# #     #
# #     # while n > 0:
# #     #     n //= 10
# #     #     count += 1
# #     # return  count
# #     n = len(str(n))
# #     return n
#
#
#
#
# # print(chis())
# # #
# # def polindrom():
# #     n = 'qwerewq'
# #
# #     print('Полиндром' if n == n[::-1] else 'не полиндром')
# #     print(n[::-1])
# #
# # polindrom()
#
#
