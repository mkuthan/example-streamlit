import altair as alt
import streamlit as st

from example.services import nyc_tlc_trips
from example.ui.components import date_range_picker, payment_type_selector

st.title("NY Taxi Trips")

st.write("New York City Taxi and Limousine Commission (TLC) trips")

st.caption("Filters")

date_range = date_range_picker.show()
payment_type = payment_type_selector.show()

trips = nyc_tlc_trips.get_trips(date_range, payment_type)

st.caption("Search results")
st.dataframe(trips, use_container_width=True)

st.download_button("Export CSV", nyc_tlc_trips.export_trips(trips), "trips.csv", "text/csv")

trip_count_chart = (
    alt.Chart(trips)
    .mark_line()
    .encode(x="day:T", y="trip_count:Q", color="rate_code:N")
    .properties(title="Trip Count Over Time by Rate Code")
)

st.altair_chart(trip_count_chart, use_container_width=True)
