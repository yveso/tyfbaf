import json

import httpx
import respx

from tyfbaf import constants, http


def test_get_expected_uri_gets_called(respx_mock):
    route = respx.get("http://server_name:6405/biprws/an_endpoint")
    _ = http.get("/an_endpoint")
    assert route.called


def test_get_base_headers_are_set(respx_mock):
    route = respx.get(
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    _ = http.get("/an_endpoint")
    assert route.called


def test_get_token_if_passed_is_used(respx_mock):
    route = respx.get(
        headers={
            "X-SAP-LogonToken": "a_token",
        },
    )
    _ = http.get("/an_endpoint", token="a_token")
    assert route.called


def test_get_token_if_saved_is_used(respx_mock):
    constants.CURRENT_TOKEN = "saved_token"
    route = respx.get(
        headers={
            "X-SAP-LogonToken": "saved_token",
        },
    )
    _ = http.get("/an_endpoint")
    assert route.called


def test_get_returns_empty_dict_if_response_was_empty(respx_mock):
    _ = respx.get().mock(return_value=httpx.Response(200, text=""))
    response = http.get("/an_endpoint")
    assert response == {}


def test_get_returns_expected_object(respx_mock):
    _ = respx.get().mock(return_value=httpx.Response(200, json={"key": "value"}))
    response = http.get("/an_endpoint")
    assert response == {"key": "value"}


def test_post_expected_uri_gets_called(respx_mock):
    route = respx.post("http://server_name:6405/biprws/an_endpoint")
    _ = http.post("/an_endpoint")
    assert route.called


def test_post_base_headers_are_set(respx_mock):
    route = respx.post(
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    _ = http.post("/an_endpoint")
    assert route.called


def test_post_token_if_passed_is_used(respx_mock):
    route = respx.post(
        headers={
            "X-SAP-LogonToken": "a_token",
        },
    )
    _ = http.post("/an_endpoint", token="a_token")
    assert route.called


def test_post_token_if_saved_is_used(respx_mock):
    constants.CURRENT_TOKEN = "saved_token"
    route = respx.post(
        headers={
            "X-SAP-LogonToken": "saved_token",
        },
    )
    _ = http.post("/an_endpoint")
    assert route.called


def test_post_body_if_passed_is_used(respx_mock):
    route = respx.post(
        json={
            "key": "value",
        },
    )
    _ = http.post("/an_endpoint", body={"key": "value"})
    assert route.called


def test_post_returns_empty_dict_if_response_was_empty(respx_mock):
    _ = respx.post().mock(return_value=httpx.Response(200, text=""))
    response = http.post("/an_endpoint")
    assert response == {}


def test_post_returns_expected_object(respx_mock):
    _ = respx.post().mock(return_value=httpx.Response(200, json={"key": "value"}))
    response = http.post("/an_endpoint")
    assert response == {"key": "value"}


def test_post_full_uriexpected_uri_gets_called(respx_mock):
    route = respx.post("http://server_name:6405/biprws/an_endpoint")
    _ = http.post_full_uri("http://server_name:6405/biprws/an_endpoint")
    assert route.called


def test_post_full_uri_base_headers_are_set(respx_mock):
    route = respx.post(
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    _ = http.post_full_uri("http://server_name:6405/biprws/an_endpoint")
    assert route.called


def test_post_full_uri_token_if_passed_is_used(respx_mock):
    route = respx.post(
        headers={
            "X-SAP-LogonToken": "a_token",
        },
    )
    _ = http.post_full_uri(
        "http://server_name:6405/biprws/an_endpoint", token="a_token"
    )
    assert route.called


def test_post_full_uri_token_if_saved_is_used(respx_mock):
    constants.CURRENT_TOKEN = "saved_token"
    route = respx.post(
        headers={
            "X-SAP-LogonToken": "saved_token",
        },
    )
    _ = http.post_full_uri("http://server_name:6405/biprws/an_endpoint")
    assert route.called


def test_post_full_uri_body_if_passed_is_used(respx_mock):
    route = respx.post(
        json={
            "key": "value",
        },
    )
    _ = http.post_full_uri(
        "http://server_name:6405/biprws/an_endpoint", body={"key": "value"}
    )
    assert route.called


def test_post_full_uri_returns_empty_dict_if_response_was_empty(respx_mock):
    _ = respx.post().mock(return_value=httpx.Response(200, text=""))
    response = http.post_full_uri("http://server_name:6405/biprws/an_endpoint")
    assert response == {}


def test_post_full_uri_returns_expected_object(respx_mock):
    _ = respx.post().mock(return_value=httpx.Response(200, json={"key": "value"}))
    response = http.post_full_uri("http://server_name:6405/biprws/an_endpoint")
    assert response == {"key": "value"}
