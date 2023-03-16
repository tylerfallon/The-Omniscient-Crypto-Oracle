const axios = require('axios');
const COINBASE_API_URL = "https://api.coinbase.com/v2/prices/BTC-USD/spot";

// Get the current price
axios.get(COINBASE_API_URL)
  .then(response => {
    const currentPrice = parseFloat(response.data.data.amount);

    // Get yesterday's date and time
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    const yesterdayISO = yesterday.toISOString();

    // Get yesterday's price
    const historicalPriceURL = `${COINBASE_API_URL}?date=${yesterdayISO}`;
    return axios.get(historicalPriceURL)
      .then(response => {
        const yesterdayPrice = parseFloat(response.data.data.amount);

        // Calculate the percent change
        const percentChange = ((currentPrice - yesterdayPrice) / yesterdayPrice) * 100;

        // Display the percent change
        console.log(`Bitcoin percent change from yesterday to today: ${percentChange.toFixed(2)}%`);
        

      });
  })
  .catch(error => console.error(error));