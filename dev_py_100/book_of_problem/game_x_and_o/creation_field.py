import numpy as np


# def width(args = 3):
    # try:
    #     args = int(input('Введите ширину поля, поле принимает только int'))
    # except (TypeError, ValueError):
    #     print('Вы ввели не int')
    #     print('Научитесь нажимать на клавиши')
    #     quit()
    # else:args
    # return args

# def height(args = 3):
    # try:
    #     args = int(input('Введите ширину поля, поле принимает только int'))
    # except (TypeError, ValueError):
    #     print('Вы ввели не чило')
    #     print('Научитесь нажимать на клавиши')
    #     quit()
#     return args
#
#
# s = range(width() * height())
# s_str = {i : '{}'.format("%02d" % i) for i in s}

    # st = step()
    # st_fr = '{}'.format("%02d" % int(st))
    # if st_fr == s_str[st]:
    # return s_str
#
#
# def field_cre(s_str):
#     def fil():
#         for i in range(1):
#             print(f" [ {s_str.get((0))} ] " + f" [ {s_str.get(1)} ] " + f" [ {s_str.get(2)} ] \n")
#             print(f" [ {s_str.get((3))} ] " + f" [ {s_str.get(4)} ] " + f" [ {s_str.get(5)} ] \n")
#             print(f" [ {s_str.get((6))} ] " + f" [ {s_str.get(7)} ] " + f" [ {s_str.get(8)} ] \n")
#     return fil()
    # matrix = np.array(field_list()).reshape(width(), height())
    # for row in matrix:
    #    print_field =   print(f' {list(row)} \n')

# field_cre()
# print(type(field_list()[1]))





# #
# #
# # wi = width()
# # he = height()
# # wehe = wi * he
# ''' можно использовать для игры Go'''
#
# def field():
#     j = 0
#
#     field = { x: x for x in range(1, 9) for x in range(1, 10)}
#
#
#     field = {x: y for x, y in zip(range(1, 10), range(15, 19)) for i in range(0, 8)}
#
#
#     a = {'key1': 'word1', 'key2': 'word2', 'key3': 'word3'}
#     b = {key.upper(): value[::-1] for key, value in a.items()}
#
#     field = [[j for j in range(2)] for j in range(9)]
#
#
#     for i in range(0, 9):
#         field[i] = str('0') + field[i]
#     return field
#
# #
#
# def field_cre():
#
#     width = 3
#     height = 3
#     s = range(width * height)
#     s_str = [' {} '.format("%02d" % i) for i in s]
#     matrix = np.array(s_str).reshape(width, height)
#     for row in matrix:
#         print()
#         print(list(row))

          #
            # print(f" [ {field().get(1)} ] " + f" [ {field().get(2)} ] " + f" [ {field().get(3)} ] ")
            # print()
            # print(f" [ {field().get(3)} ] " + f" [ {field().get(4)} ] " + f" [ {field().get(5)} ] ")
            # print()
            # print(f" [ {field().get(7)} ] " + f" [ {field().get(8)} ] " + f" [ {field().get(9)} ] ")
#
#
# #     for i in range(he):
# #         print(field()[wi * i:wi * i + wi:])
# #         print()
# #
# #
# #     return
#
# # print(field().get(1))
# # print(field().values()ues(6))
#
#
# import numpy as np
#
#
# class Field:
#     def init(self, width=None, height=None):
#         self.width = width or self.__insert_parameter(
#             description='ширина')  # если первое значение задано, то выводит его, а если первое=None, то выводит второе значение
#         self.height = height or self.__insert_parameter(description='длина')
#
#     def __insert_parameter(self, description):
#         try:
#             value = int(input('Введите {} поля, поле принимает только int'.format(description[:-1] + 'у')))
#         except (TypeError, ValueError):
#             raise ValueError('Вы ввели не int. Научитесь нажимать на клавиши!')
#         return value
#
#     def create_field(self):
#         s = range(self.width * self.height)
#         s_str = [' {} '.format("%02d" % i) for i in s]
#         matrix = np.array(s_str).reshape(self.width, self.height)
#         for row in matrix:
#             print(list(row))
#
#
# field_fun = Field(5, 5)
# field_fun.create_field()