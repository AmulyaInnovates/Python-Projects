from tkinter import *
from tkinter import messagebox

root= Tk()
root.geometry("600x400")
root.title("Multiple Except Blocks ")

Label1= Label(root)
Label1.pack()


list1= ["Amulya" ,"Himali", "Nourin" ,"Atulya"]

dictionary1= {"Age":"11" , "Age2":"41"}

try:
     print(list1[2])
     print(dictionary1["Age3"])    
     
except (IndexError) :
       Label1["text"]= "Error, The Index Is Out Of Range"
       messagebox.showinfo("Error" , "The Index Is Out Of Range")
       
except (KeyError):
       Label1["text"]= "Error , Key Is Not Defined"
       messagebox.showinfo("Error" , "Key Is Not Defined") 
       
root.mainloop()