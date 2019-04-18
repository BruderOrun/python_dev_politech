import  random

# #todo 1. Создать список, в котором каждый элемент – кортеж из двух чисел. Отсортировать данный список по
# #todo    убыванию вторых элементов кортежей.
#
#
# def set_2():
#     sett_list = [(1, 0), (2, 4), (3, 2), (4, 9)]
#     print(sett_list)
#     # sett_list = [(i+1, i**2) for i in range(4)]
#
#     s = sorted(sett_list, key=lambda i: i[1], reverse=True)
#     return s
# print(set_2())
#


# # todo 2. Отсортируйте список слов по убыванию длины слова.
#
# d = ' и  вот я  дома дорогая марья ивановна'
# dc = d.split(' ')
# print(dc)
# dss = sorted(dc, key=lambda  i: len(i), reverse= True)
# print(dss)
#
# # todo 3. Реализуйте пример замыкания (например, «инкрементатор»)
# def ink_a(a):
#
#     def ddf(x =6):
#
#          return a + x
#     return ddf
#
# a = ink_a(5)
#
# a1 = ink_a(6)
#
# print(a(7))
#


# todo 4. Написать генератор, возвращающий по очереди все слова, входящие в предложение.
# d = 'и вот я дома дорогая Раиса Владимировна'
#
# dc = d.split(' ')
# # dc = d.strip('')
# print(dc)
#
# def power(dc):
#     for i in dc:
#         yield i
# d = power(dc)
# df = iter(d)
#
# print(next(df))
# print(next(df))
# print(next(df))
# print(next(df))
# print(next(df))
# print(next(df))
# print(next(df))
#   если раскоментить сломается, превышена длинна строки
# print(next(df))

# todo . Написать генератор псевдо случайных чисел
# a = [lambda x : x*random.randint() for n in range(5)]
# b = iter(a)
# print(next(b))
import time
# s = int(time.time())
#
# def ran(x):
#     while True:
#         t = str((x *int(time.time()))**888)
#         t = t[-3::]
#         yield t




# #todo  . Генератор внутри задается какой-нибудь формулой, которая выдает «случайный» результат

#
# a = [lambda x : x*time.time() for _ in range(5)]
# print(a)

#todo 5.На вход генератору приходит seed – начальное значение, при одинаковых начальных значениях два генератора
 #todo будут выдавать одинаковые следующие значения

#
# def ran22(x):
#     s = 0
#     while True:
#         t = str((x *2*s*int(time.time()))**888)
#         t = str(int(t[-2::]) **228 - len('dfdff'))[-3::]
#         s+=1*int(time.time())
#         yield t
# print(next(ran22(59)))
# #
# a = ran22(6)
# print([next(a) for i in range(8)])

#todo 6. Написать корутину, которая реализует бесконечную арифметическую прогрессию с возможностью перезапуска с
# любого места (3, 4, 5, 6, send(30), 31, 32, 33, …)
def coro(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

@coro
def sd():
    i = 0
    while True:
        i +=1
        y = 2 ** i

        x = yield y
        i = x

d = sd()
# d.send(None)


'''

7.Давайте вместе напишем декоратор, который после каждого вызова функции будет выводить в консоль информацию о том, 
сколько раз данная функция уже вызывалась.
Для этого немного отвлечемся на PEP 232 – Function Attributes

'''


def counter(fn):
	def wrapper(*args, **kwargs):
		result = fn(*args, **kwargs)
		wrapper.count = wrapper.count + 1
		print("Функция была вызвана {} раз".format(wrapper.count))
		return result
	wrapper.count = 0
	return wrapper


@counter
def say_word(word):
	print(word)

say_word("Hi")	# Hi! Функция была вызвана 1 раз
say_word("Hi")	# Hi! Функция была вызвана 2 раз
say_word("Hi")	# Hi! Функция была вызвана 3 раз
say_word("Hi")	# Hi! Функция была вызвана 4 раз
say_word("Hi") 	# Hi! Функция была вызвана 5 раз





#
# def coroutine(func):
#     def inner(*args, **kwargs):
#         i = 0
#         func()
#         i+=1
#         print(i)
#
#     return inner()
#
# @coroutine
# def makebold():
#     d = 2+2
#
#     return d
#
# makebold()
# makebold()
# makebold()


'''
8. Напишите декоратор, выводящий в консоль время, в которое функция была запущена.
Вам понадобится модуль datetime и функция datetime.now()
'''

import time
import datetime
# def coro(func):
#     def inner():
#         print(time.time())
#         print(func())
#         print(time.time())
#
#     return inner()


def time_decor(func):
    def wrapper(*arg, **kwarg):
        print(datetime.datetime.now())

        a = func(*arg, **kwarg)

        return a

    return wrapper


@time_decor
def funny(x):
    print("I am funny ", x)

    return 30
print(funny(4))

'''
Написать следующие декораторы:
9. декоратор, замеряющий время выполнения функции и выводящий информацию в консоль
'''


def time_decor(func):
    def wrapper(*arg, **kwarg):
        t1 = datetime.datetime.now()

        print(t1)

        a = func(*arg, **kwarg)

        t2 = datetime.datetime.now()

        print(t2 - t1)

        return a

    return wrapper


@time_decor
def funny(x):
    print("I am funny ", x)

    return 30
print(funny(4))


'''
10. декоратор, кэширующий результаты функции и при каждом вызове обращающийся сначала в кэш 
чтобы проверить, нет ли результата в уже посчитанных. Декоратор не должен зависеть от количества аргументов 
декорируемой функции
'''