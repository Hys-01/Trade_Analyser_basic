from MovingAverage import MovingAverage
from config import API_KEY
from datetime import date, datetime
def moving_averages(start_date, end_date, symbol):
    '''
    This function receives input from the user for lower and upper bound for data. 

    outputs: 
        mavg: data with short and long term moving averages for each date in the data. 

    '''
    mavg_data = MovingAverage(symbol, api_key=API_KEY)
    mavg_data.retrieve_data(start_date, end_date)
    mavg = mavg_data.calculate_moving_averages()
    return mavg

def trading_volume(start_date, end_date, symbol): 
    tvol = MovingAverage(symbol=symbol, api_key=API_KEY)
    data = tvol.retrieve_data(start_date=start_date, end_date=end_date)

    if data is None: 
        print('ERROR')
    else:
        print(data['volume'])

def retrieve_data(start_date, end_date, symbol): 
    datac = MovingAverage(symbol=symbol, api_key=API_KEY)
    data = datac.retrieve_data(start_date=start_date, end_date=end_date)
    return data

if __name__ == "__main__":
    start_date = input('START date of data (yyyy-mm-dd): ')  
    if datetime.strptime(start_date, '%Y-%m-%d') is False: 
        print('[]')

    # probe user input, if they want the upper bound of data to be today's date or custom.
    user_todayyn = input("Do you wish to retreive data up to today's date? (y/n): ")
    if user_todayyn.upper() == 'Y': 
        end_date = date.today()
    elif user_todayyn.upper() == 'N':
        end_date = input('END date of data? (yyyy-mm-dd): ') 
    else: 
        print('its either YES or NO.')  
    
    symbol='TSLA'
    mavgfunction = moving_averages(start_date, end_date, symbol)
    print(mavgfunction)
    #trading_volume(start_date, end_date, symbol)


    #df = retrieve_data(start_date, end_date, symbol)
    #print(df)
