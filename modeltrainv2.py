import requests
import pandas as pd
from config import API_KEY
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics

class PolyRegressionv2: 
    def __init__(self, symbol, api_key):
        self.symbol = symbol
        self.api_key = api_key
        self.model = None
        self.data = None
        self.X = None
        self.y = None
        self.poly = None

    def retrieve_data(self, start_date, end_date):
        # FMP API doesn't need headers, so we remove them
        # Make sure your start and end dates are in the YYYY-MM-DD format
        url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{self.symbol}?from={start_date}&to={end_date}&apikey={self.api_key}"
        
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the JSON response into a DataFrame
            # Note that FMP nests the historical data under the 'historical' key
            self.data = pd.DataFrame(response.json()['historical'])
            return self.data
        else:
            print(f"Failed to get data from FMP API. Status code: {response.status_code}. Response: {response.content}")
    
    def prepare_data(self):
        df = self.data
        df['date'] = pd.to_datetime(df['date'])
        df['date_delta'] = (df['date'] - df['date'].min())  / np.timedelta64(1,'D')

        # Set X and y for future model training
        self.X = df['date_delta'].values.reshape(-1,1)
        self.y = df['close'].values.reshape(-1,1)
        return self.X, self.y

    def train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=0)

        # Transform matrix of features into matrix of higher order (polynomial) features
        self.poly = PolynomialFeatures(degree = 7)
        X_poly = self.poly.fit_transform(X_train)

        # Fit into Linear Regression model
        self.model = LinearRegression()
        self.model.fit(X_poly, y_train)

    def show_model(self):
        plt.scatter(self.X, self.y, color='grey', marker='.')
        plt.plot(self.X, self.model.predict(self.poly.fit_transform(self.X)), color='blue')
        plt.title('Polynomial Prediction')
        plt.xlabel('Date')
        plt.ylabel('Stock CLOSE Price')
        plt.show()

    def calculate_moving_averages(self, window_short_1=5, window_short_2=20):
        self.data['very short m.avg'] = self.data['close'].rolling(window_short_1).mean()
        self.data['short m.avg'] = self.data['close'].rolling(window_short_2).mean()
        return self.data


