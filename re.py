import pandas_datareader as web
import pandas as pd
import datetime
data=pd.DataFrame(web.get_data_yahoo(['GOOG','AAPL','FB','AMZN'])['Adj Close'])

print(data.plot())
