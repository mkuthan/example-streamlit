from streamlit.testing.v1 import AppTest


def test_show_title_and_login_button():
    at = AppTest.from_file("login.py").run()

    assert at.title[0].value == "Please login to continue"
    assert at.button[0].label == "Log in"


def test_login_button_click():
    at = AppTest.from_file("login.py").run()

    at.button[0].click().run()

    assert at.session_state["logged_in"] == True
    assert at.session_state["username"] == "John Doe"
