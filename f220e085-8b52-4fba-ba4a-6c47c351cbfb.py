from tkinter import *
from tkinter import ttk
import psutil 
from psutil._common import BatteryTime

root = Tk()
root.geometry('500x250')
root.config(bg="black")
root.overrideredirect(True)


battery_life = Label(root, font = 'arial 15 bold', bg ='black', fg="white")
battery_life.place(relx=0.5,rely=0.5, anchor=CENTER)


root.mainloop()



