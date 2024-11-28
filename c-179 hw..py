import tkinter as tk
import random

class Game:
    def __init__(self):
        self.__score = 0
        self.text = ["red", "blue", "green", "yellow", "orange", "purple"]
        self.color = ["black", "white", "gray", "brown", "pink", "violet"]
        
        # Create a label to display the score
        self.label_score = tk.Label(root, text="Score: 0", font=("Helvetica", 20), bg="#9fd0c2")
        self.label_score.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        
        # Create an entry element to get user input
        self.input_value = tk.Entry(root, font=("Helvetica", 20))
        self.input_value.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        
    def updateGame(self):
        self.random_number_for_text = random.randint(0, len(self.text)-1)
        self.random_number_for_color = random.randint(0, len(self.color)-1)
        label_name.config(text=self.text[self.random_number_for_text], fg=self.color[self.random_number_for_color])
    
    def __update_score(self, input_value):
        if input_value.lower() == self.color[self.random_number_for_color]:
            print(self.color[self.random_number_for_color])
            self.__score += random.randint(0, 10)
            self.label_score.config(text="Score: " + str(self.__score))
        
    def get_user_value(self, input_value):
        self.__update_score(input_value.get())
        self.input_value.delete(0, tk.END)

# Create a new tkinter window
root = tk.Tk()
root.minsize(650,650)
root.maxsize(650,650)

# Set the background color of the root window
root.configure(background="#9fd0c2")

# Create a label to display the random color name
label_name = tk.Label(root, font=("Helvetica", 30), bg="white")
label_name.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create the game object
game = Game()

# Create a button to call the get_user_value() function
button_check = tk.Button(root, text="Check", command=lambda: game.get_user_value(game.input_value), bg="#9fd0c2", fg="black", relief=tk.FLAT, padx=10, pady=5, font=("Helvetica", 20))
button_check.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Create a button to call the updateGame() function
button_start = tk.Button(root, text="Start", command=game.updateGame, bg="#9fd0c2", fg="black", relief=tk.FLAT, padx=10, pady=5, font=("Helvetica", 20))
button_start.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Run the main loop
root.mainloop()
