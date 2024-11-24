def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        
        pos = low + ((high - low) * (target - arr[low]) // (arr[high] - arr[low]))
        
        if arr[pos] == target:
            return pos
        
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1

lista_uniforme = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
alvo = 70
indice = interpolation_search(lista_uniforme, alvo)
print(f"O indice do elemento {alvo} e {indice}.")