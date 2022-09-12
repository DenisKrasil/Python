# Задайте число. Составьте список чисел Фибоначчи, в том числе для
# отрицательных индексов.

def negafib_row(item):
    f1 = 1
    f2 = -1
    list1.insert(0, f1)
    list1.insert(0, f2)
    while item > 2:
        buff = f2
        f2 = f1 - f2
        f1 = buff
        list1.insert(0, f2)
        item -= 1


def fib_row(item):
    f1 = f2 = 1
    list1.append(f1)
    list1.append(f2)
    while item > 2:
        buff = f2
        f2 = f1 + f2
        f1 = buff
        list1.append(f2)
        item -= 1


list1 = [0]
fib_row(11)
negafib_row(11)
print(list1)
