### Algoritmos de Ordenação Estáveis

## Merge Sort
    - Descrição: Este algoritmo divide a lista em sublistas, ordena cada uma e, em seguida, combina as sublistas de maneira ordenada.
    - Estabilidade: Merge Sort é estável porque, ao combinar sublistas, ele preserva a ordem relativa de elementos iguais.
    Exemplo:
    - Lista original: [(2, 'A'), (1, 'B'), (2, 'C'), (1, 'D')]
    - Ordenando por chave numérica: [(1, 'B'), (1, 'D'), (2, 'A'), (2, 'C')]
    - Observação: A ordem dos pares (2, 'A') e (2, 'C') é mantida.

## Bubble Sort
    - Descrição: Compara pares adjacentes e os troca se estiverem na ordem errada. Este processo é repetido até que a lista esteja ordenada.
    - Estabilidade: Bubble Sort é estável porque as trocas ocorrem apenas entre elementos adjacentes.
    Exemplo:
    - Lista original: [(4, 'A'), (3, 'B'), (4, 'C'), (2, 'D')]
    - Ordenando por chave numérica: [(2, 'D'), (3, 'B'), (4, 'A'), (4, 'C')]
    - Observação: A ordem dos pares (4, 'A') e (4, 'C') é mantida.

## Insertion Sort
    - Descrição: Constrói a lista ordenada um item de cada vez, movendo cada novo item para sua posição correta.
    - Estabilidade: Insertion Sort é estável porque os elementos iguais não são trocados de ordem.
    Exemplo:
    - Lista original: [(5, 'A'), (3, 'B'), (5, 'C'), (2, 'D')]
    - Ordenando por chave numérica: [(2, 'D'), (3, 'B'), (5, 'A'), (5, 'C')]
    - Observação: A ordem dos pares (5, 'A') e (5, 'C') é mantida.

### Algoritmos de Ordenação Instáveis

## Quick Sort
    - Descrição: Utiliza um pivô para dividir a lista em partes menores, ordenando recursivamente estas partes.
    - Instabilidade: Quick Sort não é estável porque pode trocar a ordem relativa de elementos iguais.
    Exemplo:
    - Lista original: [(3, 'A'), (2, 'B'), (3, 'C'), (1, 'D')]
    - Ordenando por chave numérica: [(1, 'D'), (2, 'B'), (3, 'C'), (3, 'A')]
    - Observação: A ordem dos pares (3, 'A') e (3, 'C') pode ser alterada.

### Significado da Estabilidade
    - Importância: A estabilidade é importante em situações onde a preservação da ordem original dos dados é necessária, como em ordenações múltiplas (por exemplo, ordenar por nome e depois por data de nascimento).
    - Impacto: Em estruturas de dados complexas, onde cada elemento tem várias chaves, a estabilidade permite que a ordem de uma chave secundária seja mantida ao ordenar por uma chave primária.