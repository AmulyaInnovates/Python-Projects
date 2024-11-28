from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root = Tk()  
root.geometry("900x1200") 
root.title("Time")
clock_image= ImageTk.PhotoImage(Image.open ("map.jpg"))


india_label = Label(root,text="India")
india_label.place(relx=0.2,rely=0.05, anchor= CENTER)
 
india_clock=Label(root)
india_clock["image"]=clock_image
india_clock.place(relx=0.2,rely=0.35, anchor= CENTER)
 
india_time = Label(root)
india_time.place(relx=0.2,rely=0.65, anchor= CENTER)

usa_label = Label(root,text="usa")
usa_label.place(relx=0.7,rely=0.05, anchor= CENTER)
 
usa_clock=Label(root)
usa_clock["image"]=clock_image
usa_clock.place(relx=0.7,rely=0.35, anchor= CENTER)
 
usa_time = Label(root)
usa_time.place(relx=0.7,rely=0.65, anchor= CENTER)

australia_label = Label(root,text="Australia")
australia_label.place(relx=0.2,rely=0.05, anchor= CENTER)
 
australia_clock=Label(root)
australia_clock["image"]=clock_image
australia_clock.place(relx=0.2,rely=0.35, anchor= CENTER)
 
australia_time = Label(root)
australia_time.place(relx=0.2,rely=0.65, anchor= CENTER)


japan_label = Label(root,text="India")
japan_label.place(relx=0.2,rely=0.05, anchor= CENTER)
 
japan_clock=Label(root)
japan_clock["image"]=clock_image
japan_clock.place(relx=0.2,rely=0.35, anchor= CENTER)
 
japan_time = Label(root)
japan_time.place(relx=0.2,rely=0.65, anchor= CENTER)


class India():
    def times(self):
        home=pytz.timezone('Asia/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        india_time["text"]="Time :"+ current_time
        india_time.after(200,self.times)
        
        	
class usa():
    def times(self):
        home2=pytz.timezone('US/Central')
        local_time2=datetime.now(home2)
        current_time2=local_time2.strftime("%H:%M:%S")
        usa_time["text"]="Time :"+ current_time2
        usa_time.after(200,self.times)
        
class Australia():
            def times(self):
                home3=pytz.timezone('Australia/ACT')
                local_time3=datetime.now(home3)
                current_time3=local_time3.strftime("%H:%M:%S")
                Australia_time["text"]="Time :"+ current_time3
                Australia_time.after(200,self.times)
                
                	
class Japan():
            def times(self):
                home4=pytz.timezone('Japan/JST')
                local_time4=datetime.now(home4)
                current_time4=local_time4.strftime("%H:%M:%S")
                Japan["text"]="Time :"+ current_time4
                Japan.after(200,self.times)
        
obj_india=India()
obj_usa=usa()
obj_Australia=Australia()
obj_Japan=Japan()
	
india_btn=Button(root,text="Show Time",command=obj_india.times)
india_btn.place(relx=0.2,rely=0.8, anchor= CENTER)

usa_btn=Button(root,text="Show Time",command=obj_usa.times)
usa_btn.place(relx=0.7,rely=0.8, anchor= CENTER)

Australia_btn=Button(root,text="Show Time",command=obj_Australia.times)
Australia_btn.place(relx=0.2,rely=0.8, anchor= CENTER)

Japan_btn=Button(root,text="Show Time",command=obj_Japan.times)
Japan_btn.place(relx=0.7,rely=0.8, anchor= CENTER)

root.mainloop()