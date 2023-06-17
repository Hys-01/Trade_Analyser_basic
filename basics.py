import requests
import pandas as pd
from config import TIINGO_API_KEY


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
