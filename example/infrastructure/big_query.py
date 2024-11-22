import pandas as pd
from google.cloud import bigquery

# Don't allow unbounded results to avoid OOM errors
_MAX_RESULTS = 100_000

# Limit the time a query can run to avoid long waits
_JOB_TIMEOUT_MS = 60_000

# Define labels for better query management
_JOB_LABELS = {"application": "example-streamlit"}


def query(q: str, params: dict = None) -> pd.DataFrame:
    client = __get_client()

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            # TODO: add support for other types
            bigquery.ScalarQueryParameter(name, "STRING", value)
            for name, value in (params or {}).items()
        ],
        job_timeout_ms=_JOB_TIMEOUT_MS,
        labels=_JOB_LABELS,
    )

    # Default timeout is None, but there is a good reason for that, see sources for more details.
    # Default retry and job_retry polices look good, so we don't need to change them.
    results = client.query(q, job_config=job_config)

    # Use regular Job instead of Storage API to avoid costs
    return results.to_dataframe(max_results=_MAX_RESULTS, create_bqstorage_client=False)


def __get_client() -> bigquery.Client:
    # TODO: add authentication
    return bigquery.Client()
