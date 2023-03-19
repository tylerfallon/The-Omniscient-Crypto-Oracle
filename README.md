# The-Omniscient-Crypto-Oracle

![dataBytes2](https://user-images.githubusercontent.com/114044192/223600108-0371d529-3bad-4187-a8e3-ffb8a3c347f8.jpg)

### Team Members
* Tyler Fallon
* Aaron Horneman
* Bobbi Colhour
* David Oliver

## Introduction

The cryptocurrency market is a center of a lot of activity. It is a growing market with much potential and profit. Data science is used in cryptocurrency to forecast and predict the prices of these digital coins. This science is used to figure out what causes the changes in prices of the coins, and then indictaes whether the prices will increase or decrease in the future. By focusing on market capitalization, or the coins' worth, one will predict how well or poorly a cryptocurrency will perform. 

In this project, TABD will be focusing on 5 different cryptocurrencies and their overall performance, specifically: Bitcoin, Dogecoin, Litecoin, Ripple and Ethereum. After running parsed data into specific machine learning algorithms, our goal is obtain predictions whether it is a good time to buy or sell a specific cryptocurrency or not. In addition, we will be able to determine which kind of crypto market the data falls under, whether is it a bull, bear, or neutral market.

Two years data was analyzed and averaged by weekday to see if there were any trends for high/low days. 

## Criteria for whether the user should invest:
### Is it a bull, bear, or neutral market?
  
#### Bull Market Criteria: 
1) Has Bitcoin price increased by over 70% in the past 3 months, and 150% in the past 6 months?
2) Has the asset in question increased by over 70% in the past 3 months, and over 200% in the past 6 months?

#### Bear Market Criteria:
1) Has Bitcoin price decreased by over 40% in the past 3 months, and 60% in the past 6 months? 
2) Has the asset in question decreased by over 40% in the past 3 months and over 60% in the past 6 months?
**For the above, if both 1 and 2, then highly likely bull market / bear market. If only 1, then somewhat likely bull market / bear market. If only 2, then it may indicate project growth or failure but not a true bull market / bear market. 

#### Neutral Market Criteria:
1) Has Bitcoin price stayed within a 70% range over the past 3 months, and neither increased or decreased more than 150% in the past 6 months? 
2) Has the asset in question stayed within a 70% range over the past 3 month, and neither increased or decreased more than 150% in the past 6 months?
* * If none of the above are true for bull, bear, or neutral market criteria, then it is too difficult to predict the market type

## Resources

### Data Sources: 
#### Monthly Data
https://coinmetrics.io/community-network-data/

#### Daily Data
https://www.investing.com/crypto/xrp/historical-data 
https://www.investing.com/crypto/ethereum/historical-data 
https://www.investing.com/crypto/bitcoin/historical-data 
https://www.investing.com/crypto/dogecoin/historical-data
https://www.investing.com/crypto/litecoin/historical-data

#### Definition
https://www.investopedia.com/

#### Data Resources: 
  - Deep Learning Algorithm to Predict Cryptocurrency Fluctuation Prices: Increasing Investment Awareness
      - https://www.mdpi.com/2079-9292/11/15/2349
  - Cryptocurrency price prediction using LSTMs | TensorFlow for Hackers (Part III)  
      - https://towardsdatascience.com/cryptocurrency-price-prediction-using-lstms-tensorflow-for-hackers-part-iii-264fcdbccd3f
  - Cryptocurrency Price Prediction Using Deep Learning
      - https://towardsdatascience.com/cryptocurrency-price-prediction-using-deep-learning-70cfca50dd3a
  
#### Data Tools: (Put database link here)

* [Preprocessing Code](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/b0425cc016031bcfc09992cbb61c9597b5496a38/Aaron/data_cleanup.ipynb)
* quickdatabasediagrams.com [ERD](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/david/QuickDBD-export.png)
* [Machine Learning Model Codes](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/tree/main/David) 

#### Software: 
Visual Studio Code, Jupyter Notebook, Github

#### Modules/Libraries: 
Python, Pandas, TensorFlow, Matplotlib, glob, Numpy
Keras, Long Short-Term Memory (LSTM),
Scikit-learn Library

Dashboard: HTML, CSS (Bootstrap), Javascript, Flask.py

## The Process

#### Topic
Cryptocurrencies – multiple types
#### Original Idea
What type of market? 
Is it a good time to invest?
Is it a good time to sell?  
Are there any particular trends that may be relevant?

#### Tasks Breakdown
##### Tyler
- Create New Repository
- Identify cryptos with 3 years history
- Define market type criteria
- Mock up dashboard

##### Aaron
- Cleaned all 5 set of data
- Create database w/ 2 tables

##### Bobbi
- Create Initial Repository
- Created logo for Team
- Gather datasets
- Time Series Research & Resources
- Clean/Transform data for Daily
- Create line graphs showing day of the week trends for each crypto
- Definitions
- Read Me & Project Template Layout

##### David
- ERD
- Time Series Research
- Built Machine Learning model for all five crypocurrencies
- Created Visualizations from Matplotlib
- Evaluated Model with various types of metrics
- Predicted Future Prices for all five cryptocurrencies
- Initialized ReadMe & Project Template Layout

## Future Enhancements
Coinmarketcap API to csv: https://stevesie.com/apps/coinmarketcap-api
