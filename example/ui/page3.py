import streamlit as st

from example.api import nyc_tlc_trips

st.title("Subsystem 2 - Page 1")

st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit")

with st.spinner("Loading trips ..."):
    # TODO: make this code testable and write streamlit test
    trips = nyc_tlc_trips.get_trips()

st.dataframe(trips)
