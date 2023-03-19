from flask import Flask, jsonify, render_template
import requests
import datetime
COINBASE_API_URL = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
# url = 'https://api.coinbase.com/v2/prices/ETH-USD/spot'
# url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'
# url = 'https://api.coinbase.com/v2/prices/DOGE-USD/spot'
# url = 'https://api.coinbase.com/v2/prices/LTC-USD/spot'


app = Flask(__name__, static_url_path='/assets', static_folder='assets')

@app.route('/', methods=['GET'])
def index():
    return render_template('/index.html')

# # Define the data for Bitcoin
# bitcoin = {
#     'name': 'Bitcoin',
#     'symbol': 'BTC',
#     'price': 49832.13
# }

# Define the route for Bitcoin
@app.route('/bitcoin', methods=['GET'])
def bitcoin():
#    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    return render_template('bitcoin.html')

# @app.route('/bitcoin', methods=['GET'])
# def bitcoin():
#     return render_template('bitcoin.html', bitcoin=bitcoin)



@app.route('/ethereum', methods=['GET'])
def ethereum():
    return render_template('ethereum.html')

@app.route('/ripple', methods=['GET'])
def ripple():
    return render_template('ripple.html')

@app.route('/dogecoin', methods=['GET'])
def dogecoin():
    return render_template('dogecoin.html')

@app.route('/litecoin', methods=['GET'])
def litecoin():
    return render_template('litecoin.html')

@app.route('/getcryptodata', methods=['GET'])
def getcryptodata():
    url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'
    response = requests.get(url)
    data = response.json()
    priceOfCoin = data['data']['amount']
    priceOfCoinFloat = round(float(priceOfCoin), 2)
    return jsonify({'name': 'Bitcoin', 'symbol': 'BTC', 'price': priceOfCoinFloat})

@app.route('/getethdata', methods=['GET'])
def getethdata():
    url = 'https://api.coinbase.com/v2/prices/ETH-USD/spot'
    response = requests.get(url)
    data = response.json()
    priceOfCoin = data['data']['amount']
    priceOfCoinFloat = round(float(priceOfCoin), 2)
    return jsonify({'name': 'Ethereum', 'symbol': 'ETH', 'price': priceOfCoinFloat})

@app.route('/getdogedata', methods=['GET'])
def getdogedata():
    url = 'https://api.coinbase.com/v2/prices/DOGE-USD/spot'
    response = requests.get(url)
    data = response.json()
    priceOfCoin = data['data']['amount']
    priceOfCoinFloat = round(float(priceOfCoin), 2)
    return jsonify({'name': 'Dogecoin', 'symbol': 'DOGE', 'price': priceOfCoinFloat})

@app.route('/getltcdata', methods=['GET'])
def getltcdata():
    url = 'https://api.coinbase.com/v2/prices/LTC-USD/spot'
    response = requests.get(url)
    data = response.json()
    priceOfCoin = data['data']['amount']
    priceOfCoinFloat = round(float(priceOfCoin), 2)
    return jsonify({'name': 'Litecoin', 'symbol': 'LTC', 'price': priceOfCoinFloat})

@app.route('/getXRPdata', methods=['GET'])
def getXRPdata():
    url = 'https://api.kraken.com/0/public/Ticker?pair=XRPUSD'
    response = requests.get(url)
    data = response.json()
    priceOfCoin = data['result']['XXRPZUSD']['c'][0]
    priceOfCoinFloat = round(float(priceOfCoin), 2)
    return jsonify({'name': 'Ripple', 'symbol': 'XRP', 'price': priceOfCoinFloat})


@app.route('/getpercentchange', methods=['GET'])
def getpercentchange():
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
    percent_change_rounded = f"{percent_change:.2f}"
    return jsonify({'name': 'Ethereum', 'symbol': 'ETH', 'price': percent_change_rounded})
    # priceOfCoin = data['bpi']['USD']['rate']
    # priceOfCoinFloat = round(float(priceOfCoin.replace(',', '')),2)

@app.route('/getethpercentchange', methods=['GET'])
def getethpercentchange():
    # Get the current price
    url = 'https://api.coinbase.com/v2/prices/ETH-USD/spot'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    current_price = float(data['data']['amount'])
    # Get yesterday's date and time
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday_iso = yesterday.isoformat()
    # Get yesterday's price
    historical_price_url = f"{url}?date={yesterday_iso}"
    response = requests.get(historical_price_url)
    response.raise_for_status()
    data = response.json()
    yesterday_price = float(data['data']['amount'])
    # Calculate the percent change
    percent_change = ((current_price - yesterday_price) / yesterday_price) * 100
    # Display the percent change
    print(f"Ethereum percent change from yesterday to today: {percent_change:.2f}%")
    percent_change_rounded = f"{percent_change:.2f}"
    return jsonify({'name': 'Ethereum', 'symbol': 'ETH', 'price': percent_change_rounded})
    # priceOfCoin = data['bpi']['USD']['rate']
    # priceOfCoinFloat = round(float(priceOfCoin.replace(',', '')),2)


@app.route('/getltcpercentchange', methods=['GET'])
def getltcpercentchange():
    # Get the current price
    url = 'https://api.coinbase.com/v2/prices/LTC-USD/spot'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    current_price = float(data['data']['amount'])
    # Get yesterday's date and time
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday_iso = yesterday.isoformat()
    # Get yesterday's price
    historical_price_url = f"{url}?date={yesterday_iso}"
    response = requests.get(historical_price_url)
    response.raise_for_status()
    data = response.json()
    yesterday_price = float(data['data']['amount'])
    # Calculate the percent change
    percent_change = ((current_price - yesterday_price) / yesterday_price) * 100
    # Display the percent change
    print(f"Litecoin percent change from yesterday to today: {percent_change:.2f}%")
    percent_change_rounded = f"{percent_change:.2f}"
    return jsonify({'name': 'Litecoin', 'symbol': 'LTC', 'price': percent_change_rounded})
    # priceOfCoin = data['bpi']['USD']['rate']
    # priceOfCoinFloat = round(float(priceOfCoin.replace(',', '')),2)

@app.route('/getdogepercentchange', methods=['GET'])
def getdogepercentchange():
    # Get the current price
    url = 'https://api.coinbase.com/v2/prices/DOGE-USD/spot'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    current_price = float(data['data']['amount'])
    # Get yesterday's date and time
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday_iso = yesterday.isoformat()
    # Get yesterday's price
    historical_price_url = f"{url}?date={yesterday_iso}"
    response = requests.get(historical_price_url)
    response.raise_for_status()
    data = response.json()
    yesterday_price = float(data['data']['amount'])
    # Calculate the percent change
    percent_change = ((current_price - yesterday_price) / yesterday_price) * 100
    # Display the percent change
    print(f"Litecoin percent change from yesterday to today: {percent_change:.2f}%")
    percent_change_rounded = f"{percent_change:.2f}"
    return jsonify({'name': 'Dogecoin', 'symbol': 'DOGE', 'price': percent_change_rounded})
    # priceOfCoin = data['bpi']['USD']['rate']
    # priceOfCoinFloat = round(float(priceOfCoin.replace(',', '')),2)

# @app.route('/getxrppercentchange', methods=['GET'])
# def getxrppercentchange():
#     # Get the current price
#     url = 'https://api.kraken.com/0/public/Ticker?pair=XRPUSD'
#     response = requests.get(url)
#     response.raise_for_status()
#     data = response.json()
#     current_price = float(data['data']['amount'])
#     # Get yesterday's date and time
#     yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
#     yesterday_iso = yesterday.isoformat()
#     # Get yesterday's price
#     historical_price_url = f"{url}?date={yesterday_iso}"
#     response = requests.get(historical_price_url)
#     response.raise_for_status()
#     data = response.json()
#     yesterday_price = float(data['data']['amount'])
#     # Calculate the percent change
#     percent_change = ((current_price - yesterday_price) / yesterday_price) * 100
#     # Display the percent change
#     print(f"Litecoin percent change from yesterday to today: {percent_change:.2f}%")
#     percent_change_rounded = f"{percent_change:.2f}"
#     return jsonify({'name': 'Dogecoin', 'symbol': 'DOGE', 'price': percent_change_rounded})
#     # priceOfCoin = data['bpi']['USD']['rate']
#     # priceOfCoinFloat = round(float(priceOfCoin.replace(',', '')),2)

@app.route('/getmarkettype', methods=['GET'])
def getmarkettype():
    # Set API endpoint and parameters for BTC price 3 months ago
    endpoint = 'https://api.coingecko.com/api/v3/coins/bitcoin/history'
    start_date_3_months_ago = datetime.datetime.now() - datetime.timedelta(days=90)
    params = {'date': start_date_3_months_ago.strftime('%d-%m-%Y')}

    # Make API request and get response
    response = requests.get(endpoint, params=params)

    # Parse response and get BTC price
    btc3MonthsAgoPrice = response.json()['market_data']['current_price']['usd']

    # Set API endpoint and parameters for BTC price 6 months ago
    endpoint = 'https://api.coingecko.com/api/v3/coins/bitcoin/history'
    start_date_6_months_ago = datetime.datetime.now() - datetime.timedelta(days=180)
    params = {'date': start_date_6_months_ago.strftime('%d-%m-%Y')}

    # Make API request and get response
    response = requests.get(endpoint, params=params)

    # Parse response and get BTC price
    btc6MonthsAgoPrice = response.json()['market_data']['current_price']['usd']

    # Fetch current Bitcoin price from Coindesk API using requests
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    btcCurrentPrice = response.json()['bpi']['USD']['rate_float']

    # Calculate percentage change over past 3 and 6 months
    btc3MonthPercentChange = ((btcCurrentPrice - btc3MonthsAgoPrice) / btc3MonthsAgoPrice) * 100
    btc6MonthPercentChange = ((btcCurrentPrice - btc6MonthsAgoPrice) / btc6MonthsAgoPrice) * 100

    # Determine market type based on rules
    if btc3MonthPercentChange > 45 and btc6MonthPercentChange > 100:
        marketTypeFinal = "Bull Market"
    elif btc3MonthPercentChange < -45 and btc6MonthPercentChange < -60:
        marketTypeFinal = "Bear Market"
    elif -45 <= btc3MonthPercentChange <= 45 and -60 <= btc6MonthPercentChange <= 60:
        marketTypeFinal = "Neutral Market"
    else:
        marketTypeFinal = "Market type is difficult to predict"
    return jsonify(marketTypeFinal)







    #return jsonify({'3 Month Change': btc3MonthPercentChange, '6 Month Change': btc6MonthPercentChange})
    # "3 Month Change": 42.078524506658724, 
    # "6 Month Change": 24.638586561060183

   





    # # Get the current price
    # response = requests.get(COINBASE_API_URL)
    # response.raise_for_status()
    # data = response.json()
    # current_price = float(data['data']['amount'])

    # # Get yesterday's date and time
    # yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    # yesterday_iso = yesterday.isoformat()

    # # Get yesterday's price
    # historical_price_url = f"{COINBASE_API_URL}?date={yesterday_iso}"
    # response = requests.get(historical_price_url)
    # response.raise_for_status()
    # data = response.json()
    # yesterday_price = float(data['data']['amount'])

    # # Calculate the percent change
    # percent_change = ((current_price - yesterday_price) / yesterday_price) * 100

    # # Display the percent change
    # print(f"Bitcoin percent change from yesterday to today: {percent_change:.2f}%")

    return jsonify({'name': 'Ethereum', 'symbol': 'ETH', 'price': priceOfCoinFloat})







if __name__ == '__main__':
    app.run(port=4000, debug=True)