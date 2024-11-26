from datetime import date

from streamlit.testing.v1 import AppTest

from example.ui.components import date_range_picker


def _function_under_test():
    from example.ui.components import date_range_picker

    date_range_picker.show("test_key")


def test_date_range_picker_valid_default():
    at = AppTest.from_function(_function_under_test).run()

    date_range_default = (date_range_picker._START_DATE_DEFAULT, date_range_picker._END_DATE_DEFAULT)
    assert at.date_input[0].value == date_range_default
    assert at.session_state["test_key"] == date_range_default


def test_date_range_picker_valid_range():
    date_range = (date(2015, 1, 1), date(2015, 1, 15))

    at = AppTest.from_function(_function_under_test).run()
    at.date_input[0].set_value(date_range).run()

    assert at.date_input[0].value == date_range
    assert at.session_state["test_key"] == date_range


def test_date_range_picker_invalid_range():
    start_date_only = date(2015, 1, 1)

    at = AppTest.from_function(_function_under_test).run()
    at.date_input[0].set_value(start_date_only).run()

    assert at.date_input[0].value == (start_date_only,)
    assert at.error[0].value == "Please select a valid date range"
    assert at.session_state["test_key"] == (date_range_picker._START_DATE_DEFAULT, date_range_picker._END_DATE_DEFAULT)
