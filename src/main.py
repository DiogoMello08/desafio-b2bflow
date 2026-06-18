import logging

from src.database import get_contacts

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.getLogger("httpx").setLevel(logging.WARNING)


def run() -> None:
    logging.info("Iniciando aplicação")

    contacts = get_contacts()

    if not contacts:
        logging.warning("Nenhum contato encontrado no Supabase")
        return

    logging.info(f"{len(contacts)} contato(s) encontrado(s)")

    processed = 0

    for contact in contacts:

        name = contact.get("nome")
        phone = contact.get("telefone")

        if not name or not phone:
            logging.warning(
                f"Contato inválido encontrado: {contact}"
            )
            continue

        message = f"Olá, {name} tudo bem com você?"

        logging.info(
            f"Mensagem preparada para {name}: {message}"
        )

        processed += 1

    logging.info(
        f"Processamento finalizado. {processed} mensagem(ns) preparada(s)."
    )