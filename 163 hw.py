from tkinter import *
from tkinter import messagebox

root= Tk()
root.title("Fever Report HOMEWORK")
root.geometry("600x600")

question1_radiobuton= StringVar(value= "0")
Question1= Label(root,text= "Do You Experience Shortess In Breathing?")
Question1.pack()
question1_rb1= Radiobutton(root, text= "Yes" , variable= question1_radiobuton ,value= "yes")
question1_rb1.pack()
question1_rb2= Radiobutton(root, text= "No" , variable= question1_radiobuton ,value= "No")
question1_rb2.pack()

question2_radiobuton= StringVar(value= "0")
Question2= Label(root,text= "Do You Swollen in your ankles /legs?")
Question2.pack()
question2_rb1= Radiobutton(root, text= "Yes" , variable= question2_radiobuton ,value= "yes")
question2_rb1.pack()
question2_rb2= Radiobutton(root, text= "No" , variable= question2_radiobuton ,value= "No")
question2_rb2.pack()

question3_radiobuton= StringVar(value= "0")
Question3= Label(root,text= "Do You Feel Confusion or loss of memory?")
Question3.pack()
question3_rb1= Radiobutton(root, text= "Yes" , variable= question3_radiobuton ,value= "yes")
question3_rb1.pack()
question3_rb2= Radiobutton(root, text= "No" , variable= question3_radiobuton ,value= "No")
question3_rb2.pack()

question4_radiobuton= StringVar(value= "0")
Question4= Label(root,text= "Do You Experience Shortess In Breathing While Sleeping?")
Question4.pack()
question4_rb1= Radiobutton(root, text= "Yes" , variable= question4_radiobuton ,value= "yes")
question4_rb1.pack()
question4_rb2= Radiobutton(root, text= "No" , variable= question4_radiobuton ,value= "No")
question4_rb2.pack()

question5_radiobuton= StringVar(value= "0")
Question5= Label(root,text= "Do You Experience Sneezing / coughing that produces blood??")
Question5.pack()
question3_rb5= Radiobutton(root, text= "Yes" , variable= question5_radiobuton ,value= "yes")
question3_rb5.pack()
question3_rb5= Radiobutton(root, text= "No" , variable= question5_radiobuton ,value= "No")
question3_rb5.pack()

def fever_score():
    score= 0
    if question1_radiobuton.get()=="yes" :
       score= score+10
       print(score)
       
    if question2_radiobuton.get()=="yes" :
       score= score+10
       print(score)
       
    if question3_radiobuton.get()=="yes" :
       score= score+10
       print(score)
       
    if question4_radiobuton.get()=="yes" :
       score= score+10
       print(score)
       
    if question5_radiobuton.get()=="yes" :
       score= score+10
       print(score)
       
    if score <= 10:
       messagebox.showinfo("Report","You dont need to go to Doctor!")
       
    elif score > 10 and score <= 30:
       messagebox.showinfo("Report","You probably should go to Doctor!")
       
    else :
       messagebox.showinfo("Report","I STRONGLY ADVICE YOU TO GO TO THE DOCTOR!!")
       
       
btn= Button(root,text= "Click ME To See Your Report" , command= fever_score)
btn.pack()

root.mainloop()