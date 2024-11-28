
from tkinter import *
import random

root=Tk()
root.title("Dictionary")
root.geometry("600x400")

dictionary = {"colour": [ "maroon1", "DarkSlateGray1", "lavender", "medium turquoise", "firebrick1", "RoayalBlue2", "deep pink", "chocolate1", "magenta2", "springgreen2", "cyan", "Lawn green"]}
  

def bg_change():
    random_no = random.randint(0,11)
    print(dictionary["colour"][random_no])
    root.configure(background= dictionary["colour"][random_no])
    
    
    
btn= Button(root,text="click on me to change the colours ",command=bg_change)
btn.place(relx= 0.5 ,rely=0.5 , anchor= CENTER)
    


root.mainloop()