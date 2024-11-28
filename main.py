from tkinter import *
from tkinter import ttk
import psutil 
from psutil._common import BatteryTime
import time
import datetime

root = Tk()
root.geometry('500x250')
root.config(bg="black")
root.overrideredirect(True)
style= ttk.Style(root)
style.layout('ProgressBarStyle',[('Horizontal.Progressbar.trough',{'children':[('Horizontal.Progressbar.pbar',{'side':'right','sticky':'ns'})],
'sticky':'nsew'}),('Horizontal.Progressbar.label',{'sticky': ''})])
bar=ttk.Progressbar(root,maximum=100,style='ProgressBarStyle')
bar.place(relx=0.5,rely=0.2,anchor=CENTER)
battery_life = Label(root, font = 'arial 15 bold', bg ='black', fg="white")
battery_life.place(relx=0.5,rely=0.5, anchor=CENTER)

def converttime(seconds):
    get_time= time.gmtime(seconds)
    order_time= time.strftime("%H:%M:%S",get_time)
    return order_time

def battery_life():
    battery= psutil.sensors_battery()
    bar['value']=battery.percent
    style.configure('ProgressBarStyle',text= str(battery.percent)+ " %")
    bl= converttime(battery.secsleft)

    if battery.secsleft== BatteryTime.POWER_TIME_UNLIMITED:
        battery_life['text']="Unplug The Charger \n Rerun The Program"
    elif battery.secsleft== BatteryTime.POWER_TIME_UNKNOWN:
        battery_life['text']="There Was A Problem Detecting The Battery \n Rerun The Program"
    else:
        battery_life['text']="Battery Life"+bl
        root.after(1000,battery_life)

battery_life()

root.mainloop()



