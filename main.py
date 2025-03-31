from dotenv import load_dotenv
import os
load_dotenv()
from scripts.extract import extract_weather_data
from scripts.transform import transform_weather_data
from scripts.load import load_weather_data

API_KEY = os.getenv('WEATHER_API_KEY')
CITY = 'London'

# Extract
df = extract_weather_data(API_KEY, CITY)

# Transform
df = transform_weather_data(df)

# Load
load_weather_data(df)

print("ETL process completed successfully!")
