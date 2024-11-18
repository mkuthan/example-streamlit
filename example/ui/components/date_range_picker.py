from datetime import datetime
from datetime import timedelta

import streamlit as st


# TODO: test this component
def show(key: str = "date_range_picker"):
    __initialize_state(key)

    today = datetime.now().date()
    min_value = today - timedelta(days=3 * 365)
    max_value = today

    date_range = st.date_input("Select date range", min_value=min_value, max_value=max_value, value=st.session_state[key])

    if len(date_range) == 2:
        st.session_state[key] = date_range
    else:
        st.error("Please select a valid date range")


def __initialize_state(key: str):
    if key not in st.session_state:
        today = datetime.now().date()
        st.session_state[key] = (today - timedelta(days=7), today)
