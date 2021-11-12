#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 00:32:34 2021

@author: Ege Dogan Dursun
    Phone Number: +90(507)0558665
    E-Mail: edogandursun@gmail.com
    
    Please feel free to reach me out and give feedbacks about the code!
"""

import datetime

#Check if the csupply is empty
def null_check_csupply(coin_obj):
    if coin_obj.csupply == "" or coin_obj.csupply == None:
        return True

#Check if the tsupply is empty        
def null_check_tsupply(coin_obj):
    if coin_obj.tsupply == "" or coin_obj.tsupply == None:
        return True

#Check if the msupply is empty
def null_check_msupply(coin_obj):
    if coin_obj.msupply == "" or coin_obj.msupply == None:
        return True

#Preperation of the insert query for the SQL queries
def prepare_insert_query(coin_obj):
    query_str = ""
    query_str += "INSERT INTO "
    query_str += str(coin_obj.symbol)
    query_str += " ("
    query_str += """
                id,
                datetime,
                symbol, 
                name, 
                nameid, 
                rank, 
                price_usd, 
                percent_change_24h, 
                percent_change_1h,
                percent_change_7d, 
                price_btc, 
                market_cap_usd, 
                volume24,
                volume24a, 
                csupply, 
                tsupply, 
                msupply
                """
    query_str += ") VALUES("  
    query_str += "NULL, '"
    query_str += str(datetime.datetime.now())
    query_str += "', '"
    query_str += str(coin_obj.symbol)
    query_str += "', '"
    query_str += str(coin_obj.name)
    query_str += "', '"
    query_str += str(coin_obj.nameid)
    query_str += "', "
    query_str += str(coin_obj.rank)
    query_str += ", "
    query_str += str(coin_obj.price_usd)
    query_str += ", "
    query_str += str(coin_obj.percent_change_24h)
    query_str += ", "
    query_str += str(coin_obj.percent_change_1h)
    query_str += ", "
    query_str += str(coin_obj.percent_change_7d)
    query_str += ", "
    query_str += str(coin_obj.price_btc)
    query_str += ", "
    query_str += str(coin_obj.market_cap_usd)
    query_str += ", "
    query_str += str(coin_obj.volume24)
    query_str += ", "
    query_str += str(coin_obj.volume24a)
    query_str += ", "
    query_str += "0" if null_check_csupply(coin_obj) else str(coin_obj.csupply)
    query_str += ", "
    query_str += "0" if null_check_tsupply(coin_obj) else str(coin_obj.tsupply)
    query_str += ", "
    query_str += "0" if null_check_msupply(coin_obj) else str(coin_obj.msupply)
    query_str += ");"
    return query_str

#Prepare the query for table creation if such table does not exist
def prepare_table_creation_if_not_exists(coin_obj):
    query_str = ""
    query_str += "CREATE TABLE IF NOT EXISTS "
    query_str += str(coin_obj.symbol)
    query_str += " ("
    query_str += """
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                datetime TEXT,
                symbol CHAR(16), 
                name CHAR(255), 
                nameid CHAR(255), 
                rank INTEGER, 
                price_usd FLOAT, 
                percent_change_24h FLOAT, 
                percent_change_1h FLOAT, 
                percent_change_7d FLOAT, 
                price_btc FLOAT, 
                market_cap_usd FLOAT, 
                volume24 FLOAT, 
                volume24a FLOAT, 
                csupply FLOAT, 
                tsupply FLOAT, 
                msupply FLOAT
                """
    query_str += ");"
    return query_str

#Selection query for retrieval of coin information from the database
def prepare_select_query(coin_name, selection_threshold):
    query_str = ""
    query_str += "SELECT * FROM (SELECT * FROM "
    query_str += str(coin_name)
    query_str += " ORDER BY id DESC LIMIT "
    query_str += str(selection_threshold)
    query_str += ") ORDER BY id ASC"
    query_str += ";"
    return query_str    