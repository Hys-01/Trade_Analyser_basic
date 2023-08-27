import unittest
from MovingAverage import MovingAverage
from config import API_KEY
from datetime import date, datetime

def test_very_short_mavg(start_date, end_date, symbol): 
    '''
    This function tests the dataframe values for very short moving average. 

    inputs: 
        
    outputs: 
        

    '''
    mavg_data = MovingAverage(symbol, api_key=API_KEY)
    mavg_data.retrieve_data(start_date, end_date)
    mavg = mavg_data.calculate_moving_averages()


if __name__ == "__main__": 
    symbol='TSLA'
    mavgfunction = moving_averages("2020-01-01", date.today(), symbol)
    print(mavgfunction)

