from flask import Flask, jsonify, render_template
import requests
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'


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

@app.route('/getcryptodata', methods=['GET'])
def getcryptodata():
    response = requests.get(url)
    data = response.json()
    priceOfCoin = data['bpi']['USD']['rate']
    priceOfCoinFloat = round(float(priceOfCoin.replace(',', '')),2)
    return jsonify({'name': 'Ethereum', 'symbol': 'ETH', 'price': priceOfCoinFloat})

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

if __name__ == '__main__':
    app.run(port=4000, debug=True)