def partition(arr, low, high, pivot_choice):
    if pivot_choice == 'first':
        pivot_index = low
    elif pivot_choice == 'last':
        pivot_index = high
    elif pivot_choice == 'middle':
        pivot_index = (low + high) // 2

    pivot = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high, pivot_choice='last'):
    if low < high:
        pi = partition(arr, low, high, pivot_choice)
        quick_sort(arr, low, pi - 1, pivot_choice)
        quick_sort(arr, pi + 1, high, pivot_choice)

def sort(arr, pivot_choice='last'):
    quick_sort(arr, 0, len(arr) - 1, pivot_choice)

numeros = [10, 7, 8, 9, 1, 5]
print("Lista original:", numeros)

for choice in ['first', 'last', 'middle']:
    arr_copy = numeros.copy()
    sort(arr_copy, pivot_choice=choice)
    print(f"Lista ordenada com pivo '{choice}':", arr_copy)