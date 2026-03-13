import requests
import pandas as pd
def get_api_data(url):
    response =requests.get(url)
    data=response.json()
    return pd.DataFrame(data)