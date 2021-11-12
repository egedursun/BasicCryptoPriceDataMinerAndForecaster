#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 00:32:34 2021

@author: Ege Dogan Dursun
    Phone Number: +90(507)0558665
    E-Mail: edogandursun@gmail.com
    
    Please feel free to reach me out and give feedbacks about the code!
"""

import sqlite3
import os
import constants
import sql_middleware as sqlmw

#Method for selecting and retrieving coin information from the database
def get_coin_info_from_db(coin_name):
    query = sqlmw.prepare_select_query(coin_name, constants.DATA_SELECTION_THRESHOLD)
    db_path = os.path.join(constants.DATABASE_FOLDER, constants.DATABASE_NAME)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(query)
    records = cur.fetchall()
    cur.close()
    con.close()
    return records
    
#Method for the retrieval of coin information from the database with batches
def get_batch_coin_info_from_db(coin_names):
    multiple_coin_records = {}
    for coin_name in coin_names:
        records = get_coin_info_from_db(coin_name)
        multiple_coin_records[coin_name] = records
        