from src.Conexão import sheet_con as sheet_auth
from src.ETL import extract
from src.ETL import transform
from src.ETL import load

def main():
    conexao = sheet_auth.connect_sheet()

    dados_planilha = extract.extrair_daily(conexao)
    DF_dados = transform.transformar_daily(dados_planilha)
    load_banco = load.carregar_dados(DF_dados)


if __name__ == "__main__":
    print("Iniciando o processo de ETL...")
    main()