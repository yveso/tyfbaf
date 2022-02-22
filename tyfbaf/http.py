from tkinter.messagebox import NO
from typing import Any
import requests

SERVER_NAME = None
PORT = 6405
BASE_HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}
PROXIES = {"http": None, "https": None}


def _setup(server_name: str, port: int = 6405) -> None:
    global SERVER_NAME, PORT
    SERVER_NAME = server_name
    PORT = port


def post(endpoint: str, *, body=None, token=None) -> dict[str, Any]:
    response = requests.post(
        f"http://{SERVER_NAME}:{PORT}/biprws{endpoint}",
        proxies=PROXIES,
        headers=(
            {"X-SAP-LogonToken": token, **BASE_HEADERS} if token else BASE_HEADERS
        ),
        json=body,
    )
    return response.json() if response.text else {}
