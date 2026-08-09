import pandas as pd


def transformar_daily(dados_daily):

    cabecalho = dados_daily[1]
    
    dados = dados_daily[2:]

    df = pd.DataFrame(dados, columns=cabecalho)

    colunas = []
    contador_semana = 0

    for coluna in df.columns:

        if coluna == "semana":
            contador_semana += 1

            if contador_semana == 1:
                colunas.append("semana")

            else:
                colunas.append("semana_2")

        elif coluna == "":
            colunas.append("ignorar")

        else:
            colunas.append(coluna)

    df.columns = colunas

    df = df.drop(columns=["ignorar"], errors="ignore")

    horarios = [
        "8h00",
        "9h00",
        "10h00",
        "11h00",
        "12h00",
        "13h00",
        "14h00",
        "15h00",
        "16h00",
        "17h00",
        "18h00",
        "19h00"
    ]

    df = df.melt(
        id_vars=["mês", "semana", "semana_2", "dia"],
        value_vars=horarios,
        var_name="horario",
        value_name="quantidade"
    )

    df["quantidade"] = pd.to_numeric(
        df["quantidade"],
        errors="coerce"
    ).fillna(0)

    df["dia"] = pd.to_datetime(
        df["dia"],
        dayfirst=True,
        errors="coerce"
    )

    return df