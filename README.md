# The Omniscient Crypto Oracle
#### by TABD (Take A Byte Data)

## Overview:

This project aims to predict the future prices of five cryptocurrencies - Bitcoin, Ethereum, Dogecoin, Ripple, and Litecoin - using a Long Short-Term Memory (LSTM) model. The purpose of the project is to explore the potential of deep learning models in cryptocurrency price prediction.

## Analysis:

The project follows the following steps to create the LSTM model and predict future prices:

* *Data Collection*: Historical price data of the five cryptocurrencies is collected from various sources, including Coin Metrics and Investing.com.

* *Data Preprocessing*: The collected data is preprocessed by cleaning missing and inconsistent values, normalizing the data using MinMaxScaler, and creating sliding window sequences of the data.

* *Model Building*: The LSTM model is built using the Keras library in Python. The model architecture includes several LSTM layers followed by a Dense layer. The model is trained on the training data.

* *Model Evaluation*: The model is evaluated on the testing data using Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and coefficient of determination (R^2) metrics. The predicted prices are compared to the actual prices to measure the accuracy of the model.

## Summary:

The project uses various metrics to evaluate the LSTM model's accuracy in predicting future prices of cryptocurrencies. The mean squared error (MSE) metric measures the average squared difference between the predicted and actual prices. A lower MSE value indicates better model performance. The coefficient of determination (R^2) metric measures the proportion of the variance in the dependent variable (i.e., cryptocurrency price) that is predictable from the independent variables (i.e., time and other features). A higher R^2 value indicates better model performance. The validation error is a metric used to evaluate the performance of the LSTM model during training and helps to prevent overfitting. The validation error is calculated on a validation dataset, which is a subset of the training dataset that is not used during the model training phase. However, in this specific project, the validation set was the same as the training set, so the model would not be evaluated on new, unseen data and could potentially overfit to the training data. This most likely resulted in a model that performs well on the training data but poorly on new data, which defeats the purpose of the model.

Overall, the LSTM model shows promising results in predicting future cryptocurrency prices. However, it is important to note that cryptocurrency prices are highly volatile and unpredictable, and the model's accuracy may vary depending on various factors such as market conditions, news events, and regulatory changes.
