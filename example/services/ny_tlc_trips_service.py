from datetime import date

import pandas as pd

from example.repositories import ny_tlc_trips_repository

_PAYMENT_TYPES = {
    0: "Unknown",
    1: "Credit card",
    2: "Cash",
    3: "No charge",
    4: "Dispute",
    5: "Unknown",
    6: "Voided trip",
}

_RATE_CODES = {
    0: "Unknown",
    1: "Standard rate",
    2: "JFK",
    3: "Newark",
    4: "Nassau or Westchester",
    5: "Negotiated fare",
    6: "Group ride",
    99: "Other",
}


def trips_totals(date_range: tuple[date, date], payment_type: str) -> pd.DataFrame:
    df = _trips_totals(date_range)

    df = df[df["payment_type"] == payment_type]

    return df


def trips_count_by_payment_type(date_range: tuple[date, date]) -> pd.DataFrame:
    df = _trips_totals(date_range)

    df = df.groupby(["day", "payment_type"]).agg(sum).reset_index()

    return df


def trips_count_by_rate_code(date_range: tuple[date, date]) -> pd.DataFrame:
    df = _trips_totals(date_range)

    df = df.groupby(["day", "rate_code"]).agg(sum).reset_index()

    return df


def trips_avg_speed(date_range: tuple[date, date]) -> pd.DataFrame:
    df = ny_tlc_trips_repository.trips_avg_speed(date_range)

    df["day_of_week"] = pd.to_datetime(df["day"]).dt.day_name()
    df["avg_speed_mi_h"] = df["avg_speed_mi_h"].round(2)
    df = df.sort_values("day")

    return df


def _trips_totals(date_range: tuple[date, date]) -> pd.DataFrame:
    df = ny_tlc_trips_repository.trips_totals(date_range)

    df["payment_type"] = df["payment_type"].fillna(0).astype(int).map(_PAYMENT_TYPES)
    df["rate_code"] = df["rate_code"].fillna(0).astype(int).map(_RATE_CODES)

    df = df.sort_values("day")

    return df
