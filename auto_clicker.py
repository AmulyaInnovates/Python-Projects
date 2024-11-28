import pyautogui
import time
import tkinter as tk

# create the GUI window
root = tk.Tk()
root.title("Auto Clicker")

# create the duration input label and field
duration_label = tk.Label(root, text="Duration (in seconds): ")
duration_label.pack(side=tk.LEFT)
duration_entry = tk.Entry(root)
duration_entry.pack(side=tk.LEFT)

# create the timing input label and field
timing_label = tk.Label(root, text="Timing (in clicks per second): ")
timing_label.pack(side=tk.LEFT)
timing_entry = tk.Entry(root)
timing_entry.pack(side=tk.LEFT)

# function to start the auto clicker
def start_clicker():
    # get the duration and timing values from the GUI
    duration = int(duration_entry.get())
    timing = float(timing_entry.get())
    
    # calculate the number of clicks based on duration and timing
    num_clicks = int(duration * timing)
    
    # loop through the specified number of clicks and simulate a left-click
    for i in range(num_clicks):
        pyautogui.click()
        time.sleep(1/timing)  # delay between clicks based on timing

# create the start button and pack it into the GUI
start_button = tk.Button(root, text="Start Auto Clicker", command=start_clicker)
start_button.pack()

# run the GUI loop
root.mainloop()
