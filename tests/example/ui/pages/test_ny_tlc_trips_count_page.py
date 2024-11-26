from unittest.mock import patch

import pandas as pd
import pytest
from streamlit.testing.v1 import AppTest


@pytest.fixture
def page_under_test():
    return "example/ui/pages/ny_tlc_trips_count_page.py"


@pytest.fixture
def mock_trips_count_by_payment_type():
    with patch("example.services.ny_tlc_trips_service.trips_count_by_payment_type") as mock:
        yield mock


@pytest.fixture
def mock_trips_count_by_rate_code():
    with patch("example.services.ny_tlc_trips_service.trips_count_by_rate_code") as mock:
        yield mock


@pytest.fixture
def mock_trips_count_by_payment_type_empty(mock_trips_count_by_payment_type):
    mock_trips_count_by_payment_type.return_value = pd.DataFrame()
    yield mock_trips_count_by_payment_type


@pytest.fixture
def mock_trips_count_by_rate_code_empty(mock_trips_count_by_rate_code):
    mock_trips_count_by_rate_code.return_value = pd.DataFrame()
    yield mock_trips_count_by_rate_code


def test_show_title_and_no_results(
    page_under_test,
    mock_trips_count_by_payment_type_empty,  # noqa: ARG001
    mock_trips_count_by_rate_code_empty,  # noqa: ARG001
):
    at = AppTest.from_file(page_under_test).run()

    assert at.title[0].value == "NY Taxi Trips Count"

    assert "No trips found" in [el.value for el in at.markdown]

    assert len(at.get("arrow_vega_lite_chart")) == 0


@pytest.fixture
def mock_trips_count_by_payment_type_single(mock_trips_count_by_payment_type):
    mock_trips_count_by_payment_type.return_value = pd.DataFrame(
        {
            "day": ["2023-01-01"],
            "payment_type": "Credit card",
            "total_fare": [100.0],
            "total_tips": [10.0],
            "total_amount": [110.0],
            "trip_count": [1],
        }
    )
    yield mock_trips_count_by_payment_type


@pytest.fixture
def mock_trip_count_by_rate_code_single(mock_trips_count_by_rate_code):
    mock_trips_count_by_rate_code.return_value = pd.DataFrame(
        {
            "day": ["2023-01-01"],
            "rate_code": "Standard rate",
            "total_fare": [100.0],
            "total_tips": [10.0],
            "total_amount": [110.0],
            "trip_count": [1],
        }
    )
    yield mock_trips_count_by_rate_code


def test_show_line_chart(page_under_test, mock_trips_count_by_payment_type_single, mock_trip_count_by_rate_code_single):  # noqa: ARG001
    at = AppTest.from_file(page_under_test).run()

    assert len(at.get("arrow_vega_lite_chart")) == 2
