from tkinter import *
import random

from PIL import ImageTk, Image
root=Tk()

root.title("Endless Dice Game")
root.geometry("600x400")

root.configure(background = "yellow2")

img=ImageTk.PhotoImage(Image.open ("dice1.4.jpg"))

player1= Label(root,text= "Player 1",bg= "royal blue",fg= "white")
player1.place(relx= 0.1 , rely=0.3 ,anchor= CENTER)

player2= Label(root,text= "Player 2",bg= "royal blue",fg= "white")
player2.place(relx= 0.9 , rely=0.3 ,anchor= CENTER)

player1_score= Label(root,bg= "royal blue",fg= "white")
player1_score.place(relx= 0.1 , rely=0.4 ,anchor= CENTER)

player2_score= Label(root,bg= "royal blue",fg= "white")
player2_score.place(relx= 0.9 , rely=0.4 ,anchor= CENTER)

random_dice_label= Label(root,bg= "chocolate1",fg= "white")
random_dice_label.place(relx= 0.5 , rely=0.5 ,anchor= CENTER)

v_player1_score= 0
def player1():
    global v_player1_score 
    random_no = random.randint(1,6)
    random_dice_label["text"]= "Player 1 Dice Random Number: " + str(random_no) 
    v_player1_score = v_player1_score + random_no
    player1_score["text"]=str(v_player1_score)
    
player1_btn= Button(root,image= img , command= player1)
player1_btn.place(relx= 0.1, rely= 0.6, anchor= CENTER)

v_player2_score= 0
def player1():
    global v_player2_score 
    random_no = random.randint(1,6)
    random_dice_label["text"]= "Player 2 Dice Random Number: " + str(random_no) 
    v_player2_score = v_player2_score + random_no
    player2_score["text"]=str(v_player2_score)
    
player2_btn= Button(root,image= img , command= player1)
player2_btn.place(relx= 0.9, rely= 0.6, anchor= CENTER)

root.mainloop()