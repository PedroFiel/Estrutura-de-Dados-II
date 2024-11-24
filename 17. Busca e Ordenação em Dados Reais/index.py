def bucket_sort(notas):
    bucket_count = 10 
    max_value = 100   
    buckets = [[] for _ in range(bucket_count)]

    for nota in notas:
        index = int(nota / max_value * (bucket_count - 1))
        buckets[index].append(nota)

    for i in range(bucket_count):
        buckets[i].sort()

    sorted_notas = []
    for bucket in buckets:
        sorted_notas.extend(bucket)

    return sorted_notas

notas = [
    88, 95, 70, 100, 67, 85, 90, 76, 92, 89, 
    73, 81, 56, 68, 79, 84, 77, 91, 69, 82, 
    65, 74, 99, 87, 60, 80, 66, 78, 93, 72
]
notas_ordenadas = bucket_sort(notas)
print("Notas ordenadas:", notas_ordenadas)

def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1

        pos = low + ((high - low) // (arr[high] - arr[low]) * (x - arr[low]))

        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1

nota_procurada = 85
indice = interpolation_search(notas_ordenadas, nota_procurada)
if indice != -1:
    print(f"Nota {nota_procurada} encontrada no indice: {indice}")
else:
    print(f"Nota {nota_procurada} não encontrada.")