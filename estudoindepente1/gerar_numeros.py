import random
import json
import csv
import os

DIRETORIO_SAIDA = "/home/mthz/Downloads/"

os.makedirs(DIRETORIO_SAIDA, exist_ok=True)

random.seed()
numeros = [random.randint(1, 100) for _ in range(20)]

dados = []
for n in numeros:
    dados.append({
        "valor_original": n,
        "valor_x2": n * 2,
        "valor_x10": n * 10
    })

with open(os.path.join(DIRETORIO_SAIDA, "numeros.txt"), "w", encoding="utf-8") as f:
    f.write(f"{'Valor Original':<20}{'Valor x2':<20}{'Valor x10':<20}\n")
    f.write("-" * 60 + "\n")
    for d in dados:
        f.write(f"{d['valor_original']:<20}{d['valor_x2']:<20}{d['valor_x10']:<20}\n")

with open(os.path.join(DIRETORIO_SAIDA, "numeros.json"), "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)

with open(os.path.join(DIRETORIO_SAIDA, "numeros.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["valor_original", "valor_x2", "valor_x10"])
    writer.writeheader()
    writer.writerows(dados)

print(f"Arquivos gerados com sucesso em: {DIRETORIO_SAIDA}")
for d in dados:
    print(d)
