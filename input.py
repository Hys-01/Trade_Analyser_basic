from modeltrain import PolyRegression
from config import TIINGO_API_KEY

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
    start_date= '2019-01-01'
    end_date='2023-06-17'
    symbol='NVDA'

    #execute(start_date, end_date, symbol)
    #trading_volume(start_date, end_date, symbol)