# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = False
y = False
z = False

result = (not (x or y or z) == (not (x) and not (y) and not (z)))
print(result)

x = False
y = False
z = True

result = (not (x or y or z) == (not (x) and not (y) and not (z)))
print(result)

x = False
y = True
z = False

result = (not (x or y or z) == (not (x) and not (y) and not (z)))
print(result)

x = False
y = True
z = True

result = (not (x or y or z) == (not (x) and not (y) and not (z)))
print(result)

x = True
y = False
z = False

result = (not (x or y or z) == (not (x) and not (y) and not (z)))
print(result)

x = True
y = False
z = True

result = (not (x or y or z) == (not (x) and not (y) and not (z)))
print(result)

x = True
y = True
z = False

result = (not (x or y or z) == (not (x) and not (y) and not (z)))
print(result)

x = True
y = True
z = True

result = (not (x or y or z) == (not (x) and not (y) and not (z)))
print(result)
