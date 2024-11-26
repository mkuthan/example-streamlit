from unittest.mock import patch

import pandas as pd
import pandas.testing as pdt
import pytest
from streamlit.testing.v1 import AppTest


@pytest.fixture
def page_under_test():
    return "example/ui/pages/ny_tlc_trips_totals_page.py"


@pytest.fixture
def mock_trips_totals():
    with patch("example.services.ny_tlc_trips_service.trips_totals") as mock:
        yield mock


@pytest.fixture
def mock_trips_totals_empty(mock_trips_totals):
    mock_trips_totals.return_value = pd.DataFrame()
    yield mock_trips_totals


def test_show_title_and_no_results(page_under_test, mock_trips_totals_empty):  # noqa: ARG001
    at = AppTest.from_file(page_under_test).run()

    assert at.title[0].value == "NY Taxi Trips Totals"

    assert "No trips found" in [el.value for el in at.markdown]

    assert len(at.dataframe) == 0
    assert len(at.get("download_button")) == 0
    assert len(at.get("arrow_vega_lite_chart")) == 0


@pytest.fixture
def mock_trips_totals_single(mock_trips_totals):
    mock_trips_totals.return_value = pd.DataFrame(
        {
            "day": ["2023-01-01"],
            "payment_type": "Credit card",
            "total_fare": [100.0],
            "total_tips": [10.0],
            "total_amount": [110.0],
            "trip_count": [1],
        }
    )
    yield mock_trips_totals


def test_show_trips_dataframe(page_under_test, mock_trips_totals_single):
    at = AppTest.from_file(page_under_test).run()

    pdt.assert_frame_equal(at.dataframe[0].value, mock_trips_totals_single.return_value)


def test_show_export_buttons(page_under_test, mock_trips_totals_single):  # noqa: ARG001
    at = AppTest.from_file(page_under_test).run()

    assert len(at.get("download_button")) == 2


def test_show_line_chart(page_under_test, mock_trips_totals_single):  # noqa: ARG001
    at = AppTest.from_file(page_under_test).run()

    assert len(at.get("arrow_vega_lite_chart")) == 1
