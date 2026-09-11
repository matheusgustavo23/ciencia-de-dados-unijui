num = int(input("Digite um numero: "))

primo = True

if num == 0 or num == 1:

    primo = False
elif num == 2:
    primo = True
elif num % 2 == 0:
    primo = False
else:
    i = 3
    while i <= num // 2:
        if num % i == 0:
            primo = False
            break
        i += 2

if primo:
    print(f"{num} eh primo.")
else:
    print(f"{num} nao eh primo.")
