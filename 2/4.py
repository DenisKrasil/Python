N = int(input("Введите N:"))
M = input("Введите номера элементов через пробел: ").split(' ')
M = [int(item) for item in M]
list1 = list(range(-N, N+1))
i = 0
res = 1
while i < len(M):
    res = (list1[M[i]])*res
    i += 1
print(list1)
print(M)
print(res)
