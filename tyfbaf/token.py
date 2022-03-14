from typing import Optional
from .http import post

CURRENT_TOKEN = ""


def request(username: str, password: str) -> str:
    """Request a new token.

    Args:
        username (str): Your username.
        password (str): Your password.

    Raises:
        ValueError: When your credentials couldn't be verified.

    Returns:
        Optional[str]: Your new token. 😎
    """
    response = post(
        "/logon/long",
        body={"userName": username, "password": password, "auth": "secEnterprise"},
    )
    if "logonToken" in response:
        return str(response.get("logonToken"))
    elif response.get("error_code", "") == "FWB 00008":
        raise ValueError(response.get("message"))
    else:
        return ""


def request_and_save(username: str, password: str) -> None:
    """Request a new token and save it, so it will be automatically used.

    Args:
        username (str): Your username.
        password (str): Your password.
    """
    global CURRENT_TOKEN
    CURRENT_TOKEN = request(username=username, password=password)


def invalidate(token: str) -> None:
    """Invalidates a token.

    Args:
        token (str): The token to invalidate.

    Raises:
        ValueError: Your token wasn't valid anyway. 😀
    """
    response = post("/logoff", token=token)

    if response.get("error_code", "") == "FWM 02024":
        raise ValueError(response.get("message"))


def invalidate_saved_token() -> None:
    """Invalidates a saved token."""
    global CURRENT_TOKEN
    if CURRENT_TOKEN:
        invalidate(token=CURRENT_TOKEN)
    CURRENT_TOKEN = ""
