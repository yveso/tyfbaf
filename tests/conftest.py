import pytest

from tyfbaf import constants


@pytest.fixture(scope="function", autouse=True)
def constants_default_values():
    constants.SERVER_NAME = "server_name"
    constants.PORT = 6405
    constants.CURRENT_TOKEN = ""
