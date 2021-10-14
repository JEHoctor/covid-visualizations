import pandas as pd

from covid.data_loaders import get_historic_states_data

class TestDataLoaders:

    def test_get_historic_states_data(self):
        df = get_historic_states_data()

        assert isinstance(df, pd.DataFrame)
