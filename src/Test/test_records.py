import pandas as pd

from src.Conexão import sheet_con
from src.ETL import extracao
from src.ETL import transformacao


conexao = sheet_con.connect_sheet()

dados_daily = extracao.extrair_daily(conexao)
dados_records = extracao.extrair_records(conexao)

df_daily = transformacao.transformar_daily(dados_daily)
df_records = transformacao.transformar_records(dados_records)


daily_total = (
    df_daily
    .groupby("dia", as_index=False)["quantidade"]
    .sum()
    .rename(columns={"quantidade": "quantidade_daily"})
)

records_total = (
    df_records[
        ["dia", "quantidade"]
    ]
    .rename(columns={"quantidade": "quantidade_records"})
)


comparacao = pd.merge(
    daily_total,
    records_total,
    on="dia",
    how="outer"
)

comparacao["quantidade_daily"] = (
    comparacao["quantidade_daily"]
    .fillna(0)
    .astype(int)
)

comparacao["quantidade_records"] = (
    comparacao["quantidade_records"]
    .fillna(0)
    .astype(int)
)

comparacao["igual"] = (
    comparacao["quantidade_daily"]
    == comparacao["quantidade_records"]
)


print("\nComparação entre daily e records:\n")
print(comparacao.to_string(index=False))


divergencias = comparacao[
    comparacao["igual"] == False
]


if len(divergencias) > 0:

    print("\nForam encontradas divergências:\n")
    print(
        divergencias[
            [
                "dia",
                "quantidade_daily",
                "quantidade_records",
                "igual"
            ]
        ].to_string(index=False)
    )

    print("\nDetalhamento das divergências:")

    for _, linha in divergencias.iterrows():

        dia = linha["dia"]

        print("\n" + "=" * 50)
        print(f"Dia: {dia.strftime('%d/%m/%Y')}")

        dados_dia = df_daily[
            df_daily["dia"] == dia
        ]

        print("\nDaily por horário:")

        print(
            dados_dia[
                ["horario", "quantidade"]
            ].to_string(index=False)
        )

        total_daily = dados_dia["quantidade"].sum()

        registros_dia = df_records[
            df_records["dia"] == dia
        ]

        if len(registros_dia) > 0:
            total_records = registros_dia[
                "quantidade"
            ].iloc[0]
        else:
            total_records = 0

        print(f"\nTotal Daily: {total_daily}")
        print(f"Total Records: {total_records}")
        print(
            f"Diferença: {total_daily - total_records}"
        )

    raise AssertionError(
        "Existem divergências entre daily e records."
    )

else:

    print(
        "\nTodos os registros de daily e records "
        "são consistentes!"
    )