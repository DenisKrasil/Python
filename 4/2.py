# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime_fact(N):
    factors = []
    i = 2
    while i * i <= N:
        if N % i == 0:
            factors.append(i)
            N //= i
        else:
            i += 1
    if len(factors) < 1:
        return print(f'Число {N} является простым')
    elif N > 1:
        factors.append(N)
    return factors

print(prime_fact(int(input('Введите натуральное число :'))))
