num = (input('Введите вещественное число: '))
point = num.split(".")
left = int(point[0])
right = int(point[1])
print(left)
print(right)
sum = 0
while (left != 0):
    sum = sum + (left % 10)
    left = left // 10
while (right != 0):
    sum = sum + (right % 10)
    right = right // 10
print(f'Сумма всех цифр числа равна {sum}')
