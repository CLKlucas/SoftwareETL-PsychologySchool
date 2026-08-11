from src.ETL import extracao
from src.Conexão import sheet_con

conexao = sheet_con.connect_sheet()

dados = extracao.extrair_daily(conexao)

print("Extração realizada com sucesso!")
print(f"Quantidade de linhas: {len(dados)}")

print("\nPrimeiras 5 linhas:")

for linha in dados[:5]:
    print(linha)