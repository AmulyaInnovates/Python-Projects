# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 11:09:49 2022

@author: Ashish Gupta
"""

from tkinter import *
import random

root=Tk()
root.title("PASSWORD GENERATING")
root.geometry("400x400")

label= Label(root)

array_3d =[[[1,2,3,4,5,6],["Head","Tail"],["A","B","C","D","E","F","G","H"]]]
print(array_3d[0][2][3])
 
def new_password():
    random_no1= random.randint(0,5)
    random_no2= random.randint(0,1)
    random_no3= random.randint(0,7)
    
    letter1 =str(array_3d[0][0][random_no1])    
    letter2 =str(array_3d[0][1][random_no2])    
    letter3 =str(array_3d[0][2][random_no3])
    label["text"]= letter1 + "" + letter2 + "" + letter3
    print(letter1 + "" + letter2 + "" + letter3)
    
btn= Button(root,text= "New Password",command=new_password)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label.place(relx=0.5 , rely= 0.6, anchor= CENTER)

root.mainloop()