import pandas as pd
import streamlit as st

from example.utils import dataframe_exporter

_CSV_MIME_TYPE = "text/csv"
_XLSX_MIME_TYPE = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"


def show_export_csv(df: pd.DataFrame, filename: str) -> bool:
    data = dataframe_exporter.export_to_csv(df)
    return st.download_button("Export CSV", data, filename, _CSV_MIME_TYPE)


def show_export_excel(df: pd.DataFrame, filename: str) -> bool:
    data = dataframe_exporter.export_to_xls(df)
    return st.download_button("Export XLS", data, filename, _XLSX_MIME_TYPE)
