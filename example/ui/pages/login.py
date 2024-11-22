import streamlit as st

from example.ui.components import authenticator

st.title("Please login to continue")

if st.button("Log in", icon=":material/login:"):
    authenticator.login()
