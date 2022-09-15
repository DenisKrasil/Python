# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import random

list1 = []
for i in range(int(input("Введите длину списка: "))):
    num = int(random() * 100)
    list1.append(num)
sum = 0
for o in range(1, len(list1), 2):
    sum += list1[o]
print(list1)
print(sum)
