# '''
# Задание: используя только Python, создать файл с любым названием, записать туда результат пользовательского ввода,
#  затем закрыть файл. После этого открыть в бинарном виде и вывести в консоль бинарное представление данного ввода.
# '''
#
# # def counter(fn):
# #     i = 0
# #     def wrapper(*args, **kwargs):
# #         result = fn(*args, **kwargs)
# #         wrapper.count = wrapper.count + 1
# #         print("Функция была вызвана {} раз".format(wrapper.count))
# #         return result
# #     wrapper.count = 0
# #     return wrapper
# #
# # @counter
# # def f():
# #     print("My funct")
# # f = counter(f)
# #
import datetime
import time
#
#
def time_d(func):
    def wrapper(*arg, **kwarg):
        t1 = datetime.datetime.now()
        # print(t1)

        a = func(*arg, **kwarg)

        t2 = datetime.datetime.now()
        # print(t2)
        print(t2 - t1)

        return a

    return wrapper
#
#
# @time_d
# def name():
#     x = 0
#     for i in range(10):
#         x = (i+1 ** 999 + i+1 * len('dfdfdfdfdfdfdfdfdfd') * time.time() ) ** 29
#         y = 9999999999** 999
#     print(f"I am Nikita {x} , {y}")
#
# name()
#
# def f_kech(func):
#     def wrapper(*arg, **kwarg):
#         d = func()
#
#
#         return a
#
#     return wrapper

#
# def f_kech(func):
#     cech = {}
#     print(cech)
#     def wrapper(*arg, **kwarg):
#         # t1 = datetime.datetime.now()
#         # print(t1)
#         # print(arg)
#         if arg in cech:
#             return cech[arg]
#
#         a = func(*arg, **kwarg)
#         cech[arg] = a
#         # print(cech)
#         #
#         # t2 = datetime.datetime.now()
#         # print(t2)
#         # print(t2 - t1)
#
#         return a
#
#     return wrapper
#
# @time_d
# @f_kech
# def fntt(n):
#     i = 0
#     while i < n:
#         i += 1
#         x = 2**i
#     return x
#
# fntt(10000)
# fntt(10000)


# with open('test.txt', 'w', encoding='utf-8') as f:
x = 'sfsfsffsfs'

fl = open('G:\python\papka\ file.txt', 'w')
# fl.write(input('Vvedite tekst'))
fl.write(x)

fl.close()
fl = open('G:\python\papka\ file.txt', 'br')
print('i vot ono')
print(fl.read())
fl.close()


'''
Задача: создать сложную структуру (словарь, у которого есть внутри словарь и список),
 сериализовать ее в формат json и сохранить в файл. 
Результат открыть текстовым редактором и посмотреть на предмет понятности.
'''
import json

# rt = [ {'d':1,'55':0},
#        [1,2,4,5]]
#
# with open("G:\python\papka\ file.txt", "w") as write_file:
#     json.dump(rt, write_file)

'''
Задача: создать сложную структуру (словарь, у которого есть внутри словарь и список), 
сериализовать ее с помощью pickle и сохранить в файл. 
Не забудьте, что файл открывается в бинарном режиме.
Результат открыть текстовым редактором и посмотреть на предмет понятности.
'''
# import pickle
# rt = [ {'d':1,'55':0},
#        [1,2,4,5]]
# with open("G:\python\papka\ file.txt", "wb") as write_file:
#     pickle.dump(rt, write_file)

'''
Реализовать программу, которая вычисляет целиком ряд арифметической прогрессии.
Программа должна реализовывать следующую логику:
При запуске необходим указать аргументы, отвечающие за начальное значение (именованные или позиционные
 – на ваш выбор) и за шаг прогрессии, далее должен идти флаг save/show
При запуске с флагом ‘save’ далее должен идти параметр –i, который указывает путь до файла, в который 
необходимо сохранить итоговый вычисленный ряд
При запуске с флагом ‘show’ далее не должно идти никакого параметра и вычисленный ряд выводится в консоль

'''
import itertools


def wrapper(*args, **kwargs):

            wrapper.count = wrapper.count + 1
            wrapper.count = 0
            print(wrapper.count)
            return wrapper

wrapper()