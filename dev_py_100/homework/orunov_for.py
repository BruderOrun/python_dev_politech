''' Страница 9
1. Найти N-й член последовательности 1, 1, 2, 3, 5, 8, 13...
'''

def for_one(n):
    const_1 = const_2  = 1
    sum_prog = 0
    for i in range(n):
        if n < 3:
            sum_prog = 1
        else:
            i += 2
            sum_prog = const_2 + const_1
            const_1 = const_2
            const_2 = sum_prog
    return sum_prog

print(for_one(2555))

'''
2. Найти N-й член последовательности 1, 1, 1, 3, 5, 9, 17…

'''



def for_two(n):
    const_1 = const_2 = const_3 = 1
    sum_prog = 0
    for i in range(n):
        if n < 3:
            sum_prog = 1
        else:
            i += 2
            sum_prog = const_3 + const_2 + const_1
            const_1 = const_2
            const_2 = const_3
            const_3 = sum_prog
    return sum_prog
print(for_two(4))


''' 
3. Вывести квадраты нечетных чисел до N

'''

def for_three(n):
    roots = [ i**2 for i in range(n) if i % 2 == 0]

    return  roots
print(for_three(40))

'''
4. Вывести прямоугольную рамочку из звёздочек, шириной А звёздочек и высотой В. 

'''
def for_zvez():
    a = 9
    b = 9
    c = '*'
    d = ' '
    prom = c + ((d * (a-2))) + c

    print(a * c)

    for i in range(b-2):

        print(prom)

    print(a * c)

for_zvez()

'''
7. Исходный список содержит положительные и отрицательные числа. Требуется положительные поместить в один список, а отрицательные - в другой

'''
import  random

def two_list():
    li = [ random.randint(-100,100) for i in range(20)]
    listik = li
    list_otr = [ listik[i] for i in range(len(listik)) if listik[i] < 0 ]
    list_pol = [ listik[i] for i in range(len(listik)) if listik[i] >= 0 ]

    print(listik)
    print(list_otr)
    print(list_pol)

two_list()



