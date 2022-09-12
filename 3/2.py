# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент,второй и предпоследний и т.д.
from random import random

list1 = []
for i in range(int(input("Введите длину списка: "))):
    num = int(random() * 10)
    list1.append(num)

print(list1)
b = 1

for i in range(0, len(list1)):
    if i < len(list1)-b:
        mult = list1[i] * list1[len(list1)-b]
        b += 1
        print(mult)
    else:
        if i == len(list1)-b:
            mult = list1[i]**2
            print(mult)
            break
