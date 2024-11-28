from tkinter import *
import speedtest   
 
root = Tk()
root.config(bg="#dee8f1")
root.title("Internet Speed Test")
root.geometry("800x800")

label= Label(root,text= "Speed Test",font=("Arial",30,"bold"), fg="Orange")
label.place(relx=0.5,rely=0.1,anchor=CENTER)

label1= Label(root,text= "Download Speed",font=("Arial",30,"bold"), fg="red")
label1.place(relx=0.25,rely=0.5,anchor=CENTER)

label2= Label(root,text= "Upload Speed",font=("Arial",30,"bold"), fg="red")
label2.place(relx=0.75,rely=0.5,anchor=CENTER)

label3= Label(root,font=("Arial",30,"bold"), fg="black")
label3.place(relx=0.25,rely=0.6,anchor=CENTER)

label4= Label(root,font=("Arial",30,"bold"), fg="black")
label4.place(relx=0.75,rely=0.6,anchor=CENTER)

def speedtest1():
    st= speedtest.Speedtest()
    download_speed= round(st.download()/1000000,2)
    print(download_speed)
    label3['text']=str(download_speed) + "  MBPS"
    upload_speed= round(st.upload()/1000000,2)
    print(upload_speed)
    label4['text']=str(upload_speed) + "  MBPS"
    

button1= Button(root, text="Check Computer Speed",command=speedtest1)
button1.place(relx=0.5,rely=0.3,anchor=CENTER)

root.mainloop()