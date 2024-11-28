import requests
import json
import tkinter as tk

# Creating the root window
root = tk.Tk()
root.geometry("800x800")

# Sending the request to the API URL
url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=24bd5c789e7d4f18b227a3e5d05e99c6"
api_request = requests.get(url)
open_bbc_page = json.loads(api_request.content)

# Extracting news titles and descriptions
title1 = open_bbc_page["articles"][0]["title"]
desc1 = open_bbc_page["articles"][0]["description"]
title2 = open_bbc_page["articles"][1]["title"]
desc2 = open_bbc_page["articles"][1]["description"]
title3 = open_bbc_page["articles"][2]["title"]
desc3 = open_bbc_page["articles"][2]["description"]
title4 = open_bbc_page["articles"][3]["title"]
desc4 = open_bbc_page["articles"][3]["description"]
title5 = open_bbc_page["articles"][4]["title"]
desc5 = open_bbc_page["articles"][4]["description"]

# Creating label for "BBC News Update"
newsupdate = tk.Label(root, text="BBC News Update", font=("Arial", 20, "bold"))
newsupdate.place(x=200, y=20)

# Creating labels for news titles
news1 = tk.Label(root, text="Title 1: "+title1, font=("Arial", 16, "bold"), fg="blue", wraplength=500, justify="left")
news1.place(x=50, y=80, anchor="nw")
news2 = tk.Label(root, text="Title 2: "+title2, font=("Arial", 16, "bold"), fg="blue", wraplength=500, justify="left")
news2.place(x=50, y=220, anchor="nw")
news3 = tk.Label(root, text="Title 3: "+title3, font=("Arial", 16, "bold"), fg="blue", wraplength=500, justify="left")
news3.place(x=50, y=360, anchor="nw")
news4 = tk.Label(root, text="Title 4: "+title4, font=("Arial", 16, "bold"), fg="blue", wraplength=500, justify="left")
news4.place(x=50, y=500, anchor="nw")
news5 = tk.Label(root, text="Title 5: "+title5, font=("Arial", 16, "bold"), fg="blue", wraplength=500, justify="left")
news5.place(x=50, y=640, anchor="nw")

# Creating labels for news descriptions
news_desc1 = tk.Label(root, text="Description: "+desc1, font=("Arial", 12, "bold"), fg="black", wraplength=500, justify="left")
news_desc1.place(x=50, y=140, anchor="nw")
news_desc2 = tk.Label(root, text="Description: "+desc2, font=("Arial", 12, "bold"), fg="black", wraplength=500, justify="left")
news_desc2.place(x=50, y=280, anchor="nw")
news_desc3 = tk.Label(root, text="Description: "+desc3, font=("Arial", 12, "bold"), fg="black", wraplength=500, justify="left")
news_desc3.place(x=50, y=420, anchor="nw")
news_desc4 = tk.Label(root, text="Description: "+desc4, font=("Arial", 12, "bold"), fg="black", wraplength=500, justify="left")
news_desc4.place(x=50, y=560, anchor="nw")
news_desc5 = tk.Label(root, text="Description: "+desc5, font=("Arial", 12, "bold"), fg="black", wraplength=500, justify="left")
news_desc5.place(x=50, y=700, anchor="nw")


root.mainloop()