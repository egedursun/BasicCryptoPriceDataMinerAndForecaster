#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 00:32:34 2021

@author: Ege Dogan Dursun
    Phone Number: +90(507)0558665
    E-Mail: edogandursun@gmail.com
    
    Please feel free to reach me out and give feedbacks about the code!
"""

#Containers for the database objects
DATABASE_FOLDER = "data_house"
DATABASE_NAME = "coins.db"

#Containers for forecast results
FORECAST_FOLDER = "forecasts"

#Url address that provides the Restful API Service
URL = "https://coinlore-cryptocurrency.p.rapidapi.com/api/tickers/"

#The host address for the API call header
API_HOST = "coinlore-cryptocurrency.p.rapidapi.com"

#The host API token / key for data requests and responses
API_KEY = "12c9a2798emsh707e09f763a8efdp13c552jsn78c44ff7d294"

#Starting index for the coins we will receive
COIN_STARTING_INDEX = 0

#Ending indexes for the coins we will receive
COIN_ENDING_INDEX = 100

#The frequency of the ticks we will receive from the API
MINING_TICK_FREQUENCY_SECONDS = 5

#The frequency of the forecasts in seconds
FORECASTING_FREQUENCY_SECONDS = 300

#Data amount threshold for LSTM
DATA_SELECTION_THRESHOLD = 10000

#Forecasting training set ratio
TRAINING_SET_RATIO = 0.7

#LSTM Training Epochs
TRAINING_EPOCHS = 10

#Forecast Coins that we would like to predict / the files will be generated in forecasts folder
FORECAST_COINS = [
    "BTC",
    "ETH",
    "ADA",
    "ALGO",
    "ATOM",
    "NEO",
    "CAKE",
    "CELO",
    "CHZ",
    "CRV",
    "DGB",
    "ETC",
    "KCS",
    "KDA",
    "LINK",
    "LTC",
    "AVAX",
    "BNB",
    "DOT",
    "ELON",
    "IOTA",
    "SHIB",
    "SUSHI",
    "SOL"
    ]