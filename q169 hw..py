from tkinter import * 
from tkinter import ttk

root = Tk()  
root.geometry("900x600") 
root.title("Classes")

canvas= Canvas(root,width=990,height=490,bg="white",highlightbackground="grey")
canvas.pack()

label= Label(root,text="choose colour :")
label.pack()

fillcolour= ["green", "yellow","red","blue"]
colour_dropdown= ttk.Combobox(root,state="readonly",values= fillcolour, width=10)
colour_dropdown.place(relx=0.8,rely=0.9,anchor= CENTER)

startx= Label(root,text="startx")
startx.place(relx=0.1,rely=0.85,anchor= CENTER)
coordinates_values= [10,50,100,200,300,400,500,600,700,800,900]
d1= ttk.Combobox(root,state="readonly",values= coordinates_values, width=10)
d1.place(relx=0.2,rely=0.85,anchor= CENTER)

starty= Label(root,text="starty")
starty.place(relx=0.3,rely=0.85,anchor= CENTER)
d2= ttk.Combobox(root,state="readonly",values= coordinates_values, width=10)
d2.place(relx=0.4,rely=0.85,anchor= CENTER)

endy= Label(root,text="starty")
endy.place(relx=0.3,rely=0.85,anchor= CENTER)
d2= ttk.Combobox(root,state="readonly",values= coordinates_values, width=10)
d2.place(relx=0.4,rely=0.85,anchor= CENTER)