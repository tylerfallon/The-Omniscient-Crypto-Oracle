# The-Omniscient-Crypto-Oracle
IMPORTANT
Remember that each team member, regardless of their role, needs to submit all the pieces of the deliverable for each segment.


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

* [Preprocessing Code](.ipynb)
* quickdatabasediagrams.com [ERD](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/david/QuickDBD-export.png)
* [Machine Learning Model Code](.ipynb) 

#### Software: 
Visual Studio Code, Jupyter Notebook, Github

#### Modules/Libraries: 
Python, Pandas, TensorFlow, Matplotlib, glob, Numpy
Keras, Long Short-Term Memory (LSTM) - (RNN model),
Scikit-learn Library - normalize data with MinMaxScaler(), evaluate using MAE (mean absolute error), confusion matrix, classification report

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
- Initialized ReadMe & Project Template Layout

## Future Enhancements
Coinmarketcap API to csv: https://stevesie.com/apps/coinmarketcap-api
