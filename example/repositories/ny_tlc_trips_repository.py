from datetime import date

import pandas as pd
import streamlit as st

from example.infrastructure import big_query


@st.cache_data(ttl=600)
def trips_totals(date_range: tuple[date, date]) -> pd.DataFrame:
    query = """
    SELECT
      DATE(pickup_datetime) AS day,
      payment_type AS payment_type,
      rate_code AS rate_code,
      SUM(passenger_count) AS total_passengers,
      SUM(fare_amount) AS total_fare,
      SUM(tip_amount) AS total_tips,
      SUM(total_amount) AS total_amount,
      COUNT(*) AS trip_count
    FROM
      `bigquery-public-data.new_york.tlc_yellow_trips_2015`
    WHERE
      DATE(pickup_datetime) BETWEEN @start_date AND @end_date
    GROUP BY ALL
    """

    params = __prepare_date_range_params(date_range)

    return big_query.query(query, params)


@st.cache_data(ttl=600)
def trips_avg_speed(date_range: tuple[date, date]) -> pd.DataFrame:
    query = """
    SELECT
      DATE(pickup_datetime) AS day,
      AVG(trip_distance / TIMESTAMP_DIFF(dropoff_datetime, pickup_datetime, SECOND)) * 3600 AS avg_speed_mi_h
    FROM
      `bigquery-public-data.new_york.tlc_yellow_trips_2015`
    WHERE
      DATE(pickup_datetime) BETWEEN @start_date AND @end_date
    AND
      trip_distance > 0
    AND
      dropoff_datetime > pickup_datetime
    AND
      fare_amount/trip_distance BETWEEN 2 AND 10
    GROUP BY ALL
    """

    params = __prepare_date_range_params(date_range)

    return big_query.query(query, params)


def __prepare_date_range_params(date_range: tuple[date, date]) -> dict:
    return {"start_date": date_range[0].isoformat(), "end_date": date_range[1].isoformat()}
