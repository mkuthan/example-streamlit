from datetime import date

import streamlit as st

_START_DATE_DEFAULT = date(2015, 6, 1)
_END_DATE_DEFAULT = date(2015, 7, 30)

_MIN_DATE = date(2015, 1, 1)
_MAX_DATE = date(2015, 12, 31)


def show(key: str = "date_range_picker") -> tuple[date, date]:
    __initialize_state(key)

    value = st.session_state[key]

    date_range = st.date_input("Select date range", min_value=_MIN_DATE, max_value=_MAX_DATE, value=value)

    if len(date_range) == 2:
        st.session_state[key] = date_range
    else:
        st.error("Please select a valid date range")

    return st.session_state[key]


def __initialize_state(key: str) -> None:
    if key not in st.session_state:
        st.session_state[key] = (_START_DATE_DEFAULT, _END_DATE_DEFAULT)
