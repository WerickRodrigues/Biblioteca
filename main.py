from gerenciamento_livros import adicionar_livro, remover_livro, listar_livros, buscar_livro, buscar_favoritos

def menu():
    print("=== Sistema de Biblioteca ===")
    print("1. Adicionar Livro")
    print("2. Remover Livro")
    print("3. Listar Livros")
    print("4. Buscar Livro")
    print("5. Buscar Livros Favoritos")
    print("6. Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Gênero: ")
        favoritos = input("Favoritos (sim/não): ")
        adicionar_livro(titulo, autor, genero, favoritos)
    elif opcao == '2':
        titulo = input("Título do livro a remover: ")
        remover_livro(titulo)
    elif opcao == '3':
        listar_livros()
    elif opcao == '4':
        termo = input("Digite o título, autor, gênero ou favoritos para buscar: ")
        buscar_livro(termo)
    elif opcao == '5':
        termo = input("Digite o título, autor ou gênero para buscar nos favoritos: ")
        buscar_favoritos(termo)
    elif opcao == '6':
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")
