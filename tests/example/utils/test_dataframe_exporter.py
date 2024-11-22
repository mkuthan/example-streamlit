import io

import pandas as pd
import pytest

from example.utils import dataframe_exporter


@pytest.fixture
def any_dataframe():
    return pd.DataFrame(
        {
            "column1": ["value1", "value2", "value3"],
            "column2": [10, 20, 30],
        }
    )


def test_export_to_csv(any_dataframe):
    csv_bytes = dataframe_exporter.export_to_csv(any_dataframe)
    dataframe = pd.read_csv(io.BytesIO(csv_bytes))

    assert dataframe.equals(any_dataframe)


def test_export_to_xls(any_dataframe):
    xls_bytes = dataframe_exporter.export_to_xls(any_dataframe)
    dataframe = pd.read_excel(io.BytesIO(xls_bytes))

    assert dataframe.equals(any_dataframe)
