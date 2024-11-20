import streamlit as st

from example.ui.components import date_range_picker, payment_type_selector

st.title("Page 4")

st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit")

with st.container():
    date_range_picker.show("page4_date_range_picker")
    payment_type_selector.show("page4_payment_type_selector")

st.divider()

with st.container():
    st.write("Content")
