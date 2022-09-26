import random


k = int(input('Введите число: '))
polynomial = [str(random.randint(0, 100)) + (f'x**{x}') for x in range(k, -1, -1)]

print(polynomial)
resul_list = list(map(lambda x: x+' + ' if not ('x**0') in x else (x[0:len(x)-4])+' = 0', polynomial))
print(resul_list)

data = open("poly.txt", 'w') # a - (добавляет) r - чтение w - (перезаписывает) 
data.writelines(resul_list) # разделителей не будет
data.close()