from tkinter import*

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.title('Encapsulation')

class userDB:
    def __init__(self):
        self.__username = "Amulya"
        self.__password = "shells16"
        self.captcha = "123"

    def showUser(self):
        label_name.config(text="Name : " + self.__username)
        label_password.config(text="Password : " + self.__password)
        label_captcha.config(text="Captcha : " + self.captcha)
        
user = userDB()

label_name= Label(root,text="Name : ")
label_name.place(relx=0.3,rely=0.1,anchor=CENTER)

label_password= Label(root,text="Password : ")
label_password.place(relx=0.3,rely=0.2,anchor=CENTER)

label_captcha= Label(root,text="Captcha : ")
label_captcha.place(relx=0.3,rely=0.3,anchor=CENTER)

entry_name= Entry(root)
entry_name.place(relx=0.5,rely=0.1,anchor=CENTER)

entry_password= Entry(root)
entry_password.place(relx=0.5,rely=0.2,anchor=CENTER)

entry_captcha= Entry(root)
entry_captcha.place(relx=0.5,rely=0.3,anchor=CENTER)

output_name=Label(root)
output_name.place(relx=0.5,rely=0.7,anchor=CENTER)

output_password=Label(root)
output_password.place(relx=0.5,rely=0.8,anchor=CENTER)

output_captcha=Label(root)
output_captcha.place(relx=0.5,rely=0.9,anchor=CENTER)



def addUser():
    global user
    user.__username = entry_name.get()
    user.__password = entry_password.get()
    user.captcha = entry_captcha.get()
    print("Details Updated")



show_profile_button = Button(root, text="Show Profile", command=user.showUser)
show_profile_button.place(relx=0.7, rely=0.5, anchor="center")

update_button = Button(root, text="Update Login Details", command=addUser)
update_button.place(relx=0.2, rely=0.5, anchor="center")

root.mainloop()
