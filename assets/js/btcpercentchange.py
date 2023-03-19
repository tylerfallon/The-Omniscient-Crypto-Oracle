import requests
import datetime

COINBASE_API_URL = "https://api.coinbase.com/v2/prices/BTC-USD/spot"

# Get the current price
response = requests.get(COINBASE_API_URL)
response.raise_for_status()
data = response.json()
current_price = float(data['data']['amount'])

# Get yesterday's date and time
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
yesterday_iso = yesterday.isoformat()

# Get yesterday's price
historical_price_url = f"{COINBASE_API_URL}?date={yesterday_iso}"
response = requests.get(historical_price_url)
response.raise_for_status()
data = response.json()
yesterday_price = float(data['data']['amount'])

# Calculate the percent change
percent_change = ((current_price - yesterday_price) / yesterday_price) * 100

# Display the percent change
print(f"Bitcoin percent change from yesterday to today: {percent_change:.2f}%")