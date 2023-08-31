# document to store unused code

'''
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
'''



'''import requests
import pandas as pd
from config import TIINGO_API_KEY

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics

# NASDAQ abbreviation for stock
symbol = 'NVDA'

# Start and end dates for which you want data in datetime format YYYY
start_date = '2019-01-01'
end_date = '2023-06-17'

# Make a request to the Tiingo API
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Token {TIINGO_API_KEY}'
}
url = f'https://api.tiingo.com/tiingo/daily/{symbol}/prices?startDate={start_date}&endDate={end_date}'

response = requests.get(url, headers=headers)
if response.status_code == 200:
    # Parse the JSON response into a DataFrame
    data = pd.DataFrame(response.json())
    # Print the DataFrame
    print(data)
else:
    print(f"Failed to get data from Tiingo API. Status code: {response.status_code}. Response: {response.content}")

df = data
df['date'] = pd.to_datetime(df['date'])
df['date_delta'] = (df['date'] - df['date'].min())  / np.timedelta64(1,'D')

# Use date_delta as our feature and close as our target
X = df['date_delta'].values.reshape(-1,1)
y = df['close'].values.reshape(-1,1)

# Split data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Transform matrix of features into matrix of higher order (polynomial) features
poly = PolynomialFeatures(degree = 4)
X_poly = poly.fit_transform(X_train)

# Fit into Linear Regression model
model = LinearRegression()
model.fit(X_poly, y_train)

# Visualizing the Polynomial Regression results
plt.scatter(X, y, color='grey')
plt.plot(X, model.predict(poly.fit_transform(X)), color='blue')
plt.title('Polynomial Prediction')
plt.xlabel('Date')
plt.ylabel('Stock CLOSE Price')
plt.show()'''