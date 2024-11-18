import streamlit as st


def login():
    st.session_state["logged_in"] = True
    st.session_state["username"] = "John Doe"
    st.rerun()


def logout():
    st.session_state["logged_in"] = False
    st.session_state["username"] = None
    st.rerun()
