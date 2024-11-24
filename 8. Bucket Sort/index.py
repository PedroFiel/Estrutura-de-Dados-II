def bucket_sort_floats(arr):
    n = len(arr)
    if n <= 1:
        return arr

    buckets = [[] for _ in range(n)]

    for num in arr:
        index = int(num * n) 
        buckets[index].append(num)

    for i in range(n):
        buckets[i].sort()

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

floats = [0.23, 0.12, 0.78, 0.45, 0.89, 0.56, 0.34]
ordenados = bucket_sort_floats(floats)
print("Lista de numeros em ponto flutuante ordenada:", ordenados)


def bucket_sort_integers(arr, bucket_size=10):
    if len(arr) == 0:
        return arr

    min_value = min(arr)
    max_value = max(arr)

    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = (num - min_value) // bucket_size
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

integers = [42, 32, 33, 52, 37, 47, 51]
ordenados = bucket_sort_integers(integers)
print("Lista de numeros inteiros ordenada:", ordenados)