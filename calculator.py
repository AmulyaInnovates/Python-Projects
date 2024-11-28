import tkinter as tk 

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.input_string = ""
        
        # Create entry widget to display result
        self.result_entry = tk.Entry(self.master, textvariable=self.result_var, justify="right")
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Create buttons for numbers
        for i in range(1,10):
            button = tk.Button(self.master, text=str(i), width=5, height=2, command=lambda num=i: self.append_input(str(num)))
            button.grid(row=(3 - (i-1)//3), column=((i-1) % 3), padx=5, pady=5)
        
        # Create zero button
        zero_button = tk.Button(self.master, text="0", width=5, height=2, command=lambda: self.append_input("0"))
        zero_button.grid(row=4, column=0, padx=5, pady=5)
        
        # Create decimal button
        decimal_button = tk.Button(self.master, text=".", width=5, height=2, command=lambda: self.append_input("."))
        decimal_button.grid(row=4, column=1, padx=5, pady=5)
        
        # Create operator buttons
        add_button = tk.Button(self.master, text="+", width=5, height=2, command=lambda: self.append_input("+"))
        add_button.grid(row=1, column=3, padx=5, pady=5)
        
        subtract_button = tk.Button(self.master, text="-", width=5, height=2, command=lambda: self.append_input("-"))
        subtract_button.grid(row=2, column=3, padx=5, pady=5)
        
        multiply_button = tk.Button(self.master, text="*", width=5, height=2, command=lambda: self.append_input("*"))
        multiply_button.grid(row=3, column=3, padx=5, pady=5)
        
        divide_button = tk.Button(self.master, text="/", width=5, height=2, command=lambda: self.append_input("/"))
        divide_button.grid(row=4, column=3, padx=5, pady=5)
        
        equals_button = tk.Button(self.master, text="=", width=5, height=2, command=self.calculate_result)
        equals_button.grid(row=4, column=2, padx=5, pady=5)
        
        clear_button = tk.Button(self.master, text="C", width=5, height=2, command=self.clear_input)
        clear_button.grid(row=1, column=0, padx=5, pady=5)
        
    def append_input(self, char):
        self.input_string += char
        self.result_var.set(self.input_string)
        
    def calculate_result(self):
        try:
            result = eval(self.input_string)
            self.result_var.set(str(result))
            self.input_string = str(result)
        except:
            self.result_var.set("Error")
            self.input_string = ""
        
    def clear_input(self):
        self.input_string = ""
        self.result_var.set("0")

if __name__ == "__main__":
    amul = tk.Tk()
    calculator = Calculator(amul)
    amul.mainloop()
