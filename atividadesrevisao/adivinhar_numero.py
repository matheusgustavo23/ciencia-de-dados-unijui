import random

ARQUIVO = "historico_adivinhacao.txt"

def main():
    historico = []

    while True:
        numero = random.randint(0, 15)
        tentativas = 0

        while True:
            palpite = int(input("Adivinhe o numero (0 a 15): "))
            tentativas += 1
            if palpite == numero:
                print(f"Acertou em {tentativas} tentativa(s)!")
                break
            print("Maior..." if palpite < numero else "Menor...")

        with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Numero: {numero}, acertou em {tentativas} tentativas\n")
        historico.append((numero, tentativas))

        if input("Jogar de novo? (s/n): ").strip().lower() != "s":
            break

    print("\nHISTORICO DE JOGADAS: ")
    for i, (numero, tentativas) in enumerate(historico, start=1):
        print(f"Rodada {i}: numero {numero} em {tentativas} tentativa(s)")

main()
