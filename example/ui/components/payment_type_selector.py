import streamlit as st


# TODO: test this component
def show(key: str = "payment_type_selector"):
    payment_type_options = ["Cash", "Credit Card", "PayPal"]

    __initialize_state(key, payment_type_options)

    payment_type = st.selectbox("Payment type", payment_type_options, index=payment_type_options.index(st.session_state[key]))
    st.session_state[key] = payment_type


def __initialize_state(key: str, payment_type_options: list):
    if key not in st.session_state:
        st.session_state[key] = payment_type_options[0]
