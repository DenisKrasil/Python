# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import random, randint

k = int(input('Введите значение k: '))
list1=[]
c=int(randint(0, 100))

for i in range(1, k+1):
    num = int(randint(0, 100))
    if num > 0:
        list1.insert(0, f'{num}X^{i}')
    else:
        continue


file = open("poly2.txt", "w+")
for i in range(0, len(list1)):
    file.write(f'{(str(list1[i]))}+')
file.write(f'{str(c)}=0')
file.close()
