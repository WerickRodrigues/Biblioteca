import json

# puxar livro
def carregar_livros():
    try:
        with open('livros.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Salvar livros 
def salvar_livros(livros):
    with open('livros.json', 'w') as file:
        json.dump(livros, file, indent=4)

# Carregar livros favoritos 
def carregar_favoritos():
    try:
        with open('favoritos.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Salvar livros favoritos
def salvar_favoritos(favoritos):
    with open('favoritos.json', 'w') as file:
        json.dump(favoritos, file, indent=4)

# colocar um livro
def adicionar_livro(titulo, autor, genero, favoritos):
    livros = carregar_livros()
    livro = {"titulo": titulo, "autor": autor, "genero": genero, "favoritos": favoritos}
    livros.append(livro)
    salvar_livros(livros)

    if favoritos.lower() == 'sim':
        favoritos = carregar_favoritos()
        favoritos.append(livro)
        salvar_favoritos(favoritos)

    print(f"Livro '{titulo}' adicionado com sucesso!")

# apagar um livro
def remover_livro(titulo):
    livros = carregar_livros()
    livros = [livro for livro in livros if livro['titulo'] != titulo]
    salvar_livros(livros)
    print(f"Livro com título '{titulo}' removido com sucesso!")

# mostrar todos os livros
def listar_livros():
    livros = carregar_livros()
    if not livros:
        print("Nenhum livro encontrado.")
        return
    for livro in livros:
        print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Gênero: {livro['genero']}, Favoritos: {livro['favoritos']}")

# Buscar um livro 
def buscar_livro(termo):
    livros = carregar_livros()
    resultados = [livro for livro in livros if termo.lower() in livro['titulo'].lower() or termo.lower() in livro['autor'].lower() or termo.lower() in livro['genero'].lower() or termo.lower() in livro['favoritos'].lower()]
    if not resultados:
        print("Nenhum livro encontrado.")
        return
    for livro in resultados:
        print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Gênero: {livro['genero']}, Favoritos: {livro['favoritos']}")

# Buscar os livros favoritos
def buscar_favoritos(termo):
    favoritos = carregar_favoritos()
    resultados = [livro for livro in favoritos if termo.lower() in livro['titulo'].lower() or termo.lower() in livro['autor'].lower() or termo.lower() in livro['genero'].lower()]
    if not resultados:
        print("Nenhum livro favorito encontrado.")
        return
    for livro in resultados:
        print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Gênero: {livro['genero']}, Favoritos: {livro['favoritos']}")
