import io
import os

import pandas as pd

import requests


COVID_ACT_NOW_API_KEY = os.getenv("COVID_ACT_NOW_API_KEY")

HISTORIC_STATES_URL = (
    "https://api.covidactnow.org/v2/states.timeseries.csv?apiKey="
    + COVID_ACT_NOW_API_KEY
)
HISTORIC_COUNTIES_URL = (
    "https://api.covidactnow.org/v2/counties.timeseries.csv?apiKey="
    + COVID_ACT_NOW_API_KEY
)
HISTORIC_METROS_URL = (
    "https://api.covidactnow.org/v2/cbsas.timeseries.csv?apiKey="
    + COVID_ACT_NOW_API_KEY
)


def get_historic_states_data():
    r = requests.get(HISTORIC_STATES_URL)
    if r.status_code != 200:
        raise RuntimeError(f"Download failure: received status {r.status_code}")

    buf = io.StringIO(r.text)
    try:
        df = pd.read_csv(buf)
    finally:
        buf.close()

    df["date"] = pd.to_datetime(df["date"])

    return df
