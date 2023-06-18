import requests
import pandas as pd
from config import TIINGO_API_KEY

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics

class PolyRegression: 
    def __init__(self, symbol, api_key):
        self.symbol = symbol
        self.api_key = api_key
        self.model = None
        self.data = None
        self.X = None
        self.y = None
        self.poly = None

    def retreive_data(self, start_date, end_date):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Token {self.api_key}'
        }
        url = f'https://api.tiingo.com/tiingo/daily/{self.symbol}/prices?startDate={start_date}&endDate={end_date}'

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # Parse the JSON response into a DataFrame
            self.data = pd.DataFrame(response.json())
        else:
            print(f"Failed to get data from Tiingo API. Status code: {response.status_code}. Response: {response.content}")

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
        self.poly = PolynomialFeatures(degree = 6)
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
