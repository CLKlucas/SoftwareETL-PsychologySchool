from src.Conexão import sheet_con
from ETL import extract
from ETL import transform

conexao = sheet_con.connect_sheet()

dados_daily = extract.extrair_daily(conexao)

df = transform.transformar_daily(dados_daily)

print("Extração + transformação executadas com sucesso!")
print(f"Quantidade de registros: {len(df)}")
print("\nColunas:")
print(df.columns.tolist())
print("\nPrimeiras 10 linhas:")
print(df.head(10).to_string(index=False))