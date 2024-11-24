from datetime import date

import pandas as pd
import streamlit as st

from example.infrastructure import big_query

def get_trips(date_range: tuple[date, date], payment_type: int) -> pd.DataFrame:
    query = """
    SELECT
      DATE(pickup_datetime) AS day,
      payment_type AS payment_type,
      rate_code AS rate_code,
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
        "payment_type": payment_type,
    }

    return big_query.query(query, params)
