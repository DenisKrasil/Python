# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# for x in (0, 1):
#     for y in (0, 1):
#         for z in (0, 1):
#             result = (not (x or y or z) == (not (x) and not (y) and not (z)))
#             print(result)

nums = [[[True for x in range(2) for y in range(2) for z in range(2) if (not(x or y or z)) == ((not x) and (not y) and (not z))]]]
print(nums)

# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# from random import random

# list1 = []
# for i in range(int(input("Введите длину списка: "))):
#     num = int(random() * 100)
#     list1.append(num)
# sum = 0
# for o in range(1, len(list1), 2):
#     sum += list1[o]
# print(list1)
# print(sum)

# from random import random

# list1 = []
# for i in range(int(input("Введите длину списка: "))):
#     num = int(random() * 100)
#     list1.append(num)
# res = list(filter(lambda x: x*x, list1))
