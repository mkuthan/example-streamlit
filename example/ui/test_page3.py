from unittest.mock import patch

import pandas as pd
import pandas.testing as pdt
from streamlit.testing.v1 import AppTest

@patch("example.api.nyc_tlc_trips.get_trips")
def test_show_title(mock_get_trips):
    trips = pd.DataFrame()
    mock_get_trips.return_value = trips

    at = AppTest.from_file("page3.py").run()

    assert at.title[0].value == "Page 3"

@patch("example.api.nyc_tlc_trips.get_trips")
def test_show_trips(mock_get_trips):
    trips = pd.DataFrame({
        'day': ['2023-01-01'],
        'payment_type': 'Credit card',
        'total_fare': [100.0],
        'total_tips': [10.0],
        'total_amount': [110.0],
        'trip_count': [1]
    })
    mock_get_trips.return_value = trips

    at = AppTest.from_file("page3.py").run()

    pdt.assert_frame_equal(at.dataframe[0].value, trips)
