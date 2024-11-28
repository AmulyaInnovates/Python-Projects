from tkinter import *
import random

from PIL import ImageTk, Image
root=Tk()

root.title("endless POKEMON game")
root.geometry("600x400")

root.configure(background = "light green")

img=ImageTk.PhotoImage(Image.open ("button.jpg"))

player1= Label(root,text= "Player 1",bg= "red",fg= "white")
player1.place(relx= 0.1 , rely=0.3 ,anchor= CENTER)

player2= Label(root,text= "Player 2",bg= "red",fg= "white")
player2.place(relx= 0.9 , rely=0.3 ,anchor= CENTER)

player1_score= Label(root,bg= "royal blue",fg= "white")
player1_score.place(relx= 0.1 , rely=0.4 ,anchor= CENTER)

player2_score= Label(root,bg= "royal blue",fg= "white")
player2_score.place(relx= 0.9 , rely=0.4 ,anchor= CENTER)

random_poke_label= Label(root,bg= "white",fg= "black")
random_poke_label.place(relx= 0.5 , rely=0.5 ,anchor= CENTER)


pikachu=ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
bulbasour=ImageTk.PhotoImage(Image.open ("bulbasour.jpg"))
charmender=ImageTk.PhotoImage(Image.open ("charmender.jpg"))
squirtle=ImageTk.PhotoImage(Image.open ("squirtle.jpg"))
ratata=ImageTk.PhotoImage(Image.open ("ratata.jpg"))
nidoking=ImageTk.PhotoImage(Image.open ("nidoking.jpg"))
jigglypuff=ImageTk.PhotoImage(Image.open ("jigglypuff.jpg"))
meowth=ImageTk.PhotoImage(Image.open ("meowth.jpg"))
persion=ImageTk.PhotoImage(Image.open ("persion.jpg"))
abra=ImageTk.PhotoImage(Image.open ("abra.jpg"))
kadabra=ImageTk.PhotoImage(Image.open ("kadabra.jpg"))
Iyvasour=ImageTk.PhotoImage(Image.open ("Iyvasour.jpg"))

pokemon_list= [pikachu,bulbasour,Iyvasour,charmender,squirtle,ratata,jigglypuff,meowth,persion,abra,kadabra,nidoking]

power_list= [200,60,100,50,50,40,70,60,70,30,70,90]

label= Label(root)
label.place(relx=0.5,rely=0.5, anchor= CENTER)

v_player1_score= 0
def player1():
    global v_player1_score 
    random_no = random.randint(0,11)
    random_pokemon= pokemon_list[random_no]
    label["image"]= random_pokemon
    
    random_power_list = power_list[random_no]
    v_player1_score= v_player1_score + random_power_list
    player1_score["text"] =  str(v_player1_score)
    
player1_btn= Button(root,image= img , command= player1)
player1_btn.place(relx= 0.1, rely= 0.6, anchor= CENTER)

v_player2_score= 0
def player2():
    global v_player2_score 
    random_no = random.randint(0,10)
    random_pokemon= pokemon_list[random_no]
    label["image"]= random_pokemon
    
    random_power_list = power_list[random_no]
    v_player2_score= v_player2_score + random_power_list
    player2_score["text"] =  str(v_player2_score)
    
player2_btn= Button(root,image= img , command= player2)
player2_btn.place(relx= 0.9, rely= 0.6, anchor= CENTER)


root.mainloop()