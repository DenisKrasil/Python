# Вычислить число c заданной точностью d

d = 0.0001
num = 234.12312545545778
d2 =str(d).split(".")
num2 = str(num).split(".")
while len(d2[1]) < len(num2[1]) :
    num2[1] = num2[1][:-1]
num2 = '.'.join(num2)
print(num2)



# num2 = str(num).split(".")
# num3 = float(num2[1])/d
# num2[1] = str(num3).split(".")[0]
# num='.'.join(num2)
# print(num)



# d = 0.0001
# num = str(input('Введите число: '))
# s = num[:(d+2)]
# print(s)
