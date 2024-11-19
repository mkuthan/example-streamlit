from datetime import date

import streamlit as st


# TODO: test this component
def show(key: str = "date_range_picker") -> tuple[date, date]:
    __initialize_state(key)

    min_value = date(2015, 1, 1)
    max_value = date(2015, 12, 31)

    date_range = st.date_input("Select date range", min_value=min_value, max_value=max_value, value=st.session_state[key])

    if len(date_range) == 2:
        st.session_state[key] = date_range
    else:
        st.error("Please select a valid date range")

    return st.session_state[key]


def __initialize_state(key: str):
    if key not in st.session_state:
        start = date(2015, 4, 1)
        end = date(2015, 4, 30)
        st.session_state[key] = (start, end)
