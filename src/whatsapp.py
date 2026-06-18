import requests

from src.config import (
    ZAPI_INSTANCE_ID,
    ZAPI_TOKEN
)

def send_message(phone, name):

    url = (
        f"https://api.z-api.io/"
        f"instances/{ZAPI_INSTANCE_ID}"
        f"/token/{ZAPI_TOKEN}"
        f"/send-text"
    )

    payload = {
        "phone": phone,
        "message": f"Olá, {name} tudo bem com você?"
    }

    try:

        response = requests.post(
            url,
            json=payload,
            timeout=10
        )

        response.raise_for_status()

        print(
            f"Mensagem enviada para {name}"
        )

    except Exception as error:

        print(
            f"Erro ao enviar para "
            f"{name}: {error}"
        )