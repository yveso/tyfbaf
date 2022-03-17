from typing import Optional
from . import constants
from .http import post


def request(username: str, password: str) -> str:
    """Request a new token.

    Args:
        username (str): Your username.
        password (str): Your password.

    Raises:
        ValueError: When your credentials couldn't be verified.

    Returns:
        str: Your new token. 😎
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
    constants.CURRENT_TOKEN = request(username=username, password=password)


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
    if constants.CURRENT_TOKEN:
        invalidate(token=constants.CURRENT_TOKEN)
    constants.CURRENT_TOKEN = ""
