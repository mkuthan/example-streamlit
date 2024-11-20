from streamlit.testing.v1 import AppTest

from example.utils import serde


def test_show_app_unauthenticated():
    at = AppTest.from_file("app.py").run()

    # TODO: no components for unauthenticated user, what else can we assert?
    assert len(at.button) == 0


def test_show_app_authenticated():
    at = AppTest.from_file("app.py")
    at.session_state["logged_in"] = True
    at.session_state["username"] = "John Doe"
    at.run()

    assert at.button[0].label == "Share"
    assert at.button[1].label == "Log out"


def test_logout_button_click():
    at = AppTest.from_file("app.py")
    at.session_state["logged_in"] = True
    at.session_state["username"] = "John Doe"
    at.run()

    at.button[1].click().run()

    assert at.session_state["logged_in"] is False
    assert at.session_state["username"] is None


def test_decode_valid_state():
    at = AppTest.from_file("app.py")
    at.query_params["s"] = serde.encode_to_url({"k1": "v1", "k2": "v2"})
    at.run()

    assert at.session_state["k1"] == "v1"
    assert at.session_state["k2"] == "v2"


def test_decode_and_merge_valid_state():
    at = AppTest.from_file("app.py")
    at.session_state["k1"] = "v1"
    at.session_state["k2"] = "v2"
    at.query_params["s"] = serde.encode_to_url({"k2": "updated v2", "k3": "v3"})
    at.run()

    assert at.session_state["k1"] == "v1"
    assert at.session_state["k2"] == "updated v2"
    assert at.session_state["k3"] == "v3"


def test_decode_invalid_state():
    at = AppTest.from_file("app.py")
    at.query_params["s"] = "invalid state"
    at.run()

    assert at.exception[0].message == "pickle data was truncated"
