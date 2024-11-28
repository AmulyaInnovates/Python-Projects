from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root= Tk()
root.title("Juice Shop")
root.geometry("800x600")
root.config(bg="orange2")

label_heading= Label(root,text="Juice Shop",bg="orange2" ,font=("Bahnschrift Light" ,18 ,"bold"))
label_heading.place(relx=0.05,rely=0.1,anchor=W)

Juice= ImageTk.PhotoImage(Image.open ("logo.png"))
Juice_label= Label(root, image=Juice,bg="orange2")
Juice_label.place(relx=0.2,rely=0.4,anchor= CENTER)

Mango_img=ImageTk.PhotoImage(Image.open ("mango_img.png"))
Apple_img=ImageTk.PhotoImage(Image.open ("apple_img.png"))
Orange_img=ImageTk.PhotoImage(Image.open ("orange.png"))

fruit_img_label= Label(root ,bg="orange2")
fruit_img_label.place(relx=0.75,rely=0.8,anchor=CENTER)

fruit_label= Label(root,text="Select Fruit")
fruit_label.place(relx=0.96,rely=0.2,anchor= E)

fruit_list= ["Orange","Mango","Apple"]
fruit_dropdown= ttk.Combobox(root, state="readonly", values=fruit_list)
fruit_dropdown.place(relx=0.95,rely=0.25,anchor=E)

Quantity_label= Label(root,text="Enter Quantity")
Quantity_label.place(relx=0.96,rely=0.35,anchor= E)

Quantity_input= Entry(root)
Quantity_input.place(relx=0.95,rely=0.4,anchor=E)

Amount_label= Label(root)
Amount_label.place(relx=0.95,rely=0.7,anchor=E)

calerie_label= Label(root)
calerie_label.place(relx=0.95,rely=0.8,anchor=E)


class JUICE:
    
    def __init__(self,fruit_name,quantity):
        self.fruit= fruit_name
        self.quantity= int(quantity)
        self.__cost= 75
    
    def __calculatecost(self):
        total_amount= self.__cost*self.quantity
        Amount_label['text']=("Your Total Cost Is :- "+ str(total_amount))
        if self.fruit == "Apple":
            calories= self.quantity *52

        elif self.fruit == "Orange":
            calories= self.quantity *47
            
        elif self.fruit == "Mango":
            calories= self.quantity *60
            
        print("calories count for " + self.fruit +" of quantity " + str(self.quantity) + " is " + str(calories))
    
    def getamount(self):
        self.__calculatecost()
        






















root.mainloop()