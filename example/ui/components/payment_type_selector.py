import streamlit as st


# TODO: test this component
def show(key: str = "payment_type_selector") -> str:
    payment_type_options = ["Credit card", "Cash", "No charge", "Dispute", "Unknown", "Voided trip"]

    __initialize_state(key, payment_type_options)

    payment_type = st.selectbox("Payment type", payment_type_options, index=payment_type_options.index(st.session_state[key]))
    st.session_state[key] = payment_type

    return st.session_state[key]


def __initialize_state(key: str, payment_type_options: list):
    if key not in st.session_state:
        st.session_state[key] = payment_type_options[0]
