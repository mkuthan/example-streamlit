import streamlit as st

from example.ui.components import authentication

st.title("Please login to continue")

if st.button("Log in", icon=":material/login:"):
    authentication.login()
