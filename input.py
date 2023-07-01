from modeltrainv2 import PolyRegressionv2
from config import API_KEY
from datetime import date, datetime
def execute(start_date, end_date, symbol): 
    poly_model = PolyRegressionv2(symbol=symbol, api_key=API_KEY)
    poly_model.retrieve_data(start_date=start_date, end_date=end_date)
    poly_model.prepare_data()
    poly_model.train_model()
    poly_model.show_model()
    mavg = poly_model.calculate_moving_averages()
    print (mavg)

def trading_volume(start_date, end_date, symbol): 
    tvol = PolyRegressionv2(symbol=symbol, api_key=API_KEY)
    data = tvol.retrieve_data(start_date=start_date, end_date=end_date)

    if data is None: 
        print('ERROR')
    else:
        print(data['volume'])

def retrieve_data(start_date, end_date, symbol): 
    datac = PolyRegressionv2(symbol=symbol, api_key=API_KEY)
    data = datac.retrieve_data(start_date=start_date, end_date=end_date)
    return data

if __name__ == "__main__":
    start_date = input('START date of data (yyyy-mm-dd): ')  
    if datetime.strptime(start_date, '%Y-%m-%d') is False: 
        print('[]')

    user_todayyn = input("Do you wish to retreive data up to today's date? (y/n): ")
    if user_todayyn.upper() == 'Y': 
        end_date = date.today()
    elif user_todayyn.upper() == 'N':
        end_date = input('END date of data? (yyyy-mm-dd): ') 
    else: 
        print('its either YES or NO.')  
    
    symbol='TSLA'
    execute(start_date, end_date, symbol)
    #trading_volume(start_date, end_date, symbol)


    #df = retrieve_data(start_date, end_date, symbol)
    #print(max(df['high']))
