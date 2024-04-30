def burbuja(num):
    n = len(num)
    for i in range(n):
        for j in range(0, n-i-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]

numeros = [64, 34, 25, 12, 22, 11, 90]
burbuja(numeros)
print("Lista ordenada:", numeros)