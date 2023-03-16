from flask import Flask, jsonify, render_template
import requests
import datetime
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
COINBASE_API_URL = "https://api.coinbase.com/v2/prices/BTC-USD/spot"



app = Flask(__name__, static_url_path='/assets', static_folder='assets')

@app.route('/', methods=['GET'])
def index():
    return render_template('/index.html')

# Define the data for Bitcoin
bitcoin = {
    'name': 'Bitcoin',
    'symbol': 'BTC',
    'price': 49832.13
}

# Define the route for Bitcoin
@app.route('/bitcoin', methods=['GET'])
def bitcoin():
    return render_template('bitcoin.html')

# @app.route('/bitcoin', methods=['GET'])
# def bitcoin():
#     return render_template('bitcoin.html', bitcoin=bitcoin)



@app.route('/ethereum', methods=['GET'])
def ethereum():
    return jsonify({'name': 'Ethereum', 'symbol': 'ETH', 'price': 1500.00})

@app.route('/ripple', methods=['GET'])
def ripple():
    return jsonify({'name': 'Ripple', 'symbol': 'XRP', 'price': 0.50})

@app.route('/dogecoin', methods=['GET'])
def dogecoin():
    return jsonify({'name': 'Dogecoin', 'symbol': 'DOGE', 'price': 0.05})

@app.route('/litecoin', methods=['GET'])
def litecoin():
    return jsonify({'name': 'Litecoin', 'symbol': 'LTC', 'price': 200.00})

@app.route('/getcryptodata', methods=['GET'])
def getcryptodata():
    response = requests.get(url)
    data = response.json()
    priceOfCoin = data['bpi']['USD']['rate']
    priceOfCoinFloat = round(float(priceOfCoin.replace(',', '')),2)
    return jsonify({'name': 'Ethereum', 'symbol': 'ETH', 'price': priceOfCoinFloat})


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

@app.route('/getmarkettype', methods=['GET'])
def getmarkettype():
    # Define historical data variables
    btc3MonthsAgoPrice = 90000  # example value
    btc6MonthsAgoPrice = 150000  # example value

    # Fetch current Bitcoin price from Coindesk API using requests
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    btcCurrentPrice = response.json()['bpi']['USD']['rate_float']

    # Calculate percentage change over past 3 and 6 months
    btc3MonthPercentChange = ((btcCurrentPrice - btc3MonthsAgoPrice) / btc3MonthsAgoPrice) * 100
    btc6MonthPercentChange = ((btcCurrentPrice - btc6MonthsAgoPrice) / btc6MonthsAgoPrice) * 100

    # Determine market type based on rules
    if btc3MonthPercentChange > 35 and btc6MonthPercentChange > 100:
        print('Bull market')
        marketTypeFinal = "Bull Market"
    elif btc3MonthPercentChange < -35 and btc6MonthPercentChange < -50:
        print('Bear market')
        marketTypeFinal = "Bear Market"
    elif -35 <= btc3MonthPercentChange <= 35 and -50 <= btc6MonthPercentChange <= 50:
        print('Neutral market')
        marketTypeFinal = "Neutral Market"
    else:
        print('Market type is difficult to predict')
        marketTypeFinal = "Neutral Market"
    return jsonify(marketTypeFinal)





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