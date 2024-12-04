import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def main():
    print("Escolha um algoritmo de ordenação:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    sort_choice = int(input("Digite o número do algoritmo de ordenação desejado: "))

    print("Escolha um algoritmo de busca:")
    print("1. Busca Linear")
    print("2. Busca Binária")
    search_choice = int(input("Digite o número do algoritmo de busca desejado: "))

    arr = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))
    element = int(input("Digite o elemento a ser procurado: "))

    sorting_algorithms = [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort]
    sort_function = sorting_algorithms[sort_choice - 1]
    start_time = time.time()
    sorted_arr = sort_function(arr.copy())
    sort_time = time.time() - start_time
    print(f"Lista ordenada: {sorted_arr}")
    print(f"Tempo de ordenação: {sort_time:.6f} segundos")

    searching_algorithms = [linear_search, binary_search]
    search_function = searching_algorithms[search_choice - 1]
    start_time = time.time()
    index = search_function(sorted_arr if search_choice == 2 else arr, element)
    search_time = time.time() - start_time
    if index != -1:
        print(f"Elemento encontrado no índice: {index}")
    else:
        print("Elemento não encontrado.")
    print(f"Tempo de busca: {search_time:.6f} segundos")

if __name__ == "__main__":
    main()