from unittest.mock import patch

import pandas as pd
import pandas.testing as pdt
import pytest
from streamlit.testing.v1 import AppTest


@pytest.fixture
def mock_trips():
    with patch("example.services.nyc_tlc_trips.get_trips") as mock:
        df = pd.DataFrame(
            {
                "day": ["2023-01-01"],
                "payment_type": "Credit card",
                "total_fare": [100.0],
                "total_tips": [10.0],
                "total_amount": [110.0],
                "trip_count": [1],
            }
        )
        mock.return_value = df
        yield mock


@patch("example.services.nyc_tlc_trips.get_trips")
def test_show_title_and_no_results(mock_get_trips_empty):
    mock_get_trips_empty.return_value = pd.DataFrame()

    at = AppTest.from_file("example/ui/pages/nyt_tlc_trips.py").run()

    assert at.title[0].value == "NY Taxi Trips"

    assert "No trips found" in [el.value for el in at.markdown]

    assert len(at.dataframe) == 0
    assert len(at.get("download_button")) == 0
    assert len(at.get("arrow_vega_lite_chart")) == 0


def test_show_trips_dataframe(mock_trips):
    at = AppTest.from_file("example/ui/pages/nyt_tlc_trips.py").run()

    pdt.assert_frame_equal(at.dataframe[0].value, mock_trips.return_value)


def test_show_export_buttons(mock_trips):  # noqa: ARG001
    at = AppTest.from_file("example/ui/pages/nyt_tlc_trips.py").run()

    assert len(at.get("download_button")) == 2


def test_show_line_chart(mock_trips):  # noqa: ARG001
    at = AppTest.from_file("example/ui/pages/nyt_tlc_trips.py").run()

    assert len(at.get("arrow_vega_lite_chart")) == 1
