import os
from supabase import create_client


def conectar_supabase():
    url = os.getenv("URL_SUPABASE")
    key = os.getenv("KEY_SUPABASE")

    if not url or not key:
        raise ValueError("Credenciais do Supabase não encontradas.")

    supabase = create_client(url, key)

    return supabase