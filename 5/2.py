# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

# candies = 221
# while candies>0:
#     point=False
#     while point==False:
#         num=int(input('Первый игрок, сколько хотите забрать конфет(не больше 28 за раз): '))
#         if num <= 0 or num >28:
#             print('Вы ввели неверное число конфет')
#             continue
#         else:
#             candies=candies-num
#             if candies <= 0:
#                 print('Поздравляю! Первый игрок все конфеты ваши')
#                 break
#             else:
#                 print(f'Конфет осталось: {candies}')
#                 point=True
#     while point==True:
#         num=int(input('Второй игрок, сколько хотите забрать конфет(не больше 28 за раз): '))
#         if num <= 0 or num >28:
#             print('Вы ввели неверное число конфет')
#             continue
#         else:
#             candies=candies-num
#             if candies <= 0:
#                 print('Поздравляю! Второй игрок все конфеты ваши')
#                 break
#             else:
#                 print(f'Конфет осталось: {candies}')
#                 point=False


# from random import randint
# user=input('Введетие ваше имя: ')
# candies = 221
# while candies>0:
#     point=False
#     while point==False:
#         num=int(input(f'{user}, сколько хотите забрать конфет(не больше 28 за раз): '))
#         if num <= 0 or num >28:
#             print('Вы ввели неверное число конфет')
#             continue
#         else:
#             candies=candies-num
#             if candies <= 0:
#                 print('Поздравляю! {user}, все конфеты ваши')
#                 break
#             else:
#                 print(f'Конфет осталось: {candies}')
#                 point=True
#     num=randint(1,28)
#     print(f'Бот забирает {num}')
#     candies=candies-num
#     if candies <= 0:
#         print('Все конфеты достаются бездушной машине. Соболезную')
#     else:
#         print(f'Конфет осталось: {candies}')


from random import randint
user=input('Введетие ваше имя: ')
candies = 221
while candies>0:
    point=False
    while point==False:
        num=int(input(f'{user}, сколько хотите забрать конфет(не больше 28 за раз): '))
        if num <= 0 or num >28:
            print('Вы ввели неверное число конфет')
            continue
        else:
            candies=candies-num
            if candies <= 0:
                print(f'Поздравляю! {user}, все конфеты ваши')
                break
            else:
                print(f'Конфет осталось: {candies}')
                point=True
    if candies > 29:
        for i in range (1, 29):
            chit=candies-i
            if chit%29==0:
                print(f'Бот забирает {i}')
                candies=candies-i
                print(f'Конфет осталось: {candies}')
                point=False
                break
        if point == True:
            num=randint(1,28)
            print(f'Бот забирает {num}')
            candies=candies-num
    else:
        print(f'Бот забирает {candies} конфет')
        candies=0
        print('Все конфеты достаются бездушной машине. Соболезную')
        break

    # while point==True:
    #     if candies > 29:
    #         num=randint(1,28)
    #         chit=candies-num
    #         if chit%29==0:
    #             print(f'Бот забирает {num}')
    #             candies=candies-num
    #             print(f'Конфет осталось: {candies}')
    #             point=False
    #         else:
    #             continue

    #     else:
            # print(f'Бот забирает {candies} конфет')
            # candies=0
            # print('Все конфеты достаются бездушной машине. Соболезную')
            # break