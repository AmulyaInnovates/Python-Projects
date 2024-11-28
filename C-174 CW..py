from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root = Tk()
root.geometry("900x500")
root.title('Rdonalds')

burger= ImageTk.PhotoImage(Image.open("burger1.png"))
burger_image= Label(root)
burger_image["image"]= burger
burger_image.place(relx=0.7, rely=0.5,anchor=CENTER)

label_heading= Label(root,text= "RDonalds",fg="Orange", font=("Arial",30,"bold"))
label_heading.place(relx=0.12, rely=0.1,anchor=CENTER)

label_dish= Label(root,text= "Select Your Dish")
label_dish.place(relx=0.06, rely=0.2,anchor=CENTER)

dish=["Burger","Ice-Cream"]
combobox1= ttk.Combobox(root,state="readonly",values=dish)
combobox1.place(relx=0.25, rely=0.2,anchor=CENTER)


label_add_on= Label(root,text= "Select Your Add-Ons")
label_add_on.place(relx=0.06, rely=0.4,anchor=CENTER)

Addon=[]
combobox2= ttk.Combobox(root,state="readonly",values=Addon)
combobox2.place(relx=0.25, rely=0.4,anchor=CENTER)

button1= Button(root,text= "Check Add-Ons", command=customer1.get_menu())
button1.place(relx=0.06,rely=0.3,anchor=CENTER)

button2= Button(root,text= "Calculate Amount",command=customer2.get_amount())
button2.place(relx=0.06,rely=0.5,anchor=CENTER)

label_amount= Label(root,text= "")
label_amount.place(relx=0.2, rely=0.75,anchor=CENTER)



class Parent:
    def __init__(self):
        print("Welcome to Our Store!")
        
    def menu(dish):
        if dish=="burger":
            print("You can give Add-ons: Cheese or Jalapeno")
            Addon=["Jalapeno","Cheese"]
            combobox2["values"]=Addon
        elif dish=="Icecream":
            print("You can give Add-ons: Chocolate or Vanilla")
            Addon=["Chocolate","Vanilla"]
            combobox2["values"]=Addon
        else:
            print("Your Dish is Invalid")
            
    def amount(dish,add_on):
        if dish=="burger" and add_on=="Cheese":
            print("Your Amount is 80 Rupees.")
            label_amount['text']= "Your Amount is 80 Rupees."
        elif dish=="burger" and add_on=="Jalapeno":
            print("Your Amount is 95 Rupees.")
            label_amount['text']= "Your Amount is 95 Rupees."
        elif dish=="Icecream" and add_on=="Chocolate":
            print("Your Amount is 45 Rupees.")
            label_amount['text']= "Your Amount is 45 Rupees."
        elif dish=="Icecream" and add_on=="Vanilla":
            print("Your Amount is 40 Rupees.")
            label_amount['text']= "Your Amount is 40 Rupees."

class Child1(Parent):
    def __init__(self,dish):
        self.new_dish=dish
    
    def get_menu(self):
        nd=combobox1.get()
        Parent.menu(nd)
        
class Child2(Parent):
    def __init__(self,dish,add_on):
        self.new_dish=dish
        self.new_add_on=add_on
          
    def get_amount(self):
        nd=combobox1.get()
        ad=combobox2.get()
        Parent.amount(nd , ad)
        
customer1= Child1(combobox1.get())
customer1.get_menu()

customer2= Child2(combobox2.get(),combobox1.get())
customer2.get_amount()
root.mainloop()