### Por que a Lista Deve Estar Ordenada?
- A lista deve estar ordenada para que o Binary Search funcione corretamente, pois o algoritmo se baseia na propriedade de ordenação para decidir se deve continuar a busca na metade esquerda ou direita da lista. Se a lista não estiver ordenada, não há garantia de que o elemento alvo estará na metade esperada, tornando o algoritmo ineficaz.

## Exemplos

# Lista Ordenada:
- Lista: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
- Alvo: 7
- Passos do Binary Search:

    - Meio inicial: 9 (índice 4), 7 é menor que 9, busca continua na metade esquerda.
    - Novo meio: 5 (índice 2), 7 é maior que 5, busca continua na metade direita.
    - Novo meio: 7 (índice 3), elemento encontrado.

# Lista Não Ordenada:
- Lista: [11, 3, 7, 1, 9, 5, 13, 19, 17, 15]
- Alvo: 11
- Passos do Binary Search:
    - Meio inicial: 9 (índice 4), 11 é maior que 9, busca continua na metade direita.
    - Novo meio: 19 (índice 7), 11 é menor que 19, busca continua na metade esquerda.
    - Novo meio: 5 (índice 5), 11 é maior que 5, busca continua na metade direita.
    - Tentativa de aplicar Binary Search falha, pois a divisão em metades não garante a localização correta e o elemento 11 não é encontrado, embora esteja presente na lista.