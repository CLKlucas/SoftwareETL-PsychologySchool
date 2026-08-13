from ETL import extract
from src.Conexão import sheet_con

conexao = sheet_con.connect_sheet()

dados = extract.extrair_daily(conexao)

print("Extração realizada com sucesso!")
print(f"Quantidade de linhas: {len(dados)}")

print("\nPrimeiras 5 linhas:")

for linha in dados[:5]:
    print(linha)