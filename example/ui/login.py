import streamlit as st

from example.utils import authentication

st.title("Please login to continue")

if st.button("Log in"):
    authentication.login()
