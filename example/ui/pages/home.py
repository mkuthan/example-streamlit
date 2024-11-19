import streamlit as st

from example.ui.components import date_range_picker
from example.ui.components import payment_type_selector

st.title("Home")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit")

left, center = st.columns([0.2, 0.8])

with left:
    navigation_items = """
    * a
    * b
    * c
    * d
    * e
    * f
    * g
    * h
    """
    st.markdown(navigation_items)

with center:
    with st.container():
        date_range_picker.show()
        payment_type_selector.show()

    st.divider()

    with st.container():
        st.write("Content")
