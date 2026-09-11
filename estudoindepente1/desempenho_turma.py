def solicitar_notas(quantidade):
    notas = []
    for i in range(quantidade):
        while True:
            try:
                nota = float(input(f"Digite a nota do estudante {i + 1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10, digite novamente.")
            except ValueError:
                print("Entrada invalida, digite um numero.")
    return notas

def maior_nota(notas):
    return max(notas)

def menor_nota(notas):
    return min(notas)

def media(notas):
    return sum(notas) / len(notas)

def contar_aprovados(notas, media_aprovacao=6.0):
    return sum(1 for nota in notas if nota >= media_aprovacao)

def contar_reprovados(notas, media_aprovacao = 6):
    return sum(1 for nota in notas if nota < media_aprovacao)

def resultados(notas):
    print("DESEMPENHO DA TURMA: ")
    print(f"Registro de notas: {notas}")
    print(f"Maior nota: {maior_nota(notas):.2f}")
    print(f"Menor nota: {menor_nota(notas):.2f}")
    print(f"Média da turma: {media(notas):.2f}")
    print(f"Aprovados: {contar_aprovados(notas)}")
    print(f"Reprovados: {contar_reprovados(notas)}")

def main():
    while True:
        try:
            quantidade = int(input("Digite a quantidade de alunos: "))
            if quantidade > 0:
                break
            else:
                print("Deve ser maior que zero")
        except ValueError:
            print("Entrada invalida, digite um número inteiro!")

    notas = solicitar_notas(quantidade)
    resultados(notas)

    main()
