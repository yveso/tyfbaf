from typing import Any, Optional
import httpx

SERVER_NAME = None
PORT = 6405
BASE_HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}


def _setup(server_name: str, port: int = 6405) -> None:
    """Private function to setup tyfbaf. You should use the public one from the tyfbaf module.

    Args:
        server_name (str): Just your server name, without any protocol or port.
        port (int, optional): The port in use of your server. Defaults to 6405.
    """
    global SERVER_NAME, PORT
    SERVER_NAME = server_name
    PORT = port


def get(endpoint: str, *, token: Optional[str] = None) -> dict[str, Any]:
    """Function to make http get requests easier.

    Args:
        endpoint (str): The endpoint to your desired API, for example "/raylight/v1/documents".
        token (Optional[str], optional): Your token. Defaults to None.

    Returns:
        dict[str, Any]: The response of the HTTP get request.
    """
    response = httpx.get(
        f"http://{SERVER_NAME}:{PORT}/biprws{endpoint}",
        headers=(
            {"X-SAP-LogonToken": token, **BASE_HEADERS} if token else BASE_HEADERS
        ),
        timeout=None,
    )
    return response.json() if response.text else {}


def post(
    endpoint: str, *, body: Optional[dict] = None, token: Optional[str] = None
) -> dict[str, Any]:
    """Function to make http post requests easier.

    Args:
        endpoint (str): The endpoint to your desired API, for example "/raylight/v1/documents".
        body (Optional[dict], optional): The body of the HTTP post request. Defaults to None.
        token (Optional[str], optional): Your token. Defaults to None.

    Returns:
        dict[str, Any]: The response of the HTTP post request.
    """
    response = httpx.post(
        f"http://{SERVER_NAME}:{PORT}/biprws{endpoint}",
        headers=(
            {"X-SAP-LogonToken": token, **BASE_HEADERS} if token else BASE_HEADERS
        ),
        json=body,
        timeout=None,
    )
    return response.json() if response.text else {}


def post_full_uri(
    uri: str, *, body: Optional[dict] = None, token: Optional[str] = None
) -> dict[str, Any]:
    """Function to make http post requests easier.
    This function takes a full URI (that you maybe got from another response) as parameter.

    Args:
        uri (str): The full uri to your desired API.
        body (Optional[dict], optional): The body of the HTTP post request. Defaults to None.
        token (Optional[str], optional): Your token. Defaults to None.

    Returns:
        dict[str, Any]: The response of the HTTP post request.
    """
    response = httpx.post(
        uri,
        headers=(
            {"X-SAP-LogonToken": token, **BASE_HEADERS} if token else BASE_HEADERS
        ),
        json=body,
        timeout=None,
    )
    return response.json() if response.text else {}
