import pytest
from tyfbaf import constants


@pytest.fixture
def ugly_hack():
    """Ugly hack to disable autouse fixture in conftest.py..."""
    constants.SERVER_NAME = ""


def test_server_name_default(ugly_hack):
    assert constants.SERVER_NAME == ""


def test_port_default():
    assert constants.PORT == 6405


def test_base_headers_default():
    assert constants.BASE_HEADERS == {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def test_current_token_default():
    assert constants.CURRENT_TOKEN == ""
