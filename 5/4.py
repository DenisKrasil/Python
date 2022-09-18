# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

def compr(str1):

    compression = ''

    i = 0
    while i < len(str1):
        count = 1

        while i + 1 < len(str1) and str1[i] == str1[i + 1]:
            count += 1
            i += 1

        compression += str(count)+ str1[i]
        i=i+1
    
    return compression

str1 = open("input.txt", "r").read()
file = open("output.txt", "w+")
file.write(compr(str1))
file.close()


