from src.Conexão import sheet_con

conexão = sheet_con.connect_sheet()

def extrair_daily():
    daily = conexão.worksheet("daily")
    dados_daily = daily.get_all_values()
    return dados_daily

def extrair_records():
    records = conexão.worksheet("records")
    records_dados = records.get_all_values()
    return records_dados