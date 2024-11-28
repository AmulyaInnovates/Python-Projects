import tkinter as tk

class Users:
    dictionary = {}
    
    @classmethod
    def addUser(cls, key, value):
        cls.dictionary[key] = value

class GetUsers(Users):
    def __init__(self, master):
        self.master = master
        self.master.title("Add User")
        
        self.label_username = tk.Label(master, text="Username")
        self.label_username.pack()
        
        self.entry_username = tk.Entry(master)
        self.entry_username.pack()
        
        self.label_email = tk.Label(master, text="Email")
        self.label_email.pack()
        
        self.entry_email = tk.Entry(master)
        self.entry_email.pack()
        
        self.button_submit = tk.Button(master, text="Submit", command=self.add_user)
        self.button_submit.pack()
        
        self.user_list = ""
        
    def add_user(self):
        username = self.entry_username.get()
        email = self.entry_email.get()
        self.addUser(username, email)
        
        self.user_list += f"{username}: {email}\n"
        
        self.entry_username.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        
        self.label_username.config(text=f"Last added user: {username}")
        self.label_email.config(text=f"Email: {email}")
        
        print("User list:")
        print(self.user_list)
        

if __name__ == "__main__":
    root = tk.Tk()
    app = GetUsers(root)
    root.mainloop()
 