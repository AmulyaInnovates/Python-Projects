# -*- coding: utf-8 -*-
"""
Created on Sun May 29 11:26:19 2022

@author: Ashish Gupta
"""

month= ("January","February","March","April","May","june","July","August","September","October","November","December")

profits= (20000,42300,90287,78253,23456,91827,12000,25000,30000,2010,92836,18402)

max_profit= max(profits)
max_profit_index = profits.index(max_profit)
print(max_profit_index)

max_profit_month= month[max_profit_index]
print("The Maximum profit of " + str(max_profit) + " was recorded in the month of " + str(max_profit_month))

min_profit= min(profits)
min_profit_index = profits.index(min_profit)
print(min_profit_index)

min_profit_month= month[min_profit_index]
print("The Minimum profit of " + str(min_profit) + " was recorded in the month of " + str(min_profit_month))
