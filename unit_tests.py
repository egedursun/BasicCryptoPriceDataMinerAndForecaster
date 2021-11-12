#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 00:32:34 2021

@author: Ege Dogan Dursun
    Phone Number: +90(507)0558665
    E-Mail: edogandursun@gmail.com
    
    Please feel free to reach me out and give feedbacks about the code!
"""


from api_agent import ApiAgent
from ticker_generator import all_coins_ticker_generator as actg
import constants

#Instantiate the API agent
agent = ApiAgent(constants.API_HOST, constants.API_KEY, constants.COIN_STARTING_INDEX, constants.COIN_ENDING_INDEX)

#Test the generator results for the API retrieval
result = next(actg(agent))
print(result)