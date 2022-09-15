# Задайте число. Составьте список чисел Фибоначчи, в том числе для
# отрицательных индексов.

def negafib_row(item):
    f1 = 1
    f2 = -1
    nega_list = []
    nega_list.insert(0, f1)
    nega_list.insert(0, f2)
    while item > 2:
        buff = f2
        f2 = f1 - f2
        f1 = buff
        nega_list.insert(0, f2)
        item -= 1
    return nega_list


def fib_row(item):
    f1 = f2 = 1
    fib_list=[]
    fib_list.append(f1)
    fib_list.append(f2)
    while item > 2:
        buff = f2
        f2 = f1 + f2
        f1 = buff
        fib_list.append(f2)
        item -= 1
    return fib_list


list1 = [0]
list1.append(fib_row(11))
list1.insert(0,negafib_row(11))
print(list1)


