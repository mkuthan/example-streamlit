import pytest
from streamlit.testing.v1 import AppTest


@pytest.fixture
def page_under_test():
    return "example/ui/pages/antd_tree_component_page.py"


def test_show_title_and_initial_state(page_under_test):
    at = AppTest.from_file(page_under_test).run()

    # Check the title
    assert at.title[0].value == "AntD Tree Component"

    # Check the initial message when no node is selected
    assert "Please select a node from the tree." in [el.value for el in at.markdown]


@pytest.mark.skip(reason="I could find a way to test AntD Tree component")
def test_node_selection(page_under_test):
    at = AppTest.from_file(page_under_test)

    # Simulate selecting a node (index 0)
    at.get("tree")[0].set_value(0).run()

    # Check that the selected node details are displayed
    assert "Selected Node Details" in [el.value for el in at.subheader]

    # Verify some content of the selected node is shown
    markdown_values = [el.value for el in at.markdown]
    assert any("TreeNode(index=0, name='item1')" in value for value in markdown_values)
    assert any("tags=" in value for value in markdown_values)
