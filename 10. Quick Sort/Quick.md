## Análise de Desempenho
   O desempenho do Quick Sort pode variar significativamente com base na escolha do pivô e na natureza da lista de entrada.

## Listas Quase Ordenadas
    - Primeiro ou Último Elemento como Pivô: Se a lista estiver quase ordenada e o primeiro ou o último elemento for escolhido como pivô, o Quick Sort pode se degradar para O(n2) devido a partições desbalanceadas.
    - Elemento do Meio como Pivô: Escolher o elemento do meio tende a fornecer partições mais equilibradas, melhorando o desempenho para O(nlogn).
    
## Listas Completamente Desordenadas
    - Desempenho Geral: Para listas totalmente desordenadas, o Quick Sort geralmente se comporta bem, alcançando uma complexidade média de O(nlogn), especialmente quando o pivô é escolhido de maneira mais estratégica (como o elemento do meio ou usando uma técnica como a mediana de três).