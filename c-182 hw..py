from tkinter import *
from tkinter import ttk
from googletrans import Translator
 
root = Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.title('C-180')
root.config(bg = "#F2CCC3")

label_heading= Label(root,text= "LANGUAGE TRANSLATOR",fg="black", font=("Arial",30,"bold"),bg = "#F2CCC3")
label_heading.place(relx=0.5, rely=0.1,anchor=CENTER)

label_enter= Label(root,text= "Enter Text",fg="black",bg = "#F2CCC3")
label_enter.place(relx=0.1, rely=0.3,anchor=CENTER)

text_area= Text(root, height= 20, width=37)
text_area.place(relx=0.25,rely=0.6,anchor= CENTER)

dish=["English", "Hindi", "French", "German", "Spanish"]
combobox1= ttk.Combobox(root,state="readonly",values=dish)
combobox1.place(relx=0.3, rely=0.3,anchor=CENTER)
combobox1.set("English")


label_enter= Label(root,text= "Enter Text",fg="black",bg = "#F2CCC3")
label_enter.place(relx=0.67, rely=0.3,anchor=CENTER)

text_area2= Text(root, height= 20, width=37)
text_area2.place(relx=0.75,rely=0.6,anchor= CENTER)

combobox2= ttk.Combobox(root,state="readonly",values=dish)
combobox2.place(relx=0.85, rely=0.3,anchor=CENTER)
combobox2.set("Hindi")

def Translate():
    try:
        # Get input parameters
        src_lang = src_lang_cb.get()
        dest_lang = dest_lang_cb.get()
        text = text_area.get("1.0", "end-1c")

        # Translate text
        translator = Translator()
        translated = translator.translate(text, src=src_lang, dest=dest_lang)

        # Clear output textarea and display translated text
        text_area2.delete("1.0", "end")
        output_textarea.insert("end", translated.text)
    except:
        print("Try again")

button_open= Button(root,text="TRANSLATE", command= Translate)
button_open.place(relx=0.5,rely=0.95 , anchor= CENTER)


root.mainloop()