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

records_total = df_records[
    ["dia", "quantidade"]
].rename(
    columns={"quantidade": "quantidade_records"}
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

print("Comparação entre daily e records:")
print(comparacao.to_string(index=False))

divergencias = comparacao[
    comparacao["igual"] == False
]

if len(divergencias) > 0:
    print("\nForam encontradas divergências:")
    print(divergencias.to_string(index=False))
    raise AssertionError("Existem divergências entre daily e records.")

print("\nTodos os registros de daily e records são consistentes!")