#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 00:32:34 2021

@author: Ege Dogan Dursun
    Phone Number: +90(507)0558665
    E-Mail: edogandursun@gmail.com
    
    Please feel free to reach me out and give feedbacks about the code!
"""

import json
from collections import namedtuple

#Decode the JSON formatted response information about the coins to object format
def customCoinDecoder(coinDict):
    return namedtuple('CryptoCoin', coinDict.keys())(*coinDict.values())

#Convert the dictionary to the relative mmodel, CryptoCoin
def dictToCoinModel(coinDict):
    coin = json.loads(json.dumps(coinDict), object_hook=customCoinDecoder)
    return coin
