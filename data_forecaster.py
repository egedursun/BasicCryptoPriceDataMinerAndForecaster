#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 00:32:34 2021

@author: Ege Dogan Dursun
    Phone Number: +90(507)0558665
    E-Mail: edogandursun@gmail.com
    
    Please feel free to reach me out and give feedbacks about the code!
"""

"""
RUN THIS CLASS TO FORECAST PREDICTIONS ABOUT THE LATEST CRYPTOCURRENCY VALUES.
"""

import lazy_learner as ll
import constants
import sys
import time

#The main method that could be used to forecast cryptocurrency predictions continuously, could be run from terminal too.
def forecast_data(forecast_coins):
    forecast_tour_count = 1
    print("Cryptocurrency Market Forecaster Unit initialized and forecast plots will be transferred to the folder.") ; sys.stdout.flush()
    try:
        while True:
            ll.multiple_forecast(forecast_coins)
            tour_info = "[?$" + str(forecast_tour_count) + "]"
            print(tour_info, end="") ; sys.stdout.flush()
            forecast_tour_count += 1
            time.sleep(constants.FORECASTING_FREQUENCY_SECONDS)
    except KeyboardInterrupt:
        print('\n\n Keyboard interrupt has been detected, forecasting operations are cancelled!')
        


if __name__ == "__main__":
    forecast_data(constants.FORECAST_COINS)



