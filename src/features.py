import pandas as pd
def add_lag_features(df,lags=(1,24)):
    df=df.copy()
    for l in lags:
        for c in ['demand','gen','price']:
            df[f'{c}_lag_{l}']=df.groupby('zone')[c].shift(l)
    return df.dropna()
def train_test_split_time(df,split_year=2023):
    return df[df.timestamp.dt.year<split_year],df[df.timestamp.dt.year>=split_year]