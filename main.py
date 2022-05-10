import datetime
from datetime import end
import pandas_datareader.data as web

start = datetime.date(2019, 1, 1)
end = datetime.date(2020, 1, 1)

df_ntt = web.DataReader('9432.T',"yahoo",start,end)
df_kddi = web.DataReader('9433.T',"yahoo",start,end)
