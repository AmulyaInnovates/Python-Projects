from tkinter import*

root=  Tk()
root.title("C-178")
root.geometry("500x500")

class JUICE:
    
    def __init__(self,fruit_name,quantity):
        self.fruit= fruit_name
        self.quantity= int(quantity)
        self.__cost= 75
    
    def __calculatecost(self):
        total_amount= self.__cost*self.quantity
        print("Your Total Cost Is :- "+ str(total_amount))
        if self.fruit == "Apple":
            calories= self.quantity *52

        elif self.fruit == "Orange":
            calories= self.quantity *47
            
        elif self.fruit == "Mango":
            calories= self.quantity *60
            
        print("calories count for " + self.fruit +" of quantity " + str(self.quantity) + " is " + str(calories))
    
    def getamount(self):
        self.__calculatecost()
 
def order_juice():
    fruit="Mango"
    quantity= 20
    obj1= JUICE(fruit,quantity)
    obj1.getamount() 
    
btn= Button(root,text="TOTAL AMOUNT" , command= order_juice)
btn.pack()
root.mainloop()