def ternary_search(arr, left, right, x):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2

        if x < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, x)
        elif x > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, x)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, x)
    
    return -1

arr = [2, 3, 4, 10, 40]
x = 10
resultado = ternary_search(arr, 0, len(arr) - 1, x)
print(f"Elemento encontrado na posicao: {resultado}" if resultado != -1 else "Elemento nao encontrado")