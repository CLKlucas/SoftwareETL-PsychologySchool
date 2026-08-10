from src.Conexão import sheet_con
from src.ETL import extracao
from src.ETL import transformacao


conexao = sheet_con.connect_sheet()

dados_records = extracao.extrair_records(conexao)

df = transformacao.transformar_records(dados_records)

print("Extração + transformação da records executadas com sucesso!")
print(f"Quantidade de registros: {len(df)}")

print("\nColunas:")
print(df.columns.tolist())

print("\nPrimeiras 10 linhas:")
print(df.head(10).to_string(index=False))