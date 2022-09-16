# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

f1 = open("poly.txt", "r").read()
f2 = open("poly2.txt", "r").read()
f1=f1.split('+')
f2=f2.split('+')
for k in range (0,len(f1)):
    if k < len(f1)-1:
        f1[k]=f1[k].split('X^')
    else:
        f1[k]=f1[k].split('=')

for j in range (0,len(f2)):
    if j < len(f2)-1:
        f2[j]=f2[j].split('X^')
    else:
        f2[j]=f2[j].split('=')

def sum_poly(list1,list2):
    sum=[]
    new_poly=[]
    result=''
    if len(list1) < len(list2):
        while len(list1)!= len(list2):
            list1.insert(0,0)
        for i in range (0, len(list1)):
            if list1[i]==0:
                sum.append(list2[i][0])
                sum.append(list2[i][1])
            else:
                sum.append(str(int(list1[i][0])+int(list2[i][0])))
                sum.append(str(int(list1[i][1])+int(list2[i][1])))
    else:
        while len(list2)!= len(list1):
            list2.insert(0,0)
        for i in range (0, len(list1)):
            if list2[i]==0:
                sum.append(list1[i][0])
                sum.append(list1[i][1])
            else:
                sum.append(str(int(list1[i][0])+int(list2[i][0])))
                sum.append(str(int(list1[i][1])+int(list2[i][1])))
    for par in range(0,len(sum)-2,2):
        new_poly.append(f'{sum[par]}x^{sum[par+1]}+')
    new_poly.append(f'{sum[-2]}={sum[-1]}')
    for pol in new_poly:
        result+=pol
    return result
file = open("poly3.txt", "w+")
file.write(sum_poly(f1,f2))
file.close
