def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n 
    count = [0] * 10 

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


numeros = [170, 45, 75, 90, 802, 24, 2, 66]
print("Lista original:", numeros)
radix_sort(numeros)
print("Lista ordenada:", numeros)

def counting_sort_base2(arr, exp):
    n = len(arr)
    output = [0] * n  
    count = [0] * 2  

    for i in range(n):
        index = (arr[i] // exp) % 2
        count[index] += 1

    count[1] += count[0]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 2
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort_base2(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_base2(arr, exp)
        exp *= 2

numeros_binarios = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort_base2(numeros_binarios)
print("Lista ordenada em base 2:", numeros_binarios)