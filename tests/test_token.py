import httpx
import pytest
import respx
from tyfbaf import constants, token


def test_request_token_is_returned_when_everything_was_cool(respx_mock):
    constants.SERVER_NAME = "server_name"
    _ = respx.route().mock(
        return_value=httpx.Response(200, json={"logonToken": "a_token"})
    )
    requested_token = token.request(username="username", password="password")
    assert requested_token == "a_token"


def test_request_reraises_bo_error(respx_mock):
    constants.SERVER_NAME = "server_name"
    _ = respx.route().mock(
        return_value=httpx.Response(
            200, json={"error_code": "FWB 00008", "message": "The message"}
        )
    )
    with pytest.raises(ValueError) as error:
        _ = token.request(username="username", password="password")
    assert str(error.value) == "The message"


def test_request_empty_string_is_returned_when_response_is_empty(respx_mock):
    constants.SERVER_NAME = "server_name"
    _ = respx.route().mock(return_value=httpx.Response(200))
    requested_token = token.request(username="username", password="password")
    assert requested_token == ""


def test_request_and_save_token_is_saved_when_everything_was_cool(respx_mock):
    constants.SERVER_NAME = "server_name"
    _ = respx.route().mock(
        return_value=httpx.Response(200, json={"logonToken": "a_token"})
    )
    token.request_and_save(username="username", password="password")
    assert constants.CURRENT_TOKEN == "a_token"


def test_invalidate_sends_expected_request_to_logoff(respx_mock):
    constants.SERVER_NAME = "server_name"
    route = respx.post(
        "http://server_name:6405/biprws/logoff",
        headers={
            "X-SAP-LogonToken": "a_token",
        },
    )
    token.invalidate("a_token")
    assert route.called


def test_invalidate_reraises_bo_error(respx_mock):
    constants.SERVER_NAME = "server_name"
    _ = respx.route().mock(
        return_value=httpx.Response(
            200, json={"error_code": "FWM 02024", "message": "The message"}
        )
    )
    with pytest.raises(ValueError) as error:
        token.invalidate("a_token")
    assert str(error.value) == "The message"


def test_invalidate_saved_token_sends_expected_request_to_logoff_if_a_token_is_saved(
    respx_mock,
):
    constants.SERVER_NAME = "server_name"
    constants.CURRENT_TOKEN = "a_token"
    route = respx.post(
        "http://server_name:6405/biprws/logoff",
        headers={
            "X-SAP-LogonToken": "a_token",
        },
    )
    token.invalidate_saved_token()
    assert route.called


def test_invalidate_saved_token_resets_token(
    respx_mock,
):
    constants.SERVER_NAME = "server_name"
    constants.CURRENT_TOKEN = "a_token"
    _ = respx.route()
    token.invalidate_saved_token()
    assert constants.CURRENT_TOKEN == ""
