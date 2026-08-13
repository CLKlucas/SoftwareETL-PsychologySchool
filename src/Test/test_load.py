from src.Conexão import sheet_con
from ETL import extract
from ETL import transform
from ETL import load


conexao = sheet_con.connect_sheet()

dados_daily = extract.extrair_daily(conexao)

df = transform.transformar_daily(dados_daily)

df_teste = df.head(2)

print("Dados que serão enviados:")
print(df_teste)

resposta = load.carregar_dados(df_teste)

print("Carga de teste realizada com sucesso.")
print(resposta.data)