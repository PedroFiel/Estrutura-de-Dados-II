## Conceito de "Baldes" no Bucket Sort
- O Bucket Sort é um algoritmo que divide a lista de entrada em várias partes menores chamadas "baldes". Cada balde é responsável por um intervalo específico de valores. O processo de ordenação envolve três etapas principais: distribuir os elementos nos baldes, ordenar cada balde individualmente e então concatenar os baldes ordenados.

# Passos do Bucket Sort
1. Distribuição nos Baldes
    - Definição de Intervalos:
        - Primeiro, a lista de valores é dividida em intervalos que correspondem a diferentes baldes. A escolha do intervalo depende da distribuição dos dados e do número total de baldes desejados.
    - Atribuição de Elementos:
        Cada elemento da lista é colocado no balde correspondente ao seu intervalo. Isso é feito calculando a posição do elemento em relação ao intervalo total e mapeando-o para o índice do balde apropriado.
        Por exemplo, em uma lista de números em ponto flutuante no intervalo [0, 1), se estivermos usando 10 baldes, um número como 0.23 seria colocado no terceiro balde, pois 0.23×10≈2.3.
2. Ordenação dos Baldes
    - Ordenação Interna:
        - Após todos os elementos serem distribuídos nos baldes, cada balde é ordenado individualmente. Como os elementos dentro de cada balde estão em um intervalo pequeno e próximo, algoritmos simples como o Insertion Sort são frequentemente usados para ordenar cada balde eficientemente.
    - A escolha do algoritmo para ordenar os baldes pode variar dependendo do contexto ou do número de elementos em cada balde.
3. Concatenar Baldes Ordenados
    - Combinação Final:
        - Depois que todos os baldes individuais são ordenados, eles são concatenados na ordem para formar a lista final ordenada.
        - Isso é feito simplesmente percorrendo cada balde em ordem e juntando seus elementos ordenados.