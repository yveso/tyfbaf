from typing import Any, Optional
import httpx
from . import constants


def get(endpoint: str, *, token: Optional[str] = None) -> dict[str, Any]:
    """Function to make http get requests easier.

    Args:
        endpoint (str): The endpoint to your desired API, for example "/raylight/v1/documents".
        token (Optional[str], optional): Your token. Defaults to None.

    Returns:
        dict[str, Any]: The response of the HTTP get request.
    """
    response = httpx.get(
        f"http://{constants.SERVER_NAME}:{constants.PORT}/biprws{endpoint}",
        headers=(
            {
                "X-SAP-LogonToken": token or constants.CURRENT_TOKEN,
                **constants.BASE_HEADERS,
            }
            if (token or constants.CURRENT_TOKEN)
            else constants.BASE_HEADERS
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
        f"http://{constants.SERVER_NAME}:{constants.PORT}/biprws{endpoint}",
        headers=(
            {
                "X-SAP-LogonToken": token or constants.CURRENT_TOKEN,
                **constants.BASE_HEADERS,
            }
            if (token or constants.CURRENT_TOKEN)
            else constants.BASE_HEADERS
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
            {
                "X-SAP-LogonToken": token or constants.CURRENT_TOKEN,
                **constants.BASE_HEADERS,
            }
            if (token or constants.CURRENT_TOKEN)
            else constants.BASE_HEADERS
        ),
        json=body,
        timeout=None,
    )
    return response.json() if response.text else {}
