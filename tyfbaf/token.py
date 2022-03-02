from typing import Optional
from .http import post


def request(username: str, password: str) -> Optional[str]:
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
        return response.get("logonToken")
    elif response.get("error_code", "") == "FWB 00008":
        raise ValueError(response.get("message"))


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
