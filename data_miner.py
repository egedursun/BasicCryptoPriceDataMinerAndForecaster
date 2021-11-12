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
RUN THIS CLASS TO MINE DATA ABOUT THE LATEST CRYPTOCURRENCY VALUES.
"""


import time
from api_agent import ApiAgent
from ticker_generator import all_coins_ticker_generator as actg
import active_tick_parser as atp
import constants
import sql_post_communicator as sqlpcm
import sys

#Main method that will mine the data about the cryptocurrency markets / ticks
def mine_crypto_data(tick_frequency):
    print("Cryptocurrency Market Data Miner Unit initialized and will mine a tick every '",tick_frequency,"' seconds.") ; sys.stdout.flush()
    mining_tour_count = 1
    try:
        while True:
            agent = ApiAgent(constants.API_HOST, constants.API_KEY, constants.COIN_STARTING_INDEX, constants.COIN_ENDING_INDEX)
            result = next(actg(agent))
            parsed_tick_objects = atp.parse_ticks(result)
            sqlpcm.save_batch_coin_info_to_db(parsed_tick_objects)
            tour_info = "[$" + str(mining_tour_count) + "]"
            print(tour_info, end="") ; sys.stdout.flush()
            mining_tour_count += 1
            time.sleep(tick_frequency)
    except KeyboardInterrupt:
        print('\n\n Keyboard interrupt has been detected, data mining operations are cancelled!')


if __name__ == "__main__":
    mine_crypto_data(constants.MINING_TICK_FREQUENCY_SECONDS)