import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk

class AustraliaIndiaAndUSAMap(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("800x600")
        self.master.title("AustraliaIndiaandUSAMaps")

        # Load map images
        self.australia_map_photo = ImageTk.PhotoImage(Image.open("australia-map.jpeg"))
        self.india_map_photo = ImageTk.PhotoImage(Image.open("india-map.jpeg"))
        self.usa_map_photo = ImageTk.PhotoImage(Image.open("usa-map.jpeg"))
        self.japan_map_photo = ImageTk.PhotoImage(Image.open("japan-map.jpeg"))

        # Create map labels
        self.australia_map_label = tk.Label(self.master, width=150 ,height=100,image=self.australia_map_photo)
        self.australia_map_label.grid(row=0, column=0, padx=5, pady=5)

        self.india_map_label = tk.Label(self.master, width=150 ,height=100, image=self.india_map_photo)
        self.india_map_label.grid(row=0, column=1, padx=5, pady=5)

        self.usa_map_label = tk.Label(self.master, width=150 ,height=100, image=self.usa_map_photo)
        self.usa_map_label.grid(row=0, column=2, padx=5, pady=5)
        
        self.japan_map_label = tk.Label(self.master, width=150 ,height=100, image=self.japan_map_photo)
        self.japan_map_label.grid(row=0, column=3, padx=5, pady=5)
        
        # Create time labels
        self.australia_time_label = tk.Label(self.master, text="")
        self.australia_time_label.grid(row=1, column=0, pady=5)

        self.india_time_label = tk.Label(self.master, text="")
        self.india_time_label.grid(row=1, column=1, pady=5)

        self.usa_time_label = tk.Label(self.master, text="")
        self.usa_time_label.grid(row=1, column=2, pady=5)
        
        self.japan_time_label = tk.Label(self.master, text="")
        self.japan_time_label.grid(row=1, column=3, pady=5)
        
        # Create time buttons
        self.show_australia_time_button = tk.Button(self.master, text="Show Australia Time", command=lambda: self.show_time("Australia/Sydney"))
        self.show_australia_time_button.grid(row=2, column=0, pady=5)

        self.show_india_time_button = tk.Button(self.master, text="Show India Time", command=lambda: self.show_time("Asia/Kolkata"))
        self.show_india_time_button.grid(row=2, column=1, pady=5)

        self.show_usa_time_button = tk.Button(self.master, text="Show USA Time", command=lambda: self.show_time("America/New_York"))
        self.show_usa_time_button.grid(row=2, column=2, pady=5)
        
        self.show_japan_time_button = tk.Button(self.master, text="Show Japan Time", command=lambda: self.show_time("Asia/Tokyo"))
        self.show_japan_time_button.grid(row=2, column=3, pady=5)
        
    def show_time(self, timezone):
        now = datetime.now(timezone)
        current_time = now.strftime("%H:%M:%S")
        
        if timezone == "Australia/Sydney":
            self.australia_time_label.config(text=f"Current time in Australia: {current_time}")
            print(current_time)
        elif timezone == "Asia/Kolkata":
            self.india_time_label.config(text=f"Current time in India: {current_time}")
        elif timezone == "America/New_York":
            print(current_time)
            self.usa_time_label.config(text=f"Current time in USA: {current_time}")
            print(current_time)
        else:
            print("Invalid timezone")

root = tk.Tk()
app = AustraliaIndiaAndUSAMap(master=root)
app.master.update()
app.mainloop()
