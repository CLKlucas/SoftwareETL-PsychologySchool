from src.Conexão import sheet_con

def extrair_daily(conexão):
    daily = conexão.worksheet("daily")
    dados_daily = daily.get_all_values()
    return dados_daily

