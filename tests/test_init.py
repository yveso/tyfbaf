import tyfbaf
import tyfbaf.constants


def test_setup_server_name_is_saved_as_intended():
    tyfbaf.setup("my-awesome-server-name")
    assert tyfbaf.constants.SERVER_NAME == "my-awesome-server-name"


def test_setup_default_port_is_used_when_none_is_given():
    tyfbaf.setup("my-awesome-server-name")
    assert tyfbaf.constants.PORT == 6405


def test_setup_port_is_saved_as_intended_when_given():
    tyfbaf.setup("my-awesome-server-name", port=1234)
    assert tyfbaf.constants.PORT == 1234
<<<<<<< Updated upstream
    tyfbaf.constants.PORT = 6405
=======
>>>>>>> Stashed changes
