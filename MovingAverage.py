import requests
import pandas as pd
import numpy as np

class MovingAverage:
    def __init__(self, api_key):
        self.api_key = api_key
        self.data = None

    def retrieve_data(self, start_date, end_date, symbol):
        '''
        Retrieves data from the TIIGO API and turns it into a dataframe.

        inputs: 
            start_date: the lower bound of the data
            end_date: upper bound of the data
        '''
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Token {self.api_key}'
        }
        url = f'https://api.tiingo.com/tiingo/daily/{symbol}/prices?startDate={start_date}&endDate={end_date}'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # Parse the JSON response into a DataFrame if the response is valid
            self.data = pd.DataFrame(response.json())
        else:
            # if there is an error retrieving the data
            print(f"Failed to get data from Tiingo API. Status code: {response.status_code}. Response: {response.content}")

    def prepare_data(self):
        '''
        Prepares the dataframe by changing the date datatype to datetime format.
        '''
        if self.data is not None:
            self.data['date'] = pd.to_datetime(self.data['date'])
            self.data['date_delta'] = (self.data['date'] - self.data['date'].min()) / np.timedelta64(1, 'D')

    def calculate_moving_averages(self, windows=[5, 10, 50, 100, 200]):
        '''
        Creates new columns in the dataframe.
        Closing prices are used to calculate moving averages.
        This is done for various periods from 5 to 200.

        input:
            windows: a list of values representing the periods
        '''
        if self.data is not None:
            for window in windows:
                # create a new column representing the moving averages (based off closing price) for each period value in windows
                self.data[f'{window}-day m.avg'] = self.data['close'].rolling(window).mean()  

        



