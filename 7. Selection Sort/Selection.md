## Passo a Passo do Selection Sort
- Vamos analisar o exemplo [64, 25, 12, 22, 11] para ver como o Selection Sort organiza a lista:

**Iteração 1:**
- Lista: [64, 25, 12, 22, 11]
- Menor elemento encontrado: 11
- Troca 64 com 11
- Lista após a troca: [11, 25, 12, 22, 64]

**Iteração 2:**
- Lista: [11, 25, 12, 22, 64]
- Menor elemento encontrado: 12
- Troca 25 com 12
- Lista após a troca: [11, 12, 25, 22, 64]

**Iteração 3:**
- Lista: [11, 12, 25, 22, 64]
- Menor elemento encontrado: 22
- Troca 25 com 22
- Lista após a troca: [11, 12, 22, 25, 64]

**Iteração 4:**
- Lista: [11, 12, 22, 25, 64]
- Menor elemento encontrado: 25
- Lista já está em ordem, mas a troca com o mesmo elemento acontece
- Lista após a troca: [11, 12, 22, 25, 64]

**Iteração 5:**
- Lista: [11, 12, 22, 25, 64]
- Menor elemento (último): 64
- Lista já está em ordem, mas a troca com o mesmo elemento acontece
- Lista após a troca: [11, 12, 22, 25, 64]

## Análise de Desempenho
- Complexidade de Tempo:
- O Selection Sort tem uma complexidade de tempo de O(n2), onde n é o número de elementos na lista. Isso ocorre porque há dois loops aninhados: um para cada elemento na lista e outro para encontrar o menor elemento restante.

## Listas Pequenas:
- Em listas pequenas, o Selection Sort pode ser adequado devido à sua simplicidade e ao fato de que o overhead de operações constantes é baixo.
- Listas Médias e Grandes:
O desempenho do Selection Sort se deteriora rapidamente à medida que o tamanho da lista aumenta devido à sua complexidade quadrática.
Não é recomendado para listas grandes, pois algoritmos como Merge Sort ou Quick Sort oferecem melhor desempenho com complexidade O(nlogn).
