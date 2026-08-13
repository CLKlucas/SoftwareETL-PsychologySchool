from src.Conexão import supabase_con as supabase


def carregar_dados(DataFrame):
    banco_conexao = supabase.conectar_supabase()

    dados = DataFrame[
        [
            "dia",
            "horario",
            "semana",   
            "quantidade"
        ]       
    ].copy()

    dados = dados.rename(
        columns={
            "dia": "Data",
            "horario": "Horario",
            "semana": "Semana",
            "quantidade": "Quantidade"
        }
    )

    dados["Data"] = dados["Data"].dt.strftime("%Y-%m-%d")

    registros = dados.to_dict(orient="records")

    resposta = (
        banco_conexao
        .table("atendimentos")
        .upsert(
            registros,
            on_conflict="Data,Horario"
        )
        .execute()
    )

    return resposta
