from tkinter import *
from tkinter import messagebox


list1= ["am", "sh", "to"]
 
try:
    print(list1[4])

except:
       print("Error, The Index Is Out Of Range")
       messagebox.showinfo("Error" , "The Index Is Out Of Range")
       
root.mainloop()