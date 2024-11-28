class Parent:
    def __init__(self):
        print("Welcome to Our Store!")
        
    def menu(dish):
        if dish=="burger":
            print("You can give Add-ons: Cheese or Jalapeno")
        elif dish=="Icecream":
            print("You can give Add-ons: Chocolate or Vanilla")
        else:
            print("Your Dish is Invalid")
            
    def amount(dish,add_on):
        if dish=="burger" and add_on=="Cheese":
            print("Your Amount is 80 Rupees.")
        elif dish=="burger" and add_on=="Jalapeno":
            print("Your Amount is 95 Rupees.")
        elif dish=="Icecream" and add_on=="Chocolate":
            print("Your Amount is 45 Rupees.")
        elif dish=="Icecream" and add_on=="Vanilla":
            print("Your Amount is 40 Rupees.")
         
class Child1(Parent):
    def __init__(self,dish):
        self.new_dish=dish
    
    def get_menu(self):
        Parent.menu(self.new_dish)
        
class Child2(Parent):
    def __init__(self,dish,add_on):
        self.new_dish=dish
        self.new_add_on=add_on
          
    def get_amount(self):
        Parent.amount(self.new_dish , self.new_add_on)
        
customer1= Child1("burger")
customer1.get_menu()

customer2= Child2("burger","Cheese")
customer2.get_amount()