import altair as alt
import streamlit as st

from example.services import ny_tlc_trips_service
from example.ui.components import date_range_picker

st.title("NY Taxi Trips Average Speed")

st.caption("Filters")

date_range = date_range_picker.show()

trips = ny_tlc_trips_service.trips_avg_speed(date_range)

st.caption("Search results")

if trips.empty:
    st.write("No trips found")
else:
    column_descriptions = {"day": "Date", "day_of_week": "Day of week", "avg_speed_mi_h": "Average Speed (mi/h)"}

    line = (
        alt.Chart(trips)
        .mark_line()
        .encode(
            x=alt.X("day:T", title=column_descriptions["day"]),
            y=alt.Y("avg_speed_mi_h:Q", title=column_descriptions["avg_speed_mi_h"]),
        )
    )
    points = line.mark_point().encode(
        tooltip=[
            alt.Tooltip("day:T", title=column_descriptions["day"]),
            alt.Tooltip("day_of_week:N", title=column_descriptions["day_of_week"]),
            alt.Tooltip("avg_speed_mi_h:Q", title=column_descriptions["avg_speed_mi_h"]),
        ]
    )

    trip_avg_speed_chart = (line + points).properties(title="Trip Average Speed Over Time")

    st.altair_chart(trip_avg_speed_chart, use_container_width=True)
