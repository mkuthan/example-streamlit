import streamlit as st

_PAYMENT_TYPE_OPTIONS = ["Credit card", "Cash", "No charge", "Dispute", "Unknown", "Voided trip"]


def show(key: str = "payment_type_selector") -> str:
    __initialize_state(key)

    index = _PAYMENT_TYPE_OPTIONS.index(st.session_state[key])

    payment_type = st.selectbox("Payment type", _PAYMENT_TYPE_OPTIONS, index=index)
    st.session_state[key] = payment_type

    return st.session_state[key]


def __initialize_state(key: str) -> None:
    if key not in st.session_state:
        st.session_state[key] = _PAYMENT_TYPE_OPTIONS[0]
