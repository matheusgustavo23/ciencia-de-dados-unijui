produtos = {}

def cadastrar_produto():
    codigo = input("Código do produto: ").strip()

    if codigo in produtos:
        print(f"Já existe um produto cadastrado com o código '{codigo}'.\n")
        return

    nome = input("Nome do produto: ").strip()

    try:
        preco = float(input("Preço unitário (R$): ").replace(",", "."))
        quantidade = int(input("Quantidade em estoque: "))
    except ValueError:
        print("Preço ou quantidade inválidos. Cadastro cancelado.\n")
        return

    produtos[codigo] = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    print(f"Produto '{nome}' cadastrado com sucesso!\n")

def consultar_produto():
    codigo = input("Digite o código do produto: ").strip()

    produto = produtos.get(codigo)

    if produto is None:
        print(f"Nenhum produto encontrado com o código '{codigo}'.\n")
        return

    print("\n--- Dados do Produto ---")
    print(f"Código:     {codigo}")
    print(f"Nome:       {produto['nome']}")
    print(f"Preço:      R$ {produto['preco']:.2f}")
    print(f"Quantidade: {produto['quantidade']}")
    print(f"Subtotal:   R$ {produto['preco'] * produto['quantidade']:.2f}\n")

def calcular_valor_total_estoque():
    if not produtos:
        print("Nenhum produto cadastrado.\n")
        return

    total = sum(p["preco"] * p["quantidade"] for p in produtos.values())
    print(f"Valor total do estoque: R$ {total:.2f}\n")

def produto_maior_valor_unitario():
    if not produtos:
        print("Nenhum produto cadastrado.\n")
        return

    codigo_maior = max(produtos, key=lambda c: produtos[c]["preco"])
    produto = produtos[codigo_maior]

    print("\n--- Produto de Maior Valor Unitário ---")
    print(f"Código: {codigo_maior}")
    print(f"Nome:   {produto['nome']}")
    print(f"Preço:  R$ {produto['preco']:.2f}\n")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.\n")
        return

    print("\n--- Produtos Cadastrados ---")
    for codigo, dados in produtos.items():
        print(f"{codigo} | {dados['nome']} | R$ {dados['preco']:.2f} | Qtd: {dados['quantidade']}")
    print()

def exibir_menu():
    print("===== MENU =====")
    print("1 - Cadastrar produto")
    print("2 - Consultar produto pelo código")
    print("3 - Calcular valor total do estoque")
    print("4 - Produto de maior valor unitário")
    print("5 - Listar todos os produtos")
    print("0 - Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        print()

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            consultar_produto()
        elif opcao == "3":
            calcular_valor_total_estoque()
        elif opcao == "4":
            produto_maior_valor_unitario()
        elif opcao == "5":
            listar_produtos()
        elif opcao == "0":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

main()
