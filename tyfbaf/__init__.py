"""
tyfbaf
"""
from .http import _setup

__version__ = "0.0.7"


def setup(server_name: str, *, port: int = 6405):
    """Function to setup tyfbaf.

    Args:
        server_name (str): Just your server name, without any protocol or port.
        port (int, optional): The port in use of your server. Defaults to 6405.
    """
    _setup(server_name, port)
