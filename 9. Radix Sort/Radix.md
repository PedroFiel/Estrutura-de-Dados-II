## Como o Radix Sort Lida com Diferentes Bases
**Base 10 (Decimal)**
*Dígitos Decimais:* Em base 10, cada número é composto por dígitos de 0 a 9. O processo do Radix Sort envolve a ordenação desses números com base em cada posição decimal (unidades, dezenas, centenas, etc.).

# Processamento de Dígitos:
*Counting Sort:* É utilizado para ordenar os números com base em cada dígito. Para a base 10, o Counting Sort precisa de um array de contagem com 10 posições (uma para cada possível valor de dígito de 0 a 9).
Iteração sobre Dígitos: O algoritmo começa com o dígito menos significativo (unidade) e avança até o dígito mais significativo.
*Ordem Estável:* A estabilidade do Counting Sort garante que números com dígitos iguais na posição atual mantenham sua ordem relativa original.

**Base 2 (Binária)**
*Bits Binários:* Em base 2, cada número é composto de bits, que podem ser 0 ou 1. O tratamento dos bits é semelhante ao dos dígitos na base 10, mas com apenas duas possibilidades para cada posição.

# Processamento de Bits:
*Counting Sort Adaptado:* Para a base 2, o Counting Sort usa um array de contagem com apenas 2 posições (uma para 0 e outra para 1).
Iteração sobre Bits: O algoritmo processa cada bit, começando do menos significativo (LSB - Least Significant Bit) até o mais significativo (MSB - Most Significant Bit).
*Eficiência em Dados Binários:* Como a base é pequena (apenas 2), o Radix Sort pode ser muito eficiente para números que naturalmente se alinham a representações binárias, como endereços IP ou dados de rede.