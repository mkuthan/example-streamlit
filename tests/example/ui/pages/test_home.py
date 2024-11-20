from streamlit.testing.v1 import AppTest


def test_show_title():
    at = AppTest.from_file("example/ui/pages/home.py").run()

    assert at.title[0].value == "Home"
