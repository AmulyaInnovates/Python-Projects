from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root=Tk()
root.minsize(650,650)
root.maxsize(650,650)

open_img= ImageTk.PhotoImage(Image.open ("open.png"))
save_img= ImageTk.PhotoImage(Image.open ("save.png"))
exit_img= ImageTk.PhotoImage(Image.open ("exit.jpg"))

L_file_name= Label(root, text= "File Name =")
L_file_name.place(relx=0.45,rely=0.04,anchor= CENTER)

input_file= Entry(root)
input_file.place(relx=0.60,rely=0.04,anchor= CENTER)

text_area= Text(root, height= 34, width=80)
text_area.place(relx=0.5,rely=0.5,anchor= CENTER)


name=""
def open_file():
    global name 
    input_file.delete(0, END)
    text_area.delete(1.0, END)
    text_file= filedialog.askopenfilename(title= " Open Your File",filetypes=(("Text Files","*.txt"),))
    print(text_file)
    name= os.path.basename(text_file)
    edited_name= name.split(".")[0]
    root.title(edited_name)
    input_file.insert(0, edited_name)
    text_file= open(name,"r")
    entire_file= text_file.read()
    text_area.insert(END, entire_file)
    text_file.close()
    
def save():
    input_name= input_file.get()
    file= open(input_name + ".txt" , "w")
    text= text_area.get("1.0" , END)
    print(text)
    file.write(text)
    input_file.delete(0, END)
    text_area.delete(1.0 ,END)
    messagebox.showinfo("Updated" , "Success")
    
def exit_window():
    root.destroy()
    
button_open= Button(root, image= open_img , command= open_file)
button_open.place(relx=0.12,rely=0.04 , anchor= CENTER)
button_save=Button(root,image=save_img,command=save)
button_save.place(relx=0.06,rely=0.04,anchor= CENTER)
button_exit= Button(root, image=exit_img, command= exit_window)
button_exit.place(relx=0.18,rely=0.04, anchor= CENTER)

root.mainloop()