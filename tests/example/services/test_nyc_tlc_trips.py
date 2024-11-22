from datetime import date
from unittest.mock import patch

import pandas as pd
import pytest

from example.services import nyc_tlc_trips


@pytest.fixture
def mock_trips():
    with patch("example.infrastructure.big_query.query") as mock:
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


def test_get_trips(mock_trips):
    any_start_date = date(2015, 1, 1)
    any_end_date = date(2015, 1, 2)
    any_payment_type = "Credit card"

    results = nyc_tlc_trips.get_trips((any_start_date, any_end_date), any_payment_type)

    expected_params = {"start_date": "2015-01-01", "end_date": "2015-01-02", "payment_type": 1}

    mock_trips.assert_called_once()

    # TODO: avoid ugly code, why call_args[0]?
    actual_query, actual_params = mock_trips.call_args[0]
    assert actual_params == expected_params

    expected_trips = pd.DataFrame(
        {
            "day": ["2023-01-01", "2023-01-02"],
            "payment_type": ["Credit card", "Cash"],
            "rate_code": ["Standard rate", "JFK"],
            "total_fare": [100.0, 150.0],
            "total_tips": [10.0, 15.0],
            "total_amount": [110.0, 165.0],
            "trip_count": [1, 2],
        }
    )

    pd.testing.assert_frame_equal(results, expected_trips)
