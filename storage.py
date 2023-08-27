    

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