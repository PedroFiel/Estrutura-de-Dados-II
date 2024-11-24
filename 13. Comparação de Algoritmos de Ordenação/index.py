import time

def measure_time_and_comparisons(sort_function, arr):
    comparisons = [0] 
    start_time = time.time()
    sorted_arr = sort_function(arr, comparisons)
    end_time = time.time()
    return sorted_arr, end_time - start_time, comparisons[0]

def shell_sort(arr, comparisons):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparisons[0] += 1
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def merge_sort(arr, comparisons):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L, comparisons)
        merge_sort(R, comparisons)

        i = j = k = 0
        while i < len(L) and j < len(R):
            comparisons[0] += 1
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

def selection_sort(arr, comparisons):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            comparisons[0] += 1
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def quick_sort(arr, comparisons):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            if arr[j] < pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)

    quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr

def bucket_sort(arr, comparisons):
    if len(arr) == 0:
        return arr
    
    max_value = max(arr)
    size = max_value // len(arr) + 1  
    buckets = [[] for _ in range(len(arr))]
    
    for i in range(len(arr)):
        j = arr[i] // size
        buckets[j].append(arr[i])

    result = []
    for i in range(len(arr)):
        insertion_sort(buckets[i], comparisons)
        result.extend(buckets[i])
    
    return result

def insertion_sort(arr, comparisons):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisons[0] += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def radix_sort(arr, comparisons):
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

        for i in range(len(arr)):
            arr[i] = output[i]

    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

arr = [
    42, 17, 63, 8, 91, 35, 76, 54, 29, 3, 
    88, 12, 67, 45, 23, 99, 7, 31, 58, 72, 
    95, 5, 60, 14, 47, 81, 26, 55, 1, 78, 
    19, 34, 87, 50, 11, 70, 24, 93, 6, 40, 
    64, 20, 84, 37, 10, 53, 90, 27, 75, 4, 
    82, 30, 61, 16, 49, 92, 22, 56, 9, 73, 
    98, 13, 66, 25, 83, 46, 32, 94, 18, 59, 
    41, 68, 2, 80, 36, 100, 21, 57, 86, 28, 
    74, 15, 52, 89, 33, 62, 97, 43, 79, 48, 
    85, 39, 65, 69, 77, 51, 44, 38, 71, 96,
    101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
    111, 112, 113, 114, 115, 116, 117, 118, 119, 120,
    121, 122, 123, 124, 125, 126, 127, 128, 129, 130,
    131, 132, 133, 134, 135, 136, 137, 138, 139, 140,
    141, 142, 143, 144, 145, 146, 147, 148, 149, 150,
    151, 152, 153, 154, 155, 156, 157, 158, 159, 160,
    161, 162, 163, 164, 165, 166, 167, 168, 169, 170,
    171, 172, 173, 174, 175, 176, 177, 178, 179, 180,
    181, 182, 183, 184, 185, 186, 187, 188, 189, 190,
    191, 192, 193, 194, 195, 196, 197, 198, 199, 200,
    201, 202, 203, 204, 205, 206, 207, 208, 209, 210,
    211, 212, 213, 214, 215, 216, 217, 218, 219, 220,
    221, 222, 223, 224, 225, 226, 227, 228, 229, 230,
    231, 232, 233, 234, 235, 236, 237, 238, 239, 240,
    241, 242, 243, 244, 245, 246, 247, 248, 249, 250,
    251, 252, 253, 254, 255, 256, 257, 258, 259, 260,
    261, 262, 263, 264, 265, 266, 267, 268, 269, 270,
    271, 272, 273, 274, 275, 276, 277, 278, 279, 280,
    281, 282, 283, 284, 285, 286, 287, 288, 289, 290,
    291, 292, 293, 294, 295, 296, 297, 298, 299, 300
]

algorithms = {
    "Shell Sort": shell_sort,
    "Merge Sort": merge_sort,
    "Selection Sort": selection_sort,
    "Quick Sort": quick_sort,
    "Bucket Sort": bucket_sort,
    "Radix Sort": radix_sort
}

results = []

for name, func in algorithms.items():
    arr_copy = arr.copy()
    sorted_arr, exec_time, comparisons = measure_time_and_comparisons(func, arr_copy)
    results.append((name, exec_time, comparisons))

for result in results:
    print(f"{result[0]} - Tempo de execucao: {result[1]:.6f} segundos, Comparacoes: {result[2]}")