# covid-visualizations
This is an exploration of data available from the [Covid Act Now API](https://apidocs.covidactnow.org/).

## API Key

After aquiring an API key as described on the Covid Act Now page, store it in an environment variable as shown below.

```bash
$ export COVID_ACT_NOW_API_KEY=YOUR_KEY_HERE
```

Then, in the same bash session, run a python interpreter in the root directory of this repository.

```python
>>> import data
>>> df = data.get_historic_states_data()
```
