from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("Working On Canvas Using Functions")
root.geometry("600x600")


color_label=Label(root, text="Enter a Color :")
color_label.place(relx=0.6,rely=0.9, anchor= CENTER)

input_box = Entry(root)
input_box.insert(0,"black")
input_box.place(relx=0.8,rely=0.9, anchor= CENTER)

canvas= Canvas(root, height=510,width=590,bg="white",highlightbackground="lightgray")
canvas.pack()

img=ImageTk.PhotoImage(Image.open("start_point1.png"))
my_image=canvas.create_image(75,50,image=img)

direction= ""
oldx= 50
oldy= 50
newx= 50
newy= 50
   



def draw(direction, oldx, oldy, newx, newy):
            fill_color = input_box.get()
           
         
root.mainloop()