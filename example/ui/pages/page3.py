import streamlit as st

from example.service import nyc_tlc_trips
from example.ui.components import date_range_picker, payment_type_selector

st.title("Page 3")

st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit")

st.divider()

date_range = date_range_picker.show()
payment_type = payment_type_selector.show()

trips = nyc_tlc_trips.get_trips(date_range, payment_type)

st.dataframe(trips)
