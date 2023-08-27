from MovingAverage import MovingAverage
from config import API_KEY
from datetime import date, datetime
def user_input_dates(): 
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

    return start_date, end_date

def moving_averages(start_date, end_date, symbol):
    '''
    This function receives input from the user for lower and upper bound for data. 

    outputs: 
        mavg: data with short and long term moving averages for each date in the data. 

    '''
    ma = MovingAverage(symbol, API_KEY)       # create a MovingAverage object
    ma.retrieve_data(start_date, end_date)    # retrieve data using specified dates as bounds
    ma.prepare_data()                         # prepare data
    ma.calculate_moving_averages()            # calcualte all periods moving averages
    return ma                           

'''def trading_volume(start_date, end_date, symbol): 
    tvol = MovingAverage(symbol=symbol, api_key=API_KEY)
    data = tvol.retrieve_data(start_date=start_date, end_date=end_date)

    if data is None: 
        print('ERROR')
    else:
        print(data['volume'])

def retrieve_data(start_date, end_date, symbol): 
    datac = MovingAverage(symbol=symbol, api_key=API_KEY)
    data = datac.retrieve_data(start_date=start_date, end_date=end_date)
    return data'''

if __name__ == "__main__":
    start_date, end_date = user_input_dates()
    
    symbol='TSLA'
    mavgfunction = moving_averages(start_date, end_date, symbol)

