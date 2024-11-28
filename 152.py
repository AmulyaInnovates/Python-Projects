# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 12:45:02 2022

@author: Ashish Gupta
"""

from tkinter import *
import random

root=Tk()
root.title("Multi Dimensional Array")

root.geometry("500x500")
label= Label(root)

array_1d=["Amulya", "Himali" , "Nourin Mam"] 
print(array_1d[0])
  
array_2d= [["Amulya","A"],["Himali","B++"] ,["Nourin Mam","A"]]
print(array_2d[0][1])

array_3d= [[["Amulya","A","Excellent"],["Himali","B++","Very GOOD!"] ,["Nourin Mam","A","Excellent"]]]
print(array_3d[0][0][2])

def report():
    label["text"]= array_3d[0][1][0] + " got grades :-" + array_3d[0][1][1] + " and they are doing " + array_3d[0][1][2]
    
btn= Button(root,text= "see your child's report card!", command=report)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()