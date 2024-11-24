import streamlit as st

from example.ui.components import authenticator
from example.utils import url_serde


@st.dialog("Share")
def share(path: str) -> None:
    state = st.session_state.to_dict()
    state_encoded = url_serde.encode(state)

    st.write("Copy the link below to share the current state of the app:")
    st.link_button("Share", f"{path}?s=${state_encoded}", icon=":material/link:")
    st.write("Current state:")
    st.json(state)


# Very limited state management, no versioning, no validation
if "s" in st.query_params:
    state_decoded = url_serde.decode(st.query_params["s"])
    st.session_state.update(state_decoded)

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

about = """
This project demonstrates how to leverage the built-in power of Streamlit using best software engineering practices
and tools.
It provides a non-trivial Streamlit application skeleton, showcasing how to effectively utilize Streamlit's
capabilities and address its limitations.
See [README](https://github.com/mkuthan/example-streamlit/blob/main/README.md) for more details.
"""

get_help = "https://discuss.streamlit.io/t/non-trivial-application-skeleton-from-seasoned-software-data-engineer/86072"
report_bug = "https://github.com/mkuthan/example-streamlit/issues/new"

st.set_page_config(
    page_title="Streamlit Non-Trivial App",
    page_icon="https://streamlit.io/images/brand/streamlit-mark-color.png",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "About": about,
        "Get Help": get_help,
        "Report a bug": report_bug,
    },
)

st.logo("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", size="large")

# Reduce top padding from 5rem to 2rem
st.markdown(
    """
<style>
section.stMain .block-container {
    padding-top: 2rem;
}
</style>""",
    unsafe_allow_html=True,
)

if not st.session_state.logged_in:
    login_page = st.Page("example/ui/pages/login_page.py", title="Log in", icon=":material/login:")

    pg = st.navigation(pages=[login_page])
else:
    home = st.Page("example/ui/pages/home_page.py", title="Home", icon=":material/home:", default=True)
    nyt_tlc_trips = st.Page("example/ui/pages/ny_tlc_trips_page.py", title="NY Taxi Trips", icon=":material/local_taxi:")

    pg = st.navigation(pages=[home, nyt_tlc_trips])

    if st.sidebar.button("Share", icon=":material/link:"):
        share(pg.url_path)

    if st.sidebar.button("Log out", icon=":material/person:"):
        authenticator.logout()

pg.run()
