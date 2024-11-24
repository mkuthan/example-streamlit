from datetime import date
from unittest.mock import patch

import pandas as pd
import pytest

from example.services import ny_tlc_trips_service


@pytest.fixture
def mock_trips():
    with patch("example.repositories.ny_tlc_trips_repository.get_trips") as mock:
        df = pd.DataFrame(
            {
                "day": ["2023-01-01", "2023-01-02"],
                "payment_type": [1, 1],
                "rate_code": [1, 2],
                "total_fare": [100.0, 150.0],
                "total_tips": [10.0, 15.0],
                "total_amount": [110.0, 165.0],
                "trip_count": [1, 2],
            }
        )
        mock.return_value = df
        yield mock


def test_get_trips(mock_trips):
    any_start_date = date(2015, 1, 1)
    any_end_date = date(2015, 1, 2)
    any_payment_type = "Credit card"

    results = ny_tlc_trips_service.get_trips((any_start_date, any_end_date), any_payment_type)

    expected_trips = pd.DataFrame(
        {
            "day": ["2023-01-01", "2023-01-02"],
            "payment_type": ["Credit card", "Credit card"],
            "rate_code": ["Standard rate", "JFK"],
            "total_fare": [100.0, 150.0],
            "total_tips": [10.0, 15.0],
            "total_amount": [110.0, 165.0],
            "trip_count": [1, 2],
        }
    )

    pd.testing.assert_frame_equal(results, expected_trips)
