import math

n = float(input("Digite um numero: "))

b = n
p = (b + (n / b)) / 2
diferenca = abs(n - (p * p))

while diferenca >= 0.0001:
    b = p
    p = (b + (n / b)) / 2
    diferenca = abs(n - (p * p))

print(f"Raiz quadrada aproximada (metodo de Newton): {p:.4f}")
print(f"Raiz quadrada usando math.sqrt(): {math.sqrt(n):.4f}")
