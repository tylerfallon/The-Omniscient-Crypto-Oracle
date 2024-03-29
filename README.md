# The-Omniscient-Crypto-Oracle

![dataBytes2](https://user-images.githubusercontent.com/114044192/223600108-0371d529-3bad-4187-a8e3-ffb8a3c347f8.jpg)

### Team Members
* Tyler Fallon
* Aaron Horneman
* Bobbi Colhour
* David Oliver

## Introduction
Everyone has heard of cryptocurrency, but how many people understand it? Everyone wants in on the riches, but there is sooooo much contradictory data and nuances. What if we could provide an unbiased tool that explained in plain English if it is a good time to buy or sell based on market data and also had simple informative information about each cryptocurrency? We wanted to do this project because there is a lot of historcal data to analyze and it would be beneficial to everyday people who wanted to invest.

The cryptocurrency market is a center of a lot of activity. It is a growing market with much potential and profit. Data science is used in cryptocurrency to forecast and predict the prices of these digital coins. This science is used to figure out what causes the changes in prices of the coins, and then indicates whether the prices will increase or decrease in the future. By focusing on market capitalization, or the coins' worth, one will predict how well or poorly a cryptocurrency will perform. 

In this project, TABD will be focusing on 5 different cryptocurrencies and their overall performance, specifically: Bitcoin, Dogecoin, Litecoin, Ripple and Ethereum. After running parsed data into specific machine learning algorithms, our goal is obtain predictions whether it is a good time to buy or sell a specific cryptocurrency or not. In addition, we will be able to determine which kind of crypto market the data falls under, whether is it a bull, bear, or neutral market.

  - API connections were used to get real time data of current crypto price and to evaluate the type of market. 
  - Ten years data for each cryptocurrency was used for the machine learning module to attempt to predict the price within 60 days of data. 
  - Two years data was analyzed and averaged by weekday to see if there were any trends for high/low days.
  
### Questions to be answered:

* What type of market are we currently in? 
* Is it a good time to invest?
* Is it a good time to sell?
* Are there any particular trends that may be relevant?

## Resources
 
#### Daily/Monthly Historical Data
https://coinmetrics.io/community-network-data/
https://www.investing.com/crypto/xrp/historical-data 
https://www.investing.com/crypto/ethereum/historical-data 
https://www.investing.com/crypto/bitcoin/historical-data 
https://www.investing.com/crypto/dogecoin/historical-data
https://www.investing.com/crypto/litecoin/historical-data

#### Data Resources: 
  - [Deep Learning Algorithm to Predict Cryptocurrency Fluctuation Prices: Increasing Investment Awareness](https://www.mdpi.com/2079-9292/11/15/2349)
  - [Cryptocurrency price prediction using LSTMs | TensorFlow for Hackers (Part III)](https://towardsdatascience.com/cryptocurrency-price-prediction-using-lstms-tensorflow-for-hackers-part-iii-264fcdbccd3f)
  - [Cryptocurrency Price Prediction Using Deep Learning](https://towardsdatascience.com/cryptocurrency-price-prediction-using-deep-learning-70cfca50dd3a)
  - [Market Definitions](https://www.investopedia.com/)
  
#### Data Tools:

* [Preprocessing Code](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/b0425cc016031bcfc09992cbb61c9597b5496a38/Aaron/data_cleanup.ipynb)
* [ERD](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/David/QuickDBD-export.png) (quickdatabasediagrams.com)
* [Machine Learning Model Codes](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/tree/main/David) 
* [Daily Trend Code](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/tree/main/Bobbi/Code)
* [Coindesk API](https://www.coindesk.com/tag/api/)
* [Kraken API](https://www.kraken.com/features/api-trading)
* [Coinbase API](https://help.coinbase.com/en/cloud/api/coinbase)

#### Software: 
Visual Studio Code, Jupyter Notebook, Github, QuickDBD, Google Colab

#### Languages/Libraries: 
* Preprocessing & ML Model: Python, Pandas, TensorFlow, Matplotlib, glob, Numpy, Keras, Long Short-Term Memory (LSTM), Scikit-learn Library, DateTime
* Dashboard: HTML, CSS (Bootstrap framework), Javascript, Flask.py, Requests

## Analysis

### Tasks Breakdown
_______________________________________________________________________________________________________________________________________________________________________
### Aaron 
[Detailed Read Me](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/Aaron/README.md)

- Used software tools to extract data from sources and store into suitable CSV formats
- Removed duplicates, missing values, and corrected data format errors
- Merged cleaned DataFrames into single DataFrame with a common time frame
- Calculated percentages of change for crypto prices and added column to DataFrame
- Assisted in reviewing code, gathering images, dashboard
- To view all the preprocessing coding, [click here!](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/Aaron/data_cleanup.ipynb)

_______________________________________________________________________________________________________________________________________________________________________
### Bobbi
[Detailed Read Me](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/Bobbi/BobbiREADME.md)

- Created [Initial Repository](https://github.com/bcolhour/TABD)
- Created logo for our team
- Gathered [datasets](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/tree/main/Bobbi/Resources)
- Time Series Research & Resources
- Compiled definitions for Market Type analysis
- Restructered main ReadMe & project template layout
- Initialized & formatted our [powerpoint presentation](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/The%20Omniscient%20Crypto%20Oracle.pptx)
- Assisted in reviewing code & the dashboard
- Cleaned/Transformed our data for daily trend analysis. [Click here](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/tree/main/Bobbi/Code) to view the code!
- Created [line graphs](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/tree/main/Bobbi/images) showing day of the week trends for each cryptocurrency

![image](https://user-images.githubusercontent.com/114044192/223884809-f680644c-b7c4-4a7e-a5de-05424cd52e1d.png)
![Dogecoin Daily](https://user-images.githubusercontent.com/114044192/223884894-1f037697-25fd-4c04-a9f5-c28ebe337072.png)
![ETH Daily](https://user-images.githubusercontent.com/114044192/223884903-3595e265-1081-4cc2-8db1-1ba381f4c079.png)
![LiteCoin Daily](https://user-images.githubusercontent.com/114044192/223884912-b3edd12b-a4fc-413b-b003-f04c0300ffb9.png)
![XRP Daily](https://user-images.githubusercontent.com/114044192/223884926-722eb05b-8d66-471b-88b4-7de6109fd01d.png)

_______________________________________________________________________________________________________________________________________________________________________
### David
[Detailed ReadMe](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/David/README.md)

- Created our initial [Entity Relationship Diagram](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/David/QuickDBD-export.png)
- Initialized ReadMe & Project Template Layout
- Time Series Research
- Edited [final presentation](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/The%20Omniscient%20Crypto%20Oracle.pptx) and ReadMe formatting 
- Built Machine Learning model for all five crypocurrencies
- Evaluated Model with various types of metrics for each cryptocurrency
- Created [Visualizations from Matplotlib](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/tree/main/Aaron/Images) to identify patterns or trends
- Exported predicion price DataFrames into suitable CSV formats
- Assisted in reviewing code & the dashboard
- To view all the deep machine learning coding, select from: [Bitcoin](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/David/LSTM-Model_Bitcoin.ipynb), [Ethereum](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/David/LSTM-Model_Ethereum.ipynb), [Dogecoin](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/David/LSTM-Model_Dogecoin.ipynb), [Litecoin](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/David/LSTM-Model_Litecoin.ipynb), [Ripple](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/David/LSTM-Model_Ripple.ipynb)

<img src="https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/Aaron/Images/Predicted%20vs.%20True%20Values%20Dogecoin.PNG" width=40% height=40%><img src="https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/Aaron/Images/Prediction%20Error%20Histogram%20Ethem.PNG" width=40% height=40%><img src="https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/Aaron/Images/Actual%20vs%20Predicted%20Bitcoin%20Prices.PNG" width=40% height=40%><img src="https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/Aaron/Images/Actual%20vs%20Predicted%20Ripple%20Rolling%20Mean.PNG" width=40% height=40%><img src="https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/Aaron/Images/Training%20and%20Validation%20Loss%20Litecoin.PNG" width=40% height=40%>

- Predicted Future Prices for all five cryptocurrencies:
 
<img src="https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/David/BTCPrediction.png" width=40% height=40%><img src="https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/David/DogePrediction.png " width=40% height=40%><img src="https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/David/ETHPrediction.png " width=40% height=40%><img src="https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/David/LTCPrediction.png " width=40% height=40%><img src="https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/David/XRPPrediction.png " width=40% height=40%>

_______________________________________________________________________________________________________________________________________________________________________
### Tyler
[Detailed ReadMe]

- Created our repository (https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle)
- Identified cryptocurrencies with at least ten years history
- Defined market type criteria
- Mocked up intial UI/UX for dashboard 
- Created Flask application with [app.py file](https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/app.py)
- Defined routes in app.py to send information to the frontend interface
- Used several APIs to get real-time price data, percent change, and type of market on the frontend
- Used HTML, CSS, and Javascript, along with the Bootstrap framework, to create the dashboard
- Created the logic to calculate whether the market was a bull market, bear market, or neutral market, and ran the logic in realtime

The data for Bitcoin can be seen below:
<img src="https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/af2ad5251a4120eff2a83474fea02a2a6862e31e/tyler/assets/img/Screen%20Shot%202023-03-23%20at%202.21.52%20PM.png">

Here is the data for Ethereum:
<img src="https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/tyler/assets/img/Screen%20Shot%202023-03-23%20at%202.27.06%20PM.png">

We also have dashboard sections for Dogecoin, Litecoin, and Ripple. 

_______________________________________________________________________________________________________________________________________________________________________

## Summary of Results
### Machine Learning Data

<img src="https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/David/Metrics.png" width=60% height=60%>

MSE measures the average squared difference between the predicted and actual values. MAE measures the average absolute difference between the predicted and actual values. RMSE measures the square root of the average squared difference between the predicted and actual values. A smaller value for these metrics indicates better performance. In this case, the values of all coins for these metrics indicates that the model's predictions are close to the actual values.

Coefficient of determination (r^2) measures the proportion of variance in the target variable (cryptocurrency prices) that can be explained by the model. The r^2 value of 0.9307 for Bitcoin, for example, indicates that the model explains 93.07% of the variance in the target variable, which is a high value and suggests that the model has captured the underlying patterns well. Dogecoin did have a lower value compared to the rest with 72.98%.

While the metrics obtained from our LSTM model suggest good performance, it is important to consider the possibility of overfitting. Additionally, the accuracy of the predictions can be affected by various factors that may not have been captured by the model, such as sudden market changes, unexpected events, or changes in government regulations. Therefore, while the model can provide a useful tool for predicting future cryptocurrency prices, it's important to interpret the results with caution.

### Daily Trend Data
It was interesting that while there are definite days that show mean price being higher or lower on different weekdays, it was different for each cryptocurrency. 

<img src="https://github.com/tylerfallon/The-Omniscient-Crypto-Oracle/blob/main/David/PricingTrendsbyWeekday.png" width=50% height=50%>

### Is it a good time to buy or sell? Are we currently in a bull, bear, or neutral market?
  
##### Bull Market Criteria: 
1) Has Bitcoin price increased by over 70% in the past 3 months, and 150% in the past 6 months?
2) Has the asset in question increased by over 70% in the past 3 months, and over 200% in the past 6 months?

##### Bear Market Criteria:
1) Has Bitcoin price decreased by over 40% in the past 3 months, and 60% in the past 6 months? 
2) Has the asset in question decreased by over 40% in the past 3 months and over 60% in the past 6 months?
**For the above, if both 1 and 2, then highly likely bull market / bear market. If only 1, then somewhat likely bull market / bear market. If only 2, then it may indicate project growth or failure but not a true bull market / bear market. 

##### Neutral Market Criteria:
1) Has Bitcoin price stayed within a 70% range over the past 3 months, and neither increased or decreased more than 150% in the past 6 months? 
2) Has the asset in question stayed within a 70% range over the past 3 month, and neither increased or decreased more than 150% in the past 6 months?

##### Too Difficult To Predict Market Type Criteria:
If none of the above are true for bull, bear, or neutral market criteria, then it is too difficult to predict the market type.

### Difficulties
Cryptocurrency prices can be volatile, and we encountered issues with noisy, missing, or incorrect data points. Some exchanges have different pricing formats so combining the data from different sources was challenging. LSTM models, in particular, are complex and tuning the hyperparameters to optimize performance and debugging any errors was time-consuming and difficult, whether it was preprocessing the data or running the actual model. We also ran to the issue of overfitting, where we obtained very good predictions with the testing set, but not so well on future, unseen data. Even trying to create visualizations and a dashboard that were both informative and visually appealing wasn't easy, especially because of our large datasets and complex models.


## Future Enhancements
- Add additional Cryptocurrencies
- Link prediction model to API for real time info
- Add a date input field for future predictions
- Use a separate validation set: used to tune our model's hyperparameters and prevent overfitting
- Use `Dropout`: randomly drops out some neurons during training to prevent overfitting
- Use `Early Stopping`: stops training process when validation error stops improving to prevent overfitting
- Add more features, such as technical indicators
- Use other RNN models, CNN models, or even ensemble methods like Random Forest
- Optimize hyperparameters such as learning rate, batch size, or number of epochs
- Use different loss function, such as Mean Absolute Percentage Error (MAPE) to evaluate model
- Experiment with different activation functions, such as Sigmoid or Tanh
