#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 00:32:34 2021

@author: Ege Dogan Dursun
    Phone Number: +90(507)0558665
    E-Mail: edogandursun@gmail.com
    
    Please feel free to reach me out and give feedbacks about the code!
"""


import requests
import constants

#This class creates an agent that communicates with the API that retrieves cryptocurrency information
class ApiAgent():
    
    #Agent constructor
    def __init__(self, host, api_key, tracked_coin_start, tracked_coin_end):
        self.host = host
        self.api_key = api_key
        self.tracked_coin_start = tracked_coin_start
        self.tracked_coin_end = tracked_coin_end
    
    #Receive response by sending a request and returning the answer in json format
    def receive_all_coins_ticker_response(self):
        querystring = {"start": str(self.tracked_coin_start),"limit": str(self.tracked_coin_end)}
        headers = {
            'x-rapidapi-host': self.host,
            'x-rapidapi-key': self.api_key
            }
        response = requests.request("GET", constants.URL, headers=headers, params=querystring)
        if response.json != None:
            return response.json()
        else:
            self.receive_all_coins_ticker_response()
        