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


def get_trips(date_range: tuple[date, date], payment_type: str) -> pd.DataFrame:
    df = ny_tlc_trips_repository.get_trips(date_range)

    df["payment_type"] = df["payment_type"].fillna(0).astype(int).map(_PAYMENT_TYPES)
    df["rate_code"] = df["rate_code"].fillna(0).astype(int).map(_RATE_CODES)

    df = df[df["payment_type"] == payment_type]
    df = df.sort_values("day")

    return df


def _get_payment_type_key(payment_type: str) -> str:
    for key, value in _PAYMENT_TYPES.items():
        if value.lower() == payment_type.lower():
            return key
    raise ValueError(f"Invalid payment type: {payment_type}")
