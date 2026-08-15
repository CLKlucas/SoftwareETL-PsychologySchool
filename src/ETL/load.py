from src.Conexão import supabase_con as supabase


def carregar_dados(DataFrame):

    banco_conexao = supabase.conectar_supabase()

    dados = DataFrame[
        [
            "dia",
            "horario",
            "semana",
            "quantidade",
            "preenchido"
        ]
    ].copy()

    dados = dados.rename(
        columns={
            "dia": "Data",
            "horario": "Horario",
            "semana": "Semana",
            "quantidade": "Quantidade",
            "preenchido": "Preenchido"
        }
    )

    dados["Data"] = dados["Data"].dt.strftime("%Y-%m-%d")

    print("\nDados que serão enviados para o Supabase:")
    print(dados.to_string(index=False))

    registros = dados.to_dict(orient="records")

    try:
        resposta = (
        banco_conexao
        .table("atendimentos_teste")
        .upsert(
            registros,
            on_conflict="Data,Horario"
        )
        .execute()
    )

    except Exception as erro:
        print("\nERRO AO ENVIAR DADOS PARA O SUPABASE!")
        print(f"Detalhes do erro: {erro}")
        raise

    return resposta