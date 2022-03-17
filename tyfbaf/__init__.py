"""
tyfbaf
"""
from . import constants

__version__ = "0.0.8"


def setup(server_name: str, *, port: int = 6405):
    """Function to setup tyfbaf.

    Args:
        server_name (str): Just your server name, without any protocol or port.
        port (int, optional): The port in use of your server. Defaults to 6405.
    """
    constants.SERVER_NAME = server_name
    constants.PORT = port
