# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).
x = int(input('Введите значение x не равное 0:'))
y = int(input('Введите значение y не равное 0:'))

if x > 0 and y > 0:
    print('Точка находится в I четверти')
elif x > 0 and y < 0:
    print('Точка находится в IV четверти')
elif x < 0 and y > 0:
    print('Точка находится во II четверти')
elif x < 0 and y < 0:
    print('Точка находится в III четверти')
