#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 00:32:34 2021

@author: Ege Dogan Dursun
    Phone Number: +90(507)0558665
    E-Mail: edogandursun@gmail.com
    
    Please feel free to reach me out and give feedbacks about the code!
"""

import data_model as dm

#This function parses the tick information that are received from the API
def parse_ticks(tick_data):
    data = tick_data["data"]
    coin_objects = []
    for coin_info in data:
        #Convert the dictionary items to cryptocurrency objects
        cur_coin = dm.dictToCoinModel(coin_info)
        coin_objects.append(cur_coin)
    #Return the coin objects
    return coin_objects
       
        
        
