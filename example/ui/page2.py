import streamlit as st

from example.ui.components import date_range_picker
from example.ui.components import payment_type_selector

st.title("Page 2")

st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit")

with st.container():
    date_range_picker.show()
    payment_type_selector.show()

st.divider()

with st.container():
    st.write("Content")
