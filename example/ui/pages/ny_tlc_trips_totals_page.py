import streamlit as st

from example.services import ny_tlc_trips_service
from example.ui.components import date_range_picker, export_buttons, payment_type_selector

st.title("NY Taxi Trips Totals")

st.caption("Filters")

date_range = date_range_picker.show()
payment_type = payment_type_selector.show()

st.caption("Search results")

trips_totals = ny_tlc_trips_service.trips_totals(date_range, payment_type)

if trips_totals.empty:
    st.write("No trips found")
else:
    st.dataframe(trips_totals, height=800, use_container_width=True)

    export_buttons.show_export_csv(trips_totals, "ny_tlc_trips.csv")
    export_buttons.show_export_excel(trips_totals, "ny_tlc_trips.xlsx")
