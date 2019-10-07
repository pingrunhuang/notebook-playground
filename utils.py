import pandas_datareader as data

SOURCE = "yahoo"

def get_stock_df(stock, start_date='2010-01-01', end_date='2016-12-31'):
    return data.DataReader(stock, SOURCE, start=start_date, end=end_date)