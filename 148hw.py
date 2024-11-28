# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 23:52:30 2022

@author: Ashish Gupta
"""

from tkinter import *
import random

root=Tk()
root.title("List")
root.geometry("400x400")

list_items=["Bottle","ID Card", "Hanky","Pencil"] 

listed_items = Label(root)
listed_items["text"]="Listed Items Are : Bottle , ID Card , Hanky , Pencil"

sorted_item = Label(root)


def sort_item():
    
    randomitem = random.sample(range(0,3),1)
    sorted_item["text"]="put item " + str(randomitem) + " in bag"
    print("put item " + str(randomitem) + " in bag")
    
listed_items.place(relx=0.5,rely=0.3,anchor=CENTER)

btn= Button(root,text= "Which Item To Put In Bag?",command=sort_item)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

sorted_item.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()