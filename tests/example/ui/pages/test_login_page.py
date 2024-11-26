import pytest
from streamlit.testing.v1 import AppTest


@pytest.fixture
def page_under_test():
    return "example/ui/pages/login_page.py"


def test_show_title_and_login_button(page_under_test):
    at = AppTest.from_file(page_under_test).run()

    assert at.title[0].value == "Please login to continue"
    assert at.button[0].label == "Log in"


def test_login_button_click(page_under_test):
    at = AppTest.from_file(page_under_test).run()

    at.button[0].click().run()

    assert at.session_state["logged_in"] is True
    assert at.session_state["username"] == "John Doe"
