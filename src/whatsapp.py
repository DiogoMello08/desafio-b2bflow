import logging
import requests

from src.config import (
    ZAPI_INSTANCE_ID,
    ZAPI_TOKEN
)


def send_message(phone: str, name: str) -> bool:
    url = (
        f"https://api.z-api.io/instances/"
        f"{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"
    )

    message = f"Olá, {name} tudo bem com você?"

    payload = {
        "phone": phone,
        "message": message
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=10
        )

        response.raise_for_status()

        logging.info(f"Mensagem enviada para {name}")
        return True

    except requests.exceptions.RequestException as error:
        logging.error(f"Erro ao enviar mensagem para {name}: {error}")
        return False