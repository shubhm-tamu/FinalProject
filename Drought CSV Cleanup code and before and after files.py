import pandas

def format_date(df):
    df['MapDate'] = pd.to_datetime(df['MapDate'], format='%Y%m%d').dt.strftime('%Y/%m/%d')
    return df


def date_to_month(df):
    df['MapDate'] = pd.to_datetime(df['MapDate'], format='%Y/%m/%d').dt.month_name()
    return df



def Average_Percents(df):
    df[['None', 'D0', 'D1', 'D2', 'D3', 'D4']] = df[['None', 'D0', 'D1', 'D2', 'D3', 'D4']].apply(pd.to_numeric, errors='coerce')
    df = df.groupby(['MapDate', 'County'])[['None', 'D0', 'D1', 'D2', 'D3', 'D4']].mean().reset_index()
    return df


def Order_Columns(df):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df['MapDate'] = pd.Categorical(df['MapDate'], categories=months, ordered=True)
    df = df.sort_values(['County', 'MapDate'])
    return df

import pandas as pd

df = pd.read_csv('County_percentage_of_area_Categorical.csv')

df = format_date(df)

df = date_to_month(df)

df = Average_Percents(df)

df = Order_Columns(df)

df.to_csv('updated_County_percentage_of_area_Categorical.csv', index=False)
