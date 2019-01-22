from tkinter import *
def show_entry_fields():
   x=open("Records.txt","a")
   x.write("\n\nName: %s\nEmail: %s\nPhone: %s\nAddress line1: %s\nAddress line 2: %s\nPassword: %s"% (txt.get(), txt1.get(), txt2.get(),txt3.get(),txt4.get(), pwd1.get()))
   x.close()   
   txt.delete(0,END)
   txt1.delete(0,END)
   txt2.delete(0,END)
   txt3.delete(0,END)
   txt4.delete(0,END)
   pwd1.delete(0,END)
   pwd3.delete(0,END)

def clean():
    txt.delete(0,END)
    txt1.delete(0,END)
    txt2.delete(0,END)
    txt3.delete(0,END)
    txt4.delete(0,END)
    pwd1.delete(0,END)
    pwd3.delete(0,END)


window=Tk()
window.geometry('650x650')
window.configure(bg='black')
window.title("Registration Form")

#Photo
photo1=PhotoImage(file="D:\\Downloads\\Avenger.gif")
Label(window, image=photo1, bg="black").place(x=0,y=0)

#Name Label
lbl=Label(window,text="Name:")
lbl.configure(bg='black',fg='white',font=('Arial',15))
lbl.place(x=90,y=50)

#Name textbox
txt=Entry(window,width=30)
txt.place(x=180,y=50)
txt.configure(font=('Arial',15))
    

#E-mail Label
lbl1=Label(window,text="E-mail:")
lbl1.configure(bg='black',fg='white',font=('Arial',15))
lbl1.place(x=90,y=100)

#E-mail textbox
txt1=Entry(window,width=30)
txt1.place(x=180,y=100)
txt1.configure(font=('Arial',15))

#Phone no Label
lbl2=Label(window,text="Phone Number:")
lbl2.configure(bg='black',fg='white',font=('Arial',15))
lbl2.place(x=40,y=150)

#Phone textbox
txt2=Entry(window,width=20)
txt2.place(x=180,y=150)
txt2.configure(font=('Arial',15))

#Address Label
lbl2=Label(window,text="Address line 1:")
lbl2.configure(bg='black',fg='white',font=('Arial',15))
lbl2.place(x=40,y=200)

#Address textbox
txt3=Entry(window,width=30)
txt3.place(x=180,y=200)
txt3.configure(font=('Arial',15))

#Address Label2
lbl2=Label(window,text="Address line 2:")
lbl2.configure(bg='black',fg='white',font=('Arial',15))
lbl2.place(x=40,y=250)

#Address textbox2
txt4=Entry(window,width=30)
txt4.place(x=180,y=250)
txt4.configure(font=('Arial',15))

#Password Label
pwd=Label(window,text="Password:")
pwd.configure(bg='black',fg='white',font=('Arial',15))
pwd.place(x=70,y=310)

#Password textbox
pwd1=Entry(window,show='*',width=30)
pwd1.place(x=180,y=310)
pwd1.configure(font=('Arial',15))

#Confirm Password Label
pwd2=Label(window,text="Confirm Password:")
pwd2.configure(bg='black',fg='White',font=('Arial',15))
pwd2.place(x=5,y=360)

#Confirm Password textbox
pwd3=Entry(window,show='*',width=30)
pwd3.place(x=180,y=360)
pwd3.configure(font=('Arial',15))

while pwd1.get()==pwd3.get():
   continue
   

#Submit Button
btn=Button(window,text='Submit',height=2,width=10,command=show_entry_fields)
btn.place(x=180,y=410)

#Reset Button
btn1=Button(window,text='Reset',height=2,width=10,command=clean)
btn1.place(x=300,y=410)


           

