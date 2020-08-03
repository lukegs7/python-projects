import os
import tushare as ts
import pandas as pd

ts.set_token('2a502c019dd831077592283439e635b8a843b43da1ff16dfe53646b4')
pro = ts.pro_api()
def get_stock_list():
    if not os.path.exists('data/stock_list.csv'):
        data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
        df = pd.DataFrame(data=data)
        print(df.columns)
        df.to_csv('data/stock_list.csv', index=False, encoding='utf-8')
    else:
        df = pd.read_csv('data/stock_list.csv')
    return df

def single_stock():
    df = pro.daily(ts_code='000001.SZ', start_date='2010701', end_date='20200730')
    print(df.shape)

if __name__ == '__main__':
    single_stock()

