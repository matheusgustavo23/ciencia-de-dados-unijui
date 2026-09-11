import csv

ARQUIVO = "lista_compras.csv"

def main():
    itens = []

    while True:
        nome = input("Nome do item (aperte a tecla ENTER para encerrar): ").strip()
        if not nome:
            break
        quantidade = int(input("Quantidade: "))
        valor = float(input("Valor unitario: "))
        itens.append((nome, quantidade, valor))

    total = sum(quantidade * valor for _, quantidade, valor in itens)

    print("\nLISTA DE COMPRAS: ")
    for nome, quantidade, valor in itens:
        print(f"{nome}: {quantidade} x R${valor:.2f} = R${quantidade * valor:.2f}")
    print(f"TOTAL: R${total:.2f}")

    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["item", "quantidade", "valor_unitario", "subtotal"])
        for nome, quantidade, valor in itens:
            escritor.writerow([nome, quantidade, f"{valor:.2f}", f"{quantidade * valor:.2f}"])
        escritor.writerow(["", "", "TOTAL", f"{total:.2f}"])

    print(f"\nLista salva em {ARQUIVO}")
main()
