import pytest
from streamlit.testing.v1 import AppTest


@pytest.fixture
def page_under_test():
    return "example/ui/pages/home_page.py"


def test_show_title(page_under_test):
    at = AppTest.from_file(page_under_test).run()

    assert at.title[0].value == "Home"


def test_show_navigation_search_results_sections(page_under_test):
    at = AppTest.from_file(page_under_test).run()

    assert at.caption[0].value == "Navigation"
    assert at.caption[1].value == "Filters"
    assert at.caption[2].value == "Search results"
