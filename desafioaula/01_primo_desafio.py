def eh_primo(num):
    if num == 0 or num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    i = 3
    while i <= num // 2:
        if num % i == 0:
            return False
        i += 2
    return True

qtd = int(input("Quantos numeros primos deseja listar? "))

contador = 0
num = 2
primos = []

while contador < qtd:
    if eh_primo(num):
        primos.append(num)
        contador += 1
    num += 1

print(f"Primeiros {qtd} numeros primos:")
print(*primos)
