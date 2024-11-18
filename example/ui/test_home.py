from streamlit.testing.v1 import AppTest


def test_show_title():
    at = AppTest.from_file("home.py").run()

    assert at.title[0].value == "Home"
