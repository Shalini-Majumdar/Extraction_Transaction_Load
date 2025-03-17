from sqlalchemy import create_engine

def load_weather_data(df):
    engine = create_engine('sqlite:///data/processed/weather_data.sqlite')
    df.to_sql('weather', engine, if_exists='replace', index=False)
    df.to_csv('data/processed/weather_data.csv', index=False)