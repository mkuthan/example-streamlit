import streamlit as st

from example.api import nyc_tlc_trips
from example.ui.components import date_range_picker
from example.ui.components import payment_type_selector

st.title("Subsystem 2 - Page 1")

st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit")

date_range = date_range_picker.show()
payment_type = payment_type_selector.show()

st.divider()

with st.spinner("Loading trips ..."):
    # TODO: make this code testable and write streamlit test
    trips = nyc_tlc_trips.get_trips(date_range, payment_type)

st.dataframe(trips)
