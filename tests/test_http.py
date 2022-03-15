import respx
from tyfbaf import constants
from tyfbaf.http import get


@respx.mock
def test_get_uri():
    constants.SERVER_NAME = "a"
    foo_route = respx.get("http://a:6405/biprws/foo").mock()
    get("/foo")
    assert foo_route.called
