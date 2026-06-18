import logging
from supabase import create_client

from src.config import (
    SUPABASE_URL,
    SUPABASE_KEY
)

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


def get_contacts(limit: int = 3) -> list:
    try:
        response = (
            supabase
            .table("contatos")
            .select("*")
            .limit(limit)
            .execute()
        )

        return response.data

    except Exception as error:
        logging.error(f"Erro ao buscar contatos: {error}")
        return []