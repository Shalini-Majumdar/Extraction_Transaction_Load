import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def transform_weather_data(df):
    df.dropna(inplace=True)

    def categorize_temperature(temp):
        if temp < 0:
            return 'Freezing'
        elif 0 <= temp < 15:
            return 'Cold'
        elif 15 <= temp < 25:
            return 'Mild'
        else:
            return 'Hot'

    df['temperature_category'] = df['temperature'].apply(categorize_temperature)

    scaler = MinMaxScaler()
    df[['temperature', 'wind_speed']] = scaler.fit_transform(df[['temperature', 'wind_speed']])

    return df