import pandas as pd


def transformar_daily(dados_daily):

    cabecalho = dados_daily[1]

    dados = dados_daily[2:]

    df = pd.DataFrame(dados, columns=cabecalho)

    colunas = []
    semana_encontrada = False

    for coluna in df.columns:

        if coluna == "semana":

            if not semana_encontrada:
                colunas.append("semana")
                semana_encontrada = True
            else:
                colunas.append("semana_duplicada")

        elif coluna == "":
            colunas.append("ignorar")

        else:
            colunas.append(coluna)

    df.columns = colunas

    df = df.drop(
        columns=["semana_duplicada", "ignorar"],
        errors="ignore"
    )

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

    if df.empty:
        return pd.DataFrame(
        columns=[
            "dia",
            "ano",
            "semana",
            "horario",
            "quantidade",
            "preenchido"
        ]
    )

    df = df.melt(
        id_vars=["semana", "dia"],
        value_vars=horarios,
        var_name="horario",
        value_name="quantidade"
    )

    df["preenchido"] = (
        df["quantidade"]
        .notna()
        & (df["quantidade"].astype(str).str.strip() != "")
    )

    df["semana"] = pd.to_numeric(
        df["semana"],
        errors="coerce"
    ).fillna(0).astype(int)

    df["quantidade"] = pd.to_numeric(
        df["quantidade"],
        errors="coerce"
    ).fillna(0).astype(int)

    if (df["quantidade"] < 0).any():
        raise ValueError(
            "Foram encontrados valores negativos na coluna 'quantidade'."
        )

    df["dia"] = pd.to_datetime(
        df["dia"],
        dayfirst=True,
        errors="coerce"
    )

    df = df.dropna(subset=["dia"])

    df["ano"] = df["dia"].dt.year.astype(int)

    df = df[
        [
            "dia",
            "ano",
            "semana",
            "horario",
            "quantidade",
            "preenchido"
        ]
    ]

    return df