import pandas as pd
import streamlit as st

st.title("Home")
st.write("Page with navigation, filters and search results")

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
    * i
    * j
    * k
    * l
    * m
    """
    st.caption("Navigation")
    st.markdown(navigation_items)

with center:
    with st.container():
        st.caption("Filters")
        st.text_input("Search")
        st.multiselect("Options", ["a", "b", "c", "d", "e", "f", "g", "h"])
        st.toggle("Include inactive")

    st.divider()

    with st.container():
        st.caption("Search results")
        sample_data = pd.DataFrame(
            {
                "A": [1, 2, 3, 4],
                "B": [10, 20, 30, 40],
                "C": [100, 200, 300, 400],
                "D": [1000, 2000, 3000, 4000],
                "E": [10000, 20000, 30000, 40000],
                "F": [100000, 200000, 300000, 400000],
                "G": [1000000, 2000000, 3000000, 4000000],
            }
        )

        st.dataframe(sample_data)
