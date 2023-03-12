# The Omniscient Crypto Oracle
#### by TABD (Take A Byte Data)

## Overview:

This project aims to predict the future prices of five cryptocurrencies - Bitcoin, Ethereum, Dogecoin, Ripple, and Litecoin - using a Long Short-Term Memory (LSTM) model. The purpose of the project is to explore the potential of deep learning models in cryptocurrency price prediction.

## Analysis:

The project follows the following steps to create the LSTM model and predict future prices:

* *Data Collection*: Historical price data of the five cryptocurrencies is collected from various sources, including Coin Metrics and Investing.com.

* *Data Preprocessing*: The collected data will be preprocessed to ensure that it is clean, complete, and ready for training. This will involve removing missing values, normalizing the data, and splitting it into training and testing sets.

* *Model Building*: The LSTM model is built using the Keras library in Python. The model architecture includes several LSTM layers followed by a Dense layer. The model is trained on the training data.

* *Model Evaluation*: The model is evaluated on the testing data using Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and coefficient of determination (R^2) metrics. The predicted prices are compared to the actual prices to measure the accuracy of the model.

* *Model Prediction*: The trained LSTM model will be used to predict the prices of the five cryptocurrencies for a specific future date range.

* *Visualization*: The predicted prices will be plotted using Matplotlib to provide a clear representation of the model's performance.

## Summary:

The LSTM model used to predict cryptocurrency prices takes in historical data, including close prices, and feeds it through a neural network with three LSTM layers, each consisting of 50 neurons with the ReLU activation function. The input shape for the LSTM model should be a 3-dimensional array, where the first dimension is the number of samples, the second dimension is the number of time steps, and the third dimension is the number of features or variables in the input data. The `return_sequences=True` parameter is used to ensure that the output of the LSTM layer has the same number of time steps as the input data, so that it can be fed to subsequent LSTM layers. The output of the last LSTM layer is fed into a dense layer with a single output node, and the model is optimized using the `Adam` optimizer with the mean squared error loss function. The model is trained on the preprocessed data and can then be used to predict future cryptocurrency prices.

Confusion matrices and classification reports are typically used in the context of classification problems, where the goal is to predict the class or category of an input. Confusion matrices and classification reports are not useful in the context of predicting cryptocurrency prices with an LSTM model, as the goal is to predict a continuous value rather than a class or category. Instead, metrics such as MSE, RMSE, R-squared, and MAE are used to evaluate the performance of the model.

The mean squared error (MSE) metric measures the average squared difference between the predicted and actual prices. A lower MSE value indicates better model performance. 

The coefficient of determination (R^2) metric measures the proportion of the variance in the dependent variable (i.e., cryptocurrency price) that is predictable from the independent variables (i.e., time and other features). A higher R^2 value indicates better model performance. 

The validation error is a metric used to evaluate the performance of the LSTM model during training and helps to prevent overfitting. The validation error is calculated on a validation dataset, which is a subset of the training dataset that is not used during the model training phase. However, in this specific project, the validation set was the same as the training set, so the model would not be evaluated on new, unseen data and could potentially overfit to the training data. This most likely resulted in a model that performs well on the training data but poorly on new data, which defeats the purpose of the model.

Overall, the LSTM model shows promising results in predicting future cryptocurrency prices. However, it is important to note that cryptocurrency prices are highly volatile and unpredictable, and the model's accuracy may vary depending on various factors such as market conditions, news events, and regulatory changes.
