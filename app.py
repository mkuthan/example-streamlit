import streamlit as st

from example.utils import authentication
from example.utils import serde


@st.dialog("Share")
def share(path: str):
    state = st.session_state.to_dict()
    state_encoded = serde.encode_to_url(state)

    st.write("Copy the link below to share the current state of the app:")
    st.link_button("Share", f"{path}?s=${state_encoded}", icon=":material/link:")
    st.write("Current state:")
    st.json(state)


# Very limited state management, no versioning, no validation
if "s" in st.query_params:
    state_decoded = serde.decode_from_url(st.query_params["s"])
    st.session_state.update(state_decoded)

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

st.set_page_config(
    page_title="Streamlit Non-Trivial App",
    page_icon="https://streamlit.io/images/brand/streamlit-mark-color.png",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://streamlit.io/"
    }
)

st.logo("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", size="large")

if not st.session_state.logged_in:
    login_page = st.Page("example/ui/login.py", title="Log in", icon=":material/login:")

    pg = st.navigation(pages=[login_page])
else:
    p1 = st.Page("example/ui/page1.py", title="Page 1", icon=":material/dashboard:", default=True)
    p2 = st.Page("example/ui/page2.py", title="Page 2", icon=":material/dashboard:")
    p3 = st.Page("example/ui/page3.py", title="Page 3", icon=":material/history:")
    p4 = st.Page("example/ui/page4.py", title="Page 4", icon=":material/history:")

    pg = st.navigation(pages=[p1, p2, p3, p4])

    if st.sidebar.button("Share", icon=":material/link:"):
        share(pg.url_path)

    if st.sidebar.button("Log out", icon=":material/person:"):
        authentication.logout()

pg.run()
