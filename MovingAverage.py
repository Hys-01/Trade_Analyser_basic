import requests
import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta

class MovingAverage:
    def __init__(self, api_key):
        self.api_key = api_key
        self.data = None

    def retrieve_data(self, start_date, end_date, symbol):
        '''
        Retrieves data from the Financial Modeling Prep API and turns it into a DataFrame.

        inputs: 
            start_date: the lower bound of the data
            end_date: upper bound of the data
            symbol: the stock symbol or identifier
        '''
        base_url = 'https://financialmodelingprep.com/api/v3'
        endpoint = f'/historical-price-full/{symbol}'
        params = {
            'apikey': self.api_key,
            'from': start_date,
            'to': end_date,
        }

        response = requests.get(base_url + endpoint, params=params)

        if response.status_code == 200:
            # Parse the JSON response into a DataFrame if the response is valid
            data = response.json()
            if 'historical' in data:
                self.data = pd.DataFrame(data['historical'])
            else:
                print(f"No historical data found for symbol {symbol}.")
        else:
            # if there is an error retrieving the data
            print(f"Failed to get data from Financial Modeling Prep API. Status code: {response.status_code}. Response: {response.content}")

    def prepare_data(self):
        '''
        Prepares the dataframe by changing the date datatype to datetime format and sorts by date
        '''
        if self.data is not None:
            self.data['date'] = pd.to_datetime(self.data['date'], format='%Y-%m-%d')
        
        self.data = self.data.sort_values(by='date')

        self.test_prepare()



    def simple_moving_averages(self, windows):
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
                self.data[f'{window} day SMA'] = self.data['close'].rolling(window).mean()  


                # NOTE: CALLING METHODS FROM ANOTHER METHOD WITHIN SHARED CLASS NEEDS SELF.METHOD()
                #self.test_simple_ma(window)   

    def exp_moving_averages(self, windows):
        '''
        Creates new columns in the dataframe for exponential moving averages.
        Closing prices are used to calculate EMAs.

        input:
            windows: a list of values representing the periods
        '''
        if self.data is not None:
            for window in windows:
                # create a new column representing the EMA for each period value in windows
                self.data[f'{window} day EMA'] = self.data['close'].ewm(span=window, adjust=False).mean()

    # TODO - doubt this will be needed but try to insert it into simple_ma() function anyway
    def test_prepare(self):
        try:
            # check the data type of the date column, ensure it is datetime not object
            if type(self.data['date']) == type(datetime.strptime("2020-01-01", "%Y-%m-%d")):
                return True
            else: 
                return False
        except AttributeError:
            # catch if the date column is NOT a pandas series
            return False


        
    def test_simple_ma(self, period):
        u = datetime.today()
        l = u - timedelta(days=period)

        relevant = self.data[  (self.data['date']>=l)&(self.data['date'] <= u)  ]
        manualma = (sum(relevant['close']))/(relevant['close'].count())
        print(manualma, self.data[f'{period} day SMA'])

        