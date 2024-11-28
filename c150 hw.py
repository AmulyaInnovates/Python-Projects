# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 12:34:14 2022

@author: Ashish Gupta
"""

from tkinter import *
import random

root=Tk()
root.title("List")
root.geometry("400x400")

enter_country= Entry(root) 
enter_country.place(relx=0.5,rely= 0.2, anchor=CENTER)

enter_capital= Entry(root) 
enter_capital.place(relx=0.5,rely= 0.3, anchor=CENTER)

country_list_label= Label(root)
capital_list_label= Label(root)
country_random_no= Label(root)
capital_random_no= Label(root)

country_list= []
capital_list= []

def add_country():
    country_name= enter_country.get()
    country_list.append(country_name)
    country_list_label["text"]= "Country List = " + str(country_list) 
    capital_name= enter_capital.get()
    capital_list.append(capital_name)
    capital_list_label["text"]= "Capital List = " + str(capital_list)
    

def random_country():
   length_cou = len(country_list)
   random_no= random.randint(0 , length_cou-1)
   generated_random_number_cap= country_list[random_no]
   country_random_no["text"]= "Random Country : " + str(generated_random_number_cap)
   length_cap = len(capital_list)
   random_no= random.randint(0 , length_cap-1)
   generated_random_number_cou= capital_list[random_no]
   capital_random_no["text"]= "Random Capital : " + str(generated_random_number_cou)
   
   
btn= Button(root, text="Display Country And City Name ",command=add_country)
btn.place(relx=0.5,rely=0.4, anchor=CENTER)

country_list_label.place(relx=0.5,rely=0.5, anchor=CENTER)
capital_list_label.place(relx=0.5,rely=0.6, anchor=CENTER)

btn1= Button(root,text="Display Country And City Name Randomly ",command=random_country)
btn1.place(relx=0.5,rely=0.7, anchor=CENTER)

country_random_no.place(relx=0.5,rely=0.8,anchor=CENTER)
capital_random_no.place(relx=0.5,rely=0.9,anchor=CENTER)

    
    
root.mainloop()