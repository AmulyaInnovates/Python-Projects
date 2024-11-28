from tkinter import *
from tkinter import messagebox

dictionary1= {"colour": "red", "animal":"lion"}

try:
   print(dictionary1["city"])
   
except: 
       print("Error , Key Is Not Defined")
       messagebox.showinfo("Error" , "Your Key Is Not Defined")
       
root.mainloop()