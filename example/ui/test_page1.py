from streamlit.testing.v1 import AppTest


def test_show_title():
    at = AppTest.from_file("page1.py").run()

    assert at.title[0].value == "Subsystem 1 - Page 1"
