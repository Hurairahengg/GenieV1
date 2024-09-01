import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def download_market_data(symbol, start_datetime, end_datetime, interval, output_file):
    try:
        # Adjust end datetime for the interval to ensure we get data until the end time
        adjusted_end_datetime = end_datetime + timedelta(minutes=int(interval[:-1]))

        # Download the market data
        data = yf.download(symbol, start=start_datetime, end=adjusted_end_datetime, interval=interval)
        
        if data.empty:
            print(f"No data found for {symbol} from {start_datetime} to {end_datetime} with interval {interval}")
        else:
            # Filter data to the exact time range
            data = data.between_time(start_datetime.time(), end_datetime.time())
            # Save the data to a CSV file
            data.to_csv(output_file)
            print(f"Market data for {symbol} from {start_datetime} to {end_datetime} saved to {output_file}")
    except Exception as e:
        print(f"Failed to download data for {symbol}: {e}")

if __name__ == "__main__":
    # Constants
    symbol = 'MXN=X'
    start_datetime = datetime(2024, 7, 26, 14, 10)  # 2024-07-15 4:00 PM
    end_datetime = datetime(2024, 7, 26, 20, 50)    # 2024-07-15 6:45 PM
    interval = '5m'
    output_file = 'market_data.csv'
    
    # Download the market data and save to CSV
    download_market_data(symbol, start_datetime, end_datetime, interval, output_file)
