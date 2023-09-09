import unittest
from MovingAverage import MovingAverage
from config import API_KEY
from datetime import date, datetime, timedelta

def test_data(start_date, end_date, symbol): 
    '''
    This function tests the dataframe values for very short moving average. 

    inputs: 
        
    outputs: 
        

    '''
    mavg_data = MovingAverage(api_key=API_KEY)
    mavg_data.retrieve_data(start_date, end_date, symbol)
    mavg_data.prepare_data()
    mavg_data.calculate_moving_averages()

    a = mavg_data.data['date']
    print((a))
    

    result_date = date.today() - timedelta(days=20)
    print(result_date)




if __name__ == "__main__": 
    symbol='TSLA'
    mavgfunction = test_data("2020-01-01", date.today(), symbol)
    print(mavgfunction)

