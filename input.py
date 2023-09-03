from MovingAverage import *
from config import API_KEY as api_key
from datetime import date, datetime
def user_input_dates(): 
    '''
    Retrieves custom boundaries for data from user. 
    Probes for lower bound date, and upper bound date

    outputs: 
        start_date: string that represents lower bnound for data
        end_date: string that represents upper bound for data
    
    start_date = input('START date of data (yyyy-mm-dd): ')  
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        print("yyyy-mm-dd for date inputs please")

    # probe user input, if they want the upper bound of data to be today's date or custom.
    user_todayyn = input("Do you wish to retreive data up to today's date? (y/n): ")
    if user_todayyn.upper() == 'Y': 
        end_date = date.today()
    elif user_todayyn.upper() == 'N':
        end_date = input('END date of data? (yyyy-mm-dd): ') 
    else: 
        print('its either YES or NO.')  
    '''
    return '2022-01-01', '2023-01-01'


def moving_averages(start_date, end_date, symbol, api_key):
    '''
    This function receives input from the user for lower and upper bound for data. 

    outputs: 
        ma: self.data including the moving average columns. 

    '''
def moving_averages(start_date, end_date, symbol, api_key):

    ma = MovingAverage(api_key)
    ma.retrieve_data(start_date, end_date, symbol)
    ma.prepare_data()
    ma.calculate_moving_averages()
    return ma                         

if __name__ == "__main__":
    start_date, end_date = user_input_dates()
    
    symbol='TSLA'
    mavgfunction = moving_averages(start_date, end_date, symbol, api_key)


