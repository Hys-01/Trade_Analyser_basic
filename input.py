from modeltrain import PolyRegression
from config import TIINGO_API_KEY
from datetime import date, datetime
def execute(start_date, end_date, symbol): 
    poly_model = PolyRegression(symbol=symbol, api_key=TIINGO_API_KEY)
    poly_model.retreive_data(start_date=start_date, end_date=end_date)
    poly_model.prepare_data()
    poly_model.train_model()
    poly_model.show_model()

def trading_volume(start_date, end_date, symbol): 
    tvol = PolyRegression(symbol=symbol, api_key=TIINGO_API_KEY)
    data = tvol.retreive_data(start_date=start_date, end_date=end_date)

    if data is None: 
        print('ERROR')
    else:
        print(data['volume'])

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
    
    symbol='NVDA'
    #execute(start_date, end_date, symbol)
    #trading_volume(start_date, end_date, symbol)