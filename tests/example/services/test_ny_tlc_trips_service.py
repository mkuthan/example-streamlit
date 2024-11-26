from datetime import date
from unittest.mock import patch

import pandas as pd
import pytest

from example.services import ny_tlc_trips_service


@pytest.fixture
def any_date_range():
    return (date(2015, 1, 1), date(2015, 1, 2))


@pytest.fixture
def mock_trips_totals():
    with patch("example.repositories.ny_tlc_trips_repository.trips_totals") as mock:
        df = pd.DataFrame(
            {
                "day": ["2023-01-01", "2023-01-02"],
                "payment_type": [1, 2],
                "rate_code": [1, 2],
                "total_fare": [100.0, 150.0],
                "total_tips": [10.0, 15.0],
                "total_amount": [110.0, 165.0],
                "trip_count": [1, 2],
            }
        )
        mock.return_value = df
        yield mock


def test_trips_totals(mock_trips_totals, any_date_range):  # noqa: ARG001
    any_payment_type = "Credit card"

    results = ny_tlc_trips_service.trips_totals(any_date_range, any_payment_type)

    expected = pd.DataFrame(
        {
            "day": ["2023-01-01"],
            "payment_type": ["Credit card"],
            "rate_code": ["Standard rate"],
            "total_fare": [100.0],
            "total_tips": [10.0],
            "total_amount": [110.0],
            "trip_count": [1],
        }
    )

    pd.testing.assert_frame_equal(results, expected)


def test_trips_count_by_payment_type():
    # TODO: Implement this test
    pass


def test_trips_count_by_rate_code():
    # TODO: Implement this test
    pass


@pytest.fixture
def mock_trips_avg_speed():
    with patch("example.repositories.ny_tlc_trips_repository.trips_avg_speed") as mock:
        df = pd.DataFrame(
            {
                "day": ["2023-01-01", "2023-01-02", "2023-01-03"],
                "avg_speed_mi_h": [20.0, 25.0, 30.0],
            }
        )
        mock.return_value = df
        yield mock


def test_trips_avg_speed(mock_trips_avg_speed, any_date_range):  # noqa: ARG001
    results = ny_tlc_trips_service.trips_avg_speed(any_date_range)

    expected = pd.DataFrame(
        {
            "day": ["2023-01-01", "2023-01-02", "2023-01-03"],
            "avg_speed_mi_h": [20.0, 25.0, 30.0],
            "day_of_week": ["Sunday", "Monday", "Tuesday"],
        }
    )

    pd.testing.assert_frame_equal(results, expected)
