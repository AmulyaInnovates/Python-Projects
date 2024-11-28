from tkinter import *
from tkinter import filedialog
from PIL import ImageTk , Image

root= Tk()
root.title("Fever Report HOMEWORK")
root.geometry("600x600")
root.configure(background= "black")

label_image= Label(root, highlightthickness= 5, bg="white")
label_image.place(relx=0.5,rely=0.5,anchor= CENTER)

img_path= ""
def openfile():
    global img_path
    img_path= filedialog.askopenfilename(title= " Open Your File",filetypes=(("Image Files","*.jpg *.gif *.jpg *.png *.jpeg" ),))
    print(img_path)
    im = Image.open(img_path)
    img= ImageTk.PhotoImage(im)
    label_image["image"]= img
    img.close()
    
def rotate():
        global img_path
        im = Image.open(img_path)
        img= ImageTk.PhotoImage(im.rotate(180))
        label_image["image"]= img
        print(img)
        img.close()
    
btn1= Button(root,text= "Rotate Image" , command=rotate)
btn1.place(relx=0.5, rely=0.9, anchor= CENTER)

btn= Button(root,text= "Open Image" , command=openfile)
btn.place(relx=0.5, rely=0.1, anchor= CENTER)

root.mainloop()