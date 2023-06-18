from modeltrain import PolyRegression
from config import TIINGO_API_KEY

def execute(start_date, end_date, symbol): 
    poly_model = PolyRegression(symbol=symbol, api_key=TIINGO_API_KEY)
    poly_model.retreive_data(start_date=start_date, end_date=end_date)
    poly_model.prepare_data()
    poly_model.train_model()
    poly_model.show_model()

if __name__ == "__main__":
    execute(start_date='2019-01-01', end_date='2023-06-17', symbol='NVDA')