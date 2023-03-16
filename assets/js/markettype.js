// Import Axios library
const axios = require('axios');

// Define historical data variables
const btc3MonthsAgoPrice = 10000; // example value
const btc6MonthsAgoPrice = 5000; // example value

// Fetch current Bitcoin price from Coindesk API using Axios
axios.get('https://api.coindesk.com/v1/bpi/currentprice.json')
  .then(response => {
    const btcCurrentPrice = response.data.bpi.USD.rate_float;

    // Calculate percentage change over past 3 and 6 months
    const btc3MonthPercentChange = ((btcCurrentPrice - btc3MonthsAgoPrice) / btc3MonthsAgoPrice) * 100;
    const btc6MonthPercentChange = ((btcCurrentPrice - btc6MonthsAgoPrice) / btc6MonthsAgoPrice) * 100;

    // Determine market type based on rules
    if (btc3MonthPercentChange > 35 && btc6MonthPercentChange > 100) {
      console.log('Bull market');
    } else if (btc3MonthPercentChange < -35 && btc6MonthPercentChange < -50) {
      console.log('Bear market');
    } else if (btc3MonthPercentChange <= 35 && btc3MonthPercentChange >= -35 && btc6MonthPercentChange <= 50 && btc6MonthPercentChange >= -50) {
      console.log('Neutral market');
    } else {
      console.log('Market type is difficult to predict');
    }
  })
  .catch(error => console.error(error));