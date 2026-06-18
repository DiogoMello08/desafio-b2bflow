import logging

from src.database import get_contacts
from src.whatsapp import send_message

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
            logging.warning(f"Contato inválido encontrado: {contact}")
            continue

        success = send_message(phone, name)

        if success:
            processed += 1

    logging.info(
        f"Processamento finalizado. {processed} mensagem(ns) enviada(s)."
    )


if __name__ == "__main__":
    run()