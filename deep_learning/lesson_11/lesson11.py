import yfinance as yf
import pandas as pd
import numpy as np

data = yf.download("AMZN",start="2015-01-01",end="2023-01-01")

data.head()

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data["Close"].values.reshape(-1,1))



sequence_length = 90

X,y=[],[]

for i in range(sequence_length,len(scaled_data)):
    X.append(scaled_data[i-sequence_length:i])
    y.append(scaled_data[i])

X,y = np.array(X), np.array(y)
print(X)
print(y)


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense

model = Sequential()
model.add(LSTM(units=50, return_sequences=True,input_shape=(X.shape[1],1)))

model.add(Dropout(0.2))

model.add(LSTM(units=50,return_sequences=False))
model.add(Dropout(0.2))

model.add(Dense(units=1))
model.compile(optimizer="adam",loss="mean_squared_error")


train_size = int(len(X) * 0.8)

X_train,X_test = X[:train_size],X[train_size:]
y_train,y_test = y[:train_size], y[train_size:]

model.fit(X_train,y_train,epochs=10,batch_size=32,validation_data = (X_test,y_test))

predictions = model.predict(X_test)

predictions = scaler.inverse_transform(predictions)
actual_prices = scaler.inverse_transform(y_test.reshape(-1,1))

from sklearn.metrics import mean_squared_error,mean_absolute_error

mae = mean_absolute_error(actual_prices,predictions)
mse = mean_squared_error(actual_prices,predictions)

print(f"Mean Absolute Error: {mae}, Mean Squared Error:{mse}")

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.plot(actual_prices,color="red",label="Actual Price")
plt.plot(predictions,color="blue",label="Predicted Prices")

plt.title("Stock Price Prediction")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend()
plt.show()