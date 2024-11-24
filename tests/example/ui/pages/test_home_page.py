from streamlit.testing.v1 import AppTest


def test_show_title():
    at = AppTest.from_file("example/ui/pages/home_page.py").run()

    assert at.title[0].value == "Home"


def test_show_navigation_search_results_sections():
    at = AppTest.from_file("example/ui/pages/home_page.py").run()

    assert at.caption[0].value == "Navigation"
    assert at.caption[1].value == "Filters"
    assert at.caption[2].value == "Search results"
