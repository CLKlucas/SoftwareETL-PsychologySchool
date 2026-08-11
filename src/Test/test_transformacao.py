from src.ETL import extracao
from src.ETL import transformacao
from src.Conexão import sheet_con

conexao = sheet_con.connect_sheet()
    
dados_daily = extracao.extrair_daily(conexao)

df = transformacao.transformar_daily(dados_daily)

print("Transformação realizada com sucesso!")

print("\nInformações do DataFrame:")
print(df.info())

print("\nPrimeiras 10 linhas:")
print(df.head(10).to_string(index=False))

print("\nColunas:")
print(df.columns.tolist())

print("\nQuantidade de linhas:")
print(len(df))