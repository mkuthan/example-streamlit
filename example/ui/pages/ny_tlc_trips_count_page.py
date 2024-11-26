import altair as alt
import streamlit as st

from example.services import ny_tlc_trips_service
from example.ui.components import date_range_picker

st.title("NY Taxi Trips Count")

st.caption("Filters")

date_range = date_range_picker.show()

st.caption("Search results")

x_axis = alt.X("day:T", title="Day")
y_axis = alt.Y("trip_count:Q", title="Trip Count")

trips_count_by_payment_type = ny_tlc_trips_service.trips_count_by_payment_type(date_range)

if trips_count_by_payment_type.empty:
    st.write("No trips found")
else:
    trip_count_by_payment_type_chart = (
        alt.Chart(trips_count_by_payment_type)
        .mark_line()
        .encode(x=x_axis, y=y_axis, color=alt.Color("payment_type:N", title="Payment Type"))
        .properties(title="Trip Count Over Time by Payment Type")
    )
    st.altair_chart(trip_count_by_payment_type_chart, use_container_width=True)

trips_count_by_rate_code = ny_tlc_trips_service.trips_count_by_rate_code(date_range)

if trips_count_by_rate_code.empty:
    st.write("No trips found")
else:
    trip_count_by_rate_code_chart = (
        alt.Chart(trips_count_by_rate_code)
        .mark_line()
        .encode(x=x_axis, y=y_axis, color=alt.Color("rate_code:N", title="Rate Code"))
        .properties(title="Trip Count Over Time by Rate Code")
    )
    st.altair_chart(trip_count_by_rate_code_chart, use_container_width=True)
