import pandas as pd

meses = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# dados ficticios de algumas cidades do RS, cada uma com seu perfil de clima
cidades_dados = {
    "Santa Rosa": {
        "temperatura": [25.5, 25.0, 23.0, 19.5, 16.0, 13.5, 12.5, 14.0, 16.5, 19.5, 22.0, 24.5],
        "precipitacao": [150, 140, 145, 130, 140, 125, 120, 130, 160, 165, 150, 155],
        "evapotranspiracao": [130, 115, 100, 75, 55, 40, 42, 50, 65, 85, 105, 120],
    },
    "Porto Alegre": {
        "temperatura": [26.5, 26.5, 24.5, 21.0, 18.0, 15.5, 14.5, 15.5, 17.5, 20.5, 23.0, 25.5],
        "precipitacao": [120, 110, 115, 100, 95, 110, 130, 120, 130, 140, 110, 115],
        "evapotranspiracao": [140, 125, 105, 80, 60, 45, 45, 55, 70, 90, 110, 130],
    },
    "Caxias do Sul": {
        "temperatura": [22.0, 22.0, 20.5, 17.0, 13.5, 10.5, 10.0, 11.5, 13.5, 16.5, 19.0, 21.0],
        "precipitacao": [160, 150, 155, 140, 150, 140, 135, 145, 170, 175, 160, 165],
        "evapotranspiracao": [110, 95, 80, 60, 40, 28, 30, 38, 50, 70, 90, 105],
    },
    "Santa Maria": {
        "temperatura": [26.0, 25.5, 23.5, 20.0, 16.5, 14.0, 13.0, 14.5, 17.0, 20.0, 22.5, 25.0],
        "precipitacao": [145, 135, 140, 125, 135, 130, 125, 135, 155, 160, 145, 150],
        "evapotranspiracao": [135, 120, 105, 80, 58, 42, 44, 52, 68, 88, 108, 125],
    },
    "Uruguaiana": {
        "temperatura": [28.0, 27.5, 25.0, 21.0, 17.0, 14.0, 13.0, 15.0, 18.0, 21.5, 24.5, 27.0],
        "precipitacao": [130, 120, 125, 110, 115, 105, 100, 110, 130, 140, 125, 130],
        "evapotranspiracao": [150, 135, 115, 85, 60, 42, 44, 55, 75, 100, 125, 145],
    },
}

# montando o dataframe geral, juntando as cidades uma embaixo da outra
df = pd.concat(
    [pd.DataFrame({"cidade": cidade, "mes": meses, **valores}) for cidade, valores in cidades_dados.items()],
    ignore_index=True,
)

# localizando so a cidade de SR dentro da base geral
santa_rosa = df.loc[df["cidade"] == "Santa Rosa"].copy()

# mostrando o dataframe ja filtrado
print(santa_rosa)

# achando o mes mais frio com idxmin
mes_mais_frio = santa_rosa.loc[santa_rosa["temperatura"].idxmin(), "mes"]

# deficit hidrico e a chuva menos a evapotranspiracao, quanto menor pior
santa_rosa["deficit_hidrico"] = santa_rosa["precipitacao"] - santa_rosa["evapotranspiracao"]
mes_maior_deficit = santa_rosa.loc[santa_rosa["deficit_hidrico"].idxmin(), "mes"]

# marcando a estacao de cada mes e tirando a media de temperatura por estacao
estacoes = {
    "Dezembro": "Verao", "Janeiro": "Verao", "Fevereiro": "Verao",
    "Marco": "Outono", "Abril": "Outono", "Maio": "Outono",
    "Junho": "Inverno", "Julho": "Inverno", "Agosto": "Inverno",
    "Setembro": "Primavera", "Outubro": "Primavera", "Novembro": "Primavera",
}
santa_rosa["estacao"] = santa_rosa["mes"].map(estacoes)
media_por_estacao = santa_rosa.groupby("estacao")["temperatura"].mean()

# respostas
print("Mes mais frio:", mes_mais_frio)
print("Mes com maior deficit hidrico:", mes_maior_deficit)
print("Media de temperatura por estacao:")
print(media_por_estacao)
