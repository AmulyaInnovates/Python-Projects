# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 11:33:39 2022

@author: Ashish Gupta
"""


from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.title("Dictionary")
root.geometry("600x400")
input_box= Entry(root)
input_box.pack()

def addition():
    number= random.randint(0,6)
    get_input= input_box.get()
    try: 
         print(number+ get_input)
         
    except: 
           messagebox.showinfo("Error" , "Cannot add 2 different data types : integers and strings")
          
button= Button(root, text="addition", command= addition)
button.pack()

root.mainloop()