

from tkinter import *
import random

root=Tk()

root.title("Random Word Generator")
root.geometry("500x500")

randword= Label(root)
words=["a", "b" ,"c" ,"d", "e" ,"f", "g", "h" ,"i","j" ,"k", "l", "m" ,"n" ,"o", "p" ,"q", "r", "s" ,"t" ,"u" ,"v" ,"w" ,"x", "y","z"]

def randomint():
    random_no  = random.randint(0, 26)
    random_no2 = random.randint(0, 26)
    random_no3 = random.randint(0, 26)
    random_no4 = random.randint(0, 26)
    random_word  = words[random_no]
    random_word2 = words[random_no2]
    random_word3 = words[random_no3]
    random_word4 = words[random_no4]
    print(random_word, random_word2,random_word3,random_word4)
    randword["text"]= str(random_word) +str(random_word2)+str(random_word3)+str(random_word4)
    
    
btn1 = Button(root, text="Find Your Random Text! ", command = randomint)
btn1.place(relx= 0.5,rely = 0.4, anchor = CENTER )

randword.place(relx= 0.5,rely = 0.5, anchor = CENTER )
 
root.mainloop()