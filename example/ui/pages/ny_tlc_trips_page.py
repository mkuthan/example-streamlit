import altair as alt
import streamlit as st

from example.services import ny_tlc_trips_service
from example.ui.components import date_range_picker, export_buttons, payment_type_selector

st.title("NY Taxi Trips")

st.write("New York City Taxi and Limousine Commission (TLC) trips")

st.caption("Filters")

date_range = date_range_picker.show()
payment_type = payment_type_selector.show()

trips = ny_tlc_trips_service.get_trips(date_range, payment_type)

st.caption("Search results")

if trips.empty:
    st.write("No trips found")
else:
    st.dataframe(trips, use_container_width=True)

    # TODO: make component for buttons in a single row
    csv, xls = st.columns(2)
    with csv:
        export_buttons.show_export_csv(trips, "ny_tlc_trips.csv")
    with xls:
        export_buttons.show_export_excel(trips, "ny_tlc_trips.xlsx")

    trip_count_chart = (
        alt.Chart(trips)
        .mark_line()
        .encode(x="day:T", y="trip_count:Q", color="rate_code:N")
        .properties(title="Trip Count Over Time by Rate Code")
    )

    st.altair_chart(trip_count_chart, use_container_width=True)
