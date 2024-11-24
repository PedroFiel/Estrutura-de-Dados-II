def binary_search(arr, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    
    n = len(arr)
    i = 1
    
    while i < n and arr[i] <= target:
        i *= 2
    
    return binary_search(arr, i // 2, min(i, n - 1), target)

lista = [2, 3, 4, 10, 40, 50, 60, 70, 80, 90, 100]
alvo = 10
indice = exponential_search(lista, alvo)
print(f"O indice do elemento {alvo} e {indice}.")