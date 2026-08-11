from src.Conexão import supabase_con


supabase = supabase_con.conectar_supabase()

resposta = (
    supabase
    .table("atendimentos")
    .select("*")
    .limit(1)
    .execute()
)

print("Conexão com Supabase realizada com sucesso.")
print(resposta.data)