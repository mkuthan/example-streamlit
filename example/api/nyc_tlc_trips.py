from datetime import date

import pandas as pd

from example.infrastructure import big_query


def get_trips(date_range: tuple[date, date], payment_type: str) -> pd.DataFrame:
    query = """
    SELECT
      DATE(pickup_datetime) as day,
      SUM(fare_amount) as total_fare,
      SUM(tip_amount) as total_tips,
      SUM(total_amount) as total_amount,
      COUNT(*) as trip_count
    FROM
      `bigquery-public-data.new_york.tlc_yellow_trips_2015`
    GROUP BY
      day
    ORDER BY
      day
    """
    return big_query.query(query)
