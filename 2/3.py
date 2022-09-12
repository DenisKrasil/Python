k = int(input("Введите число k: "))
list1 = []
for i in range(1, k+1):
    a = (1+(1/i)) ** i
    list1.append(a)
print(list1)
print(sum(list1))
