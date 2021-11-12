#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 00:32:34 2021

@author: Ege Dogan Dursun
    Phone Number: +90(507)0558665
    E-Mail: edogandursun@gmail.com
    
    Please feel free to reach me out and give feedbacks about the code!
"""

import sql_select_communicator as sqlscm
import numpy
import matplotlib.pyplot as plt
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import constants
import os
import sys
import datetime

#Convert the data into a matrix
def matrix_dataset(dataset, lb=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-lb-1):
		a = dataset[i:(i+lb), 0]
		dataX.append(a)
		dataY.append(dataset[i + lb, 0])
	return numpy.array(dataX), numpy.array(dataY)

#Prepare the data by selecting the price field from the database response
def prepare_the_data(raw_records):
    data = []
    for tick in raw_records:
        data.append(tick[6]) #Adding price (USD)
    return numpy.array(data).reshape(-1, 1)
        
#Forecast predictions by using LSTM (Long Short Term Memory)
def forecast_by_LSTM(coin_name, crt_path="/"):
    
    #Convert the raw records to organized price field time series
    raw_records = sqlscm.get_coin_info_from_db(coin_name)
    data = prepare_the_data(raw_records)
    
    #Scale and transform the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    data = scaler.fit_transform(data)
    
    #Determine the size of the training set and test set and split them
    train_size = int(len(data) * constants.TRAINING_SET_RATIO)
    
    train, test = data[0:train_size,:], data[train_size:len(data),:]
    
    print(" Length of the Training Set: ", len(train), "\n" , "Length of the Test Set: ", len(test))
    
    #Convert the flat time series data to matrices
    lb = 1
    trainX, trainY = matrix_dataset(train, lb)
    testX, testY = matrix_dataset(test, lb)
    
    trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
    testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
    
    #Define the LSTM model
    model = Sequential()
    model.add(LSTM(4, input_shape=(1, lb)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(trainX, trainY, epochs=constants.TRAINING_EPOCHS, batch_size=1, verbose=1)
    
    #Create the predictions and show the RMSE error variables
    train_predict = model.predict(trainX)
    test_predict = model.predict(testX)
    train_predict = scaler.inverse_transform(train_predict)
    trainY = scaler.inverse_transform([trainY])
    test_predict = scaler.inverse_transform(test_predict)
    testY = scaler.inverse_transform([testY])
    trainScore = math.sqrt(mean_squared_error(trainY[0], train_predict[:,0]))
    print('Training Score: %.2f RMSE' % (trainScore))
    testScore = math.sqrt(mean_squared_error(testY[0], test_predict[:,0]))
    print('Test ing Score: %.2f RMSE' % (testScore))
    
    #Prepare the plots for the LSTM
    train_predictPlot = numpy.empty_like(data)
    train_predictPlot[:, :] = numpy.nan
    train_predictPlot[lb:len(train_predict)+lb, :] = train_predict
    test_predictPlot = numpy.empty_like(data)
    test_predictPlot[:, :] = numpy.nan
    test_predictPlot[len(train_predict)+(lb*2)+1:len(data)-1, :] = test_predict
    plt.plot(scaler.inverse_transform(data))
    plt.plot(train_predictPlot)
    plt.plot(test_predictPlot)
    
    #Save the prediction plot to the file system in png format
    file_path = os.path.join(crt_path, coin_name)
    plt.savefig(file_path+".png")
    plt.clf()
    

#Forecast multiple coin information
def multiple_forecast(coin_names):
    crt_path = os.path.join(constants.FORECAST_FOLDER, str(datetime.datetime.now()))
    os.mkdir(crt_path)
    for coin_name in coin_names:
        forecast_by_LSTM(coin_name, crt_path)
        

    
    
    
    
    
    
    
    