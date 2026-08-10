from src.Conexão import sheet_con

def extrair_daily(conexão):
    daily = conexão.worksheet("daily")
    dados_daily = daily.get_all_values()
    return dados_daily

def extrair_records(conexão):
    records = conexão.worksheet("records")
    records_dados = records.get_all_values()
    return records_dados