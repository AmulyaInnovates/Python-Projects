from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
root= Tk()
root.title("Working On Canvas Using Functions")
root.geometry("600x600")

canvas= Canvas(root, height=900,width=900,bg="white",highlightbackground="lightgray")
canvas.pack()

color_label=Label(root, text="Choose a Color :")
color_label.place(relx=0.6,rely=0.9, anchor= CENTER)

fill_color=["green","yellow","red","blue"]
colour_dropdown= ttk.Combobox(root, state="readonly",values= fill_color ,width=10)
colour_dropdown.place(relx=0.8,rely=0.9,anchor=CENTER) 

startx=Label(root,text="startx")
startx.place(relx=0.1,rely=0.85,anchor=CENTER) 
coordinate_valus=[10,50,100,200,300,400,500,600,700,800,900]
d1= ttk.Combobox(root, state="readonly",values= coordinate_valus ,width=10)
d1.place(relx=0.2,rely=0.85,anchor=CENTER) 

starty=Label(root,text="starty")
starty.place(relx=0.3,rely=0.85,anchor=CENTER) 
d2= ttk.Combobox(root, state="readonly",values= coordinate_valus ,width=10)
d2.place(relx=0.4,rely=0.85,anchor=CENTER) 

endx=Label(root,text="endx")
endx.place(relx=0.5,rely=0.85,anchor=CENTER) 
d3= ttk.Combobox(root, state="readonly",values= coordinate_valus ,width=10)
d3.place(relx=0.6,rely=0.85,anchor=CENTER) 

endy=Label(root,text="endy")
endy.place(relx=0.7,rely=0.85,anchor=CENTER) 
d4= ttk.Combobox(root, state="readonly",values= coordinate_valus ,width=10)
d4.place(relx=0.8,rely=0.85,anchor=CENTER) 

def circle(event):
    oldx= d1.get()
    oldy= d2.get()
    newx= d3.get()
    newy= d4.get()
    keypress= 'c'
    draw(keypress,oldx,oldy,newx,newy)
def rectangle(event):
    oldx= d1.get()
    oldy= d2.get()
    newx= d3.get()
    newy= d4.get()
    keypress= 'r'
    draw(keypress,oldx,oldy,newx,newy)
def line(event):
    oldx= d1.get()
    oldy= d2.get()
    newx= d3.get()
    newy= d4.get()
    keypress= 'l'
    draw(keypress,oldx,oldy,newx,newy)

def draw(keypress,oldx,oldy,newx,newy):
    color= colour_dropdown.get()
    if keypress=='c':
        draw_circle= canvas.create_oval(oldx,oldy,newx,newy, fill=color)
    if keypress=='r':
        draw_rectangle= canvas.create_rectangle(oldx,oldy,newx,newy, fill=color)
    if keypress=='l':
        draw_line= canvas.create_line(oldx,oldy,newx,newy, fill=color)
    
    
root.bind("<c>",circle)
root.bind("<r>",rectangle)
root.bind("<l>",line)


root.mainloop()