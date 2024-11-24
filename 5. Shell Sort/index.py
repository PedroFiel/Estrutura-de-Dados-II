def shell_sort(arr, sequence='shell'):
    n = len(arr)
    
    if sequence == 'shell':
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
    
    elif sequence == 'knuth':
        gap = 1
        while gap < n // 3:
            gap = 3 * gap + 1
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 3
    
    elif sequence == 'hibbard':
        k = 1
        gap = 1
        while gap < n:
            gap = 2 ** k - 1
            k += 1
        gap //= 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            k -= 1
            gap = 2 ** k - 1
    
    return arr

arr = [23, 29, 15, 19, 31, 7, 9, 5, 2]
print("Original:", arr)
print("Shell Sort (Shell):", shell_sort(arr.copy(), 'shell'))
print("Shell Sort (Knuth):", shell_sort(arr.copy(), 'knuth'))
print("Shell Sort (Hibbard):", shell_sort(arr.copy(), 'hibbard'))