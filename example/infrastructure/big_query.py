import pandas as pd
from google.cloud import bigquery


# TODO: add error handling, define timeouts, etc.
def query(q: str, params: dict = None) -> pd.DataFrame:
    client = __get_client()

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            # TODO: add support for other types
            bigquery.ScalarQueryParameter(name, "STRING", value)
            for name, value in (params or {}).items()
        ]
    )
    results = client.query(q, job_config=job_config)
    return results.to_dataframe()


def __get_client() -> bigquery.Client:
    # TODO: add authentication
    return bigquery.Client()
