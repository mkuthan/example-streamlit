import pandas as pd
import polars as pl
from google.cloud import bigquery


def query(q: str) -> pd.DataFrame:
    client = __get_client()
    # TODO: add error handling, define timeouts, etc.
    results = client.query(q).to_arrow()
    return pl.from_arrow(results)


def __get_client() -> bigquery.Client:
    # TODO: add authentication
    return bigquery.Client()
