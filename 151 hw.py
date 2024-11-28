# -*- coding: utf-8 -*-
"""
Created on Sun May 29 11:45:19 2022

@author: Ashish Gupta
"""

from tkinter import *
import random
root=Tk()

root.title("Sales Application")
root.geometry("500x500")

month= Label(root)
profits= Label(root)

max_pr= Label(root)
min_pr= Label(root)
  


month_tuple= ("January","February","March","April","May","june","July","August","September","October","November","December")
profits_tuple= (20000,42300,90287,78253,23456,91827,12000,25000,30000,2010,92836,18402)

month["text"]= "Month: " + str(month_tuple)
profits["text"]= "Profits: " + str(profits_tuple)

def max_fun():
    max_profit = max(profits_tuple)
    max_profit_index = profits_tuple.index(max_profit)
    print(max_profit_index)
    max_profit_month= month_tuple[max_profit_index]
    max_pr["text"]="The Maximum profit of " + str(max_profit) + " was recorded in the month of " + str(max_profit_month)


def min_fun():
    min_profit= min(profits_tuple)
    min_profit_index = profits_tuple.index(min_profit)
    print(min_profit_index)
    min_profit_month= month_tuple[min_profit_index]
    min_pr["text"]="The Minimum profit of " + str(min_profit) + " was recorded in the month of " + str(min_profit_month)


btn= Button(root,text= "See Maximum Profit",command=max_fun)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

btn= Button(root,text= "See Minimum Profit", command=min_fun)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)

max_pr.place(relx=0.5,rely=0.5,anchor=CENTER)

min_pr.place(relx=0.5,rely=0.7,anchor=CENTER)


root.mainloop()