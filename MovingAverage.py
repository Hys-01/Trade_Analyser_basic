import requests
import pandas as pd
from config import API_KEY
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics

class MovingAverage: 
    def __init__(self, symbol, api_key):
        self.symbol = symbol
        self.api_key = api_key
        self.model = None
        self.data = None
        self.X = None
        self.y = None
        self.poly = None

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
        else:
            # if there is an error retrieving the data
            print(f"Failed to get data from Tiingo API. Status code: {response.status_code}. Response: {response.content}")

    def prepare_data(self):
        '''
        Prepares the dataframe by changing the date datatype to datetime format. 
        '''
        df = self.data
        df['date'] = pd.to_datetime(df['date'])
        df['date_delta'] = (df['date'] - df['date'].min())  / np.timedelta64(1,'D')

        # Set X and y for future model training
        self.X = df['date_delta'].values.reshape(-1,1)
        self.y = df['close'].values.reshape(-1,1)


    def calculate_moving_averages(self, window_short_1=5, window_short_2=20,  window_long_1=50, window_long_2=100, window_long_3=200):
        '''
        creates new columns in the dataframe.
        Closing prices are used to calculate moving averages. 
        This is done for various periods from 5 to 200.

        input: 
            window_short_1: integer constant of 5
            window_short_2: integer constant of 20
            window_long_1: integer constant of 50
            window_long_2: integer constant of 100
            window_long_3: integer constant of 200

        output: 
            self.data: the dataframe object filtered to show the closing price and moving averages
        '''
        
        self.data['very short m.avg'] = self.data['close'].rolling(window_short_1).mean()
        self.data['short m.avg'] = self.data['close'].rolling(window_short_2).mean()
        self.data['medium m.avg'] = self.data['close'].rolling(window_long_1).mean()
        self.data['long m.avg'] = self.data['close'].rolling(window_long_2).mean()
        self.data['very long m.avg'] = self.data['close'].rolling(window_long_3).mean()
        # for testing purposes
        print(self.data[['date','close','very short m.avg', 'short m.avg', 'medium m.avg', 'long m.avg', 'very long m.avg']])
        

    def show_graph(self):
        pass


