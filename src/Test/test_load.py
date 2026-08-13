from src.Conexão import sheet_con
from src.ETL import extracao
from src.ETL import transformacao
from src.ETL import carregar


conexao = sheet_con.connect_sheet()

dados_daily = extracao.extrair_daily(conexao)

df = transformacao.transformar_daily(dados_daily)

df_teste = df.head(2)

print("Dados que serão enviados:")
print(df_teste)

resposta = carregar.carregar_dados(df_teste)

print("Carga de teste realizada com sucesso.")
print(resposta.data)