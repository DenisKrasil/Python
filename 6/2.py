#Задайте последовательность чисел. Напишите программу, которая выведет список
#неповторяющихся элементов исходной последовательности.

# my_list=[1,2,3,1,5,7,3,8]

# def uniq(numbers):
#     un_list= []

#     for i in range(len(numbers)):
#         for j in range(len(numbers)):
#             if numbers[i] == numbers[j] and i != j:
#                 break
#         else: un_list.append(numbers[i])
#     return un_list

# print(uniq(my_list))

my_list=[1,2,3,1,5,7,3,8]
my_list=[item for item in my_list if my_list.count(item) == 1]
print(my_list)