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

#Generator for the retrieval of ticks with the API
def all_coins_ticker_generator(agent : ApiAgent):
    while True:
        response = agent.receive_all_coins_ticker_response()
        yield response


