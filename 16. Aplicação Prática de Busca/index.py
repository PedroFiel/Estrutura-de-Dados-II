def binary_search_isbn(livros, isbn_procurado):
    low = 0
    high = len(livros) - 1

    while low <= high:
        mid = (low + high) // 2
        isbn_atual = livros[mid]["isbn"]

        if isbn_atual < isbn_procurado:
            low = mid + 1
        elif isbn_atual > isbn_procurado:
            high = mid - 1
        else:
            return mid  

    return -1 

livros = [
    {"isbn": "978-3-16-148410-0", "titulo": "Livro A", "autor": "Autor A"},
    {"isbn": "978-1-23-456789-0", "titulo": "Livro B", "autor": "Autor B"},
    {"isbn": "978-0-12-345678-9", "titulo": "Livro C", "autor": "Autor C"}
]

livros_ordenados = sorted(livros, key=lambda x: x["isbn"])
isbn_a_procurar = "978-1-23-456789-0"
indice = binary_search_isbn(livros_ordenados, isbn_a_procurar)

if indice != -1:
    livro_encontrado = livros_ordenados[indice]
    print(f"Livro encontrado: {livro_encontrado['titulo']} por {livro_encontrado['autor']}")
else:
    print("Livro não encontrado.")