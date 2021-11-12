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

#Method for saving mined coin information to the database
def save_coin_info_to_db(coin):
    query = sqlmw.prepare_insert_query(coin)
    check_table_query = sqlmw.prepare_table_creation_if_not_exists(coin)
    db_path = os.path.join(constants.DATABASE_FOLDER, constants.DATABASE_NAME)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(check_table_query)
    cur.execute(query)
    con.commit()
    con.close()
    
#Method for saving the coin information to the database in batches
def save_batch_coin_info_to_db(coins):
    for coin in coins:
        save_coin_info_to_db(coin)