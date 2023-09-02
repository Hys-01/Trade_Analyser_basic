import requests
import pandas as pd
from config import API_KEY
import numpy as np

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
        data = pd.DataFrame(response.json())
    else:
        # if there is an error retrieving the data
        print(f"Failed to get data from Tiingo API. Status code: {response.status_code}. Response: {response.content}")
    return data

def prepare_data(data):
    '''
    Prepares the dataframe by changing the date datatype to datetime format. 

    inputs:    
        data: dataframe
    Outputs: 
        data: dataframe (edited)

    '''
    df = data
    df['date'] = pd.to_datetime(df['date'])
    df['date_delta'] = (df['date'] - df['date'].min())  / np.timedelta64(1,'D')
    return data


def calculate_moving_averages(data, windows=[5,10,50,100,200]):
    '''
    creates new columns in the dataframe.
    Closing prices are used to calculate moving averages. 
    This is done for various periods from 5 to 200.

    input: 
        data: prepared dataframe
        windows: a list of values representing the periods

    output: 
        data: the dataframe object filtered to show the closing price and moving averages
    '''
    for window in windows:
        data[f'{window}-day m.avg'] = data['close'].rolling(window).mean()
    return data
        



