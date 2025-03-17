# Weather Data ETL(Extraction Transform Load) Pipeline

## Project Overview
This project implements an ETL (Extract, Transform, Load) pipeline to fetch, process, and store weather data using the OpenWeatherMap API. The extracted data is transformed and stored in both an SQLite database and a CSV file for further analysis.

## Project Structure
```
data/
└── processed/
    ├── scripts/
    │   ├── extract.py   # Extracts weather data from OpenWeatherMap API
    │   ├── transform.py # Transforms and normalizes the data
    │   └── load.py      # Loads data into SQLite and CSV file
    ├── venv/           # Virtual environment (optional)
    ├── main.py         # Main script to run ETL process
    └── requirements.txt # List of dependencies
```

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/weather-etl.git
   cd weather-etl
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Update `API_KEY` and `CITY` in `main.py` with your OpenWeatherMap API key and desired city.
2. Run the ETL process:
   ```sh
   python main.py
   ```
3. The extracted, transformed, and stored data can be found in:
   - `data/processed/weather_data.sqlite` (SQLite database)
   - `data/processed/weather_data.csv` (CSV file)

## Functionality
- **Extract:** Fetches live weather data from OpenWeatherMap API.
- **Transform:** Cleans the data, categorizes temperature, and normalizes numerical values.
- **Load:** Saves processed data to an SQLite database and a CSV file.

## Dependencies
- `requests` - For API requests
- `pandas` - For data processing
- `sqlalchemy` - For database handling
- `scikit-learn` - For data normalization
- `python-dotenv` - For loading environment variables from a .env file

## Author
Shalini Majumdar (https://github.com/your-username)

