### Binary Search
Complexidade de Tempo: O(log n)
O algoritmo divide repetidamente o espaço de busca ao meio, o que resulta em uma complexidade logarítmica.
Complexidade de Espaço: O(1)
Utiliza espaço constante, pois a busca é feita in-place sem necessidade de armazenamento adicional.
Requisitos: Os dados devem estar previamente ordenados.

### Interpolation Search
Complexidade de Tempo: O(log log n) no melhor caso, O(n) no pior caso
A complexidade melhora quando os valores são uniformemente distribuídos, mas pode se degradar linearmente em dados não uniformes.
Complexidade de Espaço: O(1)
Também é feita in-place, sem necessidade de espaço extra.
Requisitos: Os dados devem estar ordenados e idealmente uniformemente distribuídos.

### Jump Search
Complexidade de Tempo: O(√n)
Este algoritmo pula blocos de elementos de tamanho fixo e realiza uma busca linear dentro do bloco.
Complexidade de Espaço: O(1)
Assim como os outros métodos de busca, é feito in-place.
Requisitos: Os dados devem estar ordenados.

### Ternary Search
Complexidade de Tempo: O(log3 n)
Divide o espaço de busca em três partes, em vez de duas como no Binary Search.
Complexidade de Espaço: O(1)
Não requer espaço adicional significativo.
Requisitos: Os dados devem estar ordenados.

#### Algoritmos de Ordenação

### Merge Sort
Complexidade de Tempo: O(n log n)
É um algoritmo baseado na técnica de dividir e conquistar, que é eficiente e estável.
Complexidade de Espaço: O(n)
Requer espaço adicional para armazenar elementos durante o processo de mesclagem.

### Selection Sort
Complexidade de Tempo: O(n²)
É um algoritmo simples que tem um desempenho ruim em grandes listas devido à sua complexidade quadrática.
Complexidade de Espaço: O(1)
Não utiliza espaço adicional significativo além do necessário para a lista original.

### Bucket Sort
Complexidade de Tempo: O(n + k)
Depende da distribuição dos elementos. k é o número de buckets.
Complexidade de Espaço: O(n + k)
Requer espaço adicional para os buckets.
Requisitos: Funciona bem quando os dados são uniformemente distribuídos em um intervalo.

### Radix Sort
Complexidade de Tempo: O(nk)
n é o número de elementos e k é o número de dígitos nos números.
Complexidade de Espaço: O(n + k)
Precisa de espaço adicional para armazenar contagens ou saídas intermediárias.
Requisitos: É eficiente para ordenar números inteiros ou strings com comprimento fixo.

### Quick Sort
Complexidade de Tempo: O(n log n) no melhor e médio caso, O(n²) no pior caso
O pior caso ocorre quando os pivôs são escolhidos de forma subótima, mas isso pode ser mitigado com técnicas de escolha de pivô.
Complexidade de Espaço: O(log n)
Utiliza espaço na pilha para chamadas recursivas, mas é in-place no que diz respeito ao armazenamento dos elementos.

