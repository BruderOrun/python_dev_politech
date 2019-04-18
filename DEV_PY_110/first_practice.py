
#
#
#
# h = 'k12345678901234567890'
# #
# # for i in range(10):
#
# #    print(h[22])
# #
# # a = list()
# for i in range(len(h)):
#     print('vvod')
#
#     print(h[10])
#     if i == 6:
#         vvod = int(input())
#         g = 0 / 1
#     print(h[4])


'''
Квадраты всех четных чисел (используя map и filter)
стра 4

'''

# old_list = [1, 2, 3, 4, 5, 6]
#
# import itertools
#
# mapp = filter(lambda x:  x % 2 == 0 , itertools.count())
#
# filtt = map(lambda x:  x**2 , mapp)
#
# for i  in range(50):
#     print(next(filtt))
#
#

'''
Дана входная строка и массив чисел, необходимо вернуть строку с теми буквами, которые стоят на указанных
 местах (два варианта, используя и не используя list comprehensions)
# «Всем привет», [1, 3, 5] -> «смп»

# '''
#
# old_str = 'ПРИВЕЕТ'
# old_list = [1, 3, 5]
#
# # fill = filter(lambda x:  x in old_list , range(len(old_str)))
# fill = map(lambda x:  old_str[x]  , old_list)
# # mapp = map(lambda x:  x *3  , fill)
#
# print(''.join(fill))

'''
Дан текст (предложения разделены только точками), в котором буквы могут находиться в разных регистрах. 
Необходимо вернуть текст, в котором все буквы в нижнем регистре, а первые буквы каждого предложения – в верхнем. 
Пользоваться можно встроенными функциями строки (кроме capitalize ☺), всеми изученными в этой теме функциями 
и модулем itertools.
'''
# slovo = 'Выпьем няня ГДЕ ЖЕ круЖка.Эй давай налей старушка.'
#
# # print(slovo)
# slovo = slovo.lower()
# slovo += 'k'
#
# slovo = slovo.split('.')
# print(slovo)
# slovo = map(lambda x: x[0].upper()+x[1:], slovo)
# print(".".join(slovo)[:-1])
#
#

'''
Демонстрация: functools.reduce

Задание:
создайте функцию pipeline_each, в которую вы будете подавать итерируемый объект и список функций, 
которые последовательно надо к нему применить.  Ответ – объект после применения функций в указанном порядке.
'''
# l = [lambda x: x**2, lambda x: x*4, lambda x: x*9]
# el = [8,9,16]
#
# def apply(func, item):
#     for function in func:
#         for i in item:
#
#             yield function(i)
# print(list(apply(l, el)))
#
#
#
