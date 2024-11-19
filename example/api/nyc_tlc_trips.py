from datetime import date

import pandas as pd

import streamlit as st
from example.infrastructure import big_query

_PAYMENT_TYPES = {
    "1": "Credit card",
    "2": "Cash",
    "3": "No charge",
    "4": "Dispute",
    "5": "Unknown",
    "6": "Voided trip"
}


@st.cache_data(ttl=600)
def get_trips(date_range: tuple[date, date], payment_type: str) -> pd.DataFrame:
    query = """
    SELECT
      DATE(pickup_datetime) AS day,
      payment_type AS payment_type,
      SUM(fare_amount) AS total_fare,
      SUM(tip_amount) AS total_tips,
      SUM(total_amount) AS total_amount,
      COUNT(*) AS trip_count
    FROM
      `bigquery-public-data.new_york.tlc_yellow_trips_2015`
    WHERE
      DATE(pickup_datetime) BETWEEN @start_date AND @end_date
    AND
      payment_type = @payment_type
    GROUP BY ALL
    ORDER BY day
    """

    params = {
        "start_date": date_range[0].isoformat(),
        "end_date": date_range[1].isoformat(),
        "payment_type": _get_payment_type_key(payment_type)
    }

    results = big_query.query(query, params)

    results["payment_type"] = results["payment_type"].map(_PAYMENT_TYPES)

    return results


def _get_payment_type_key(payment_type: str) -> str:
    for key, value in _PAYMENT_TYPES.items():
        if value.lower() == payment_type.lower():
            return key
    raise ValueError(f"Invalid payment type: {payment_type}")
