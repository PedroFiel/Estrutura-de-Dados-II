def merge_sort_strings(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_strings(left_half)
        merge_sort_strings(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i].lower() < right_half[j].lower():
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

palavras = ["banana", "abacaxi", "Uva", "laranja", "maçã"]
merge_sort_strings(palavras)
print("Lista ordenada com Merge Sort:", palavras)

def partition_strings(arr, low, high):
    pivot = arr[high].lower()
    i = low - 1
    for j in range(low, high):
        if arr[j].lower() <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_strings(arr, low, high):
    if low < high:
        pi = partition_strings(arr, low, high)
        quick_sort_strings(arr, low, pi - 1)
        quick_sort_strings(arr, pi + 1, high)

palavras = ["banana", "abacaxi", "Uva", "laranja", "maçã"]
quick_sort_strings(palavras, 0, len(palavras) - 1)
print("Lista ordenada com Quick Sort:", palavras)


def binary_search_strings(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid].lower()

        if mid_val < x.lower():
            low = mid + 1
        elif mid_val > x.lower():
            high = mid - 1
        else:
            return mid
    return -1

palavras_ordenadas = ["abacaxi", "banana", "laranja", "maca", "uva"]
palavra_a_procurar = "laranja"
resultado = binary_search_strings(palavras_ordenadas, palavra_a_procurar)
if resultado != -1:
    print(f"Palavra '{palavra_a_procurar}' encontrada na posicao: {resultado}")
else:
    print(f"Palavra '{palavra_a_procurar}' não encontrada.")