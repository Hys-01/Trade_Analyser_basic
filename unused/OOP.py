import requests
import pandas as pd
from config import API_KEY
import numpy as np
import matplotlib.pyplot as plt

class MovingAverage: 
    def __init__(self, symbol, api_key):
        self.symbol = symbol
        self.api_key = api_key

        self.data = None

    def retrieve_data(self, start_date, end_date):
        '''
        Retrieves data from the TIIGO API and turns it into a dataframe.
        inputs: 
            start_date: the lower bound of the data
            end_date: upper bound of the data
        outputs:
            self.data as a pandas dataframe
        '''
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Token {self.api_key}'
        }
        url = f'https://api.tiingo.com/tiingo/daily/{self.symbol}/prices?startDate={start_date}&endDate={end_date}'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # Parse the JSON response into a DataFrame if the response is valid
            self.data = pd.DataFrame(response.json())
            print('SONGGONG')
            return self.data
        else:
            # if there is an error retrieving the data
            print(f"Failed to get data from Tiingo API. Status code: {response.status_code}. Response: {response.content}")


from config import API_KEY
from datetime import date, datetime
def moving_averages(start_date, end_date, symbol):

    ma = MovingAverage(symbol, API_KEY)
    ma.retrieve_data(start_date, end_date)
    return ma


if __name__ == "__main__":

    
    symbol='TSLA'
    mavgfunction = moving_averages('2020-01-01','2023-01-01', symbol)
    print(mavgfunction)
