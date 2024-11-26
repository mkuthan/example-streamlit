from unittest.mock import patch

import pandas as pd
import pytest
from streamlit.testing.v1 import AppTest


@pytest.fixture
def page_under_test():
    return "example/ui/pages/ny_tlc_trips_avg_speed_page.py"


@pytest.fixture
def mock_trips_avg_speed():
    with patch("example.services.ny_tlc_trips_service.trips_avg_speed") as mock:
        yield mock


@pytest.fixture
def mock_trips_avg_speed_empty(mock_trips_avg_speed):
    mock_trips_avg_speed.return_value = pd.DataFrame()
    yield mock_trips_avg_speed


def test_show_title_and_no_results(page_under_test, mock_trips_avg_speed_empty):  # noqa: ARG001
    at = AppTest.from_file(page_under_test).run()

    assert at.title[0].value == "NY Taxi Trips Average Speed"

    assert "No trips found" in [el.value for el in at.markdown]

    assert len(at.get("arrow_vega_lite_chart")) == 0


@pytest.fixture
def mock_trips_avg_speed_single(mock_trips_avg_speed):
    mock_trips_avg_speed.return_value = pd.DataFrame(
        {
            "day": ["2023-01-01"],
            "avg_speed_mi_h": [20.0],
        }
    )
    yield mock_trips_avg_speed


def test_show_avg_speed_chart(page_under_test, mock_trips_avg_speed_single):  # noqa: ARG001
    at = AppTest.from_file(page_under_test).run()

    assert at.title[0].value == "NY Taxi Trips Average Speed"

    assert len(at.get("arrow_vega_lite_chart")) == 1
    # pdt.assert_frame_equal(at.vega_lite_chart[0].data, mock_trips_avg_speed.return_value)
