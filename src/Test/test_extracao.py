from src.ETL import extracao


dados = extracao.extrair_daily()

print("Extração realizada com sucesso!")
print(f"Quantidade de linhas: {len(dados)}")

print("\nPrimeiras 5 linhas:")

for linha in dados[:5]:
    print(linha)