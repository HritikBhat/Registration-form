import mysql.connector
from tkinter import *

def Install_Database():
     try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
        cursor=mydb.cursor()
        x=open("Server.sql","r")
        query = " ".join(x.readlines())
        cursor.execute(query)
     except:
        print("Database Already Exists!")
        
def show_entry_fields():
  i=0
  #Storing Data In The Database
  mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="server")
  
  mycursor=mydb.cursor()
  try:
     mycursor.execute("select Name from person")
     result=mycursor.fetchall()
     
     #Counts how much no of data is there
     for line in result:
        i+=1
     print(i)
     
  except:
     i=0
  val=(i+1,str(txt.get()), str(txt1.get()),str(txt2.get()),str(txt3.get()+txt4.get()), str(pwd1.get()))
  mycursor.execute("insert into person values (%s,%s,%s,%s,%s,%s)",val)
  mydb.commit()
  txt.delete(0,END)
  txt1.delete(0,END)
  txt2.delete(0,END)
  txt3.delete(0,END)
  txt4.delete(0,END)
  pwd1.delete(0,END)
  pwd3.delete(0,END)
  window.destroy()
  t1=EndPage()

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

#Submit Button
btn=Button(window,text='Submit',height=2,width=10,command=show_entry_fields)
btn.place(x=180,y=410)

#Reset Button
btn1=Button(window,text='Reset',height=2,width=10,command=clean)
btn1.place(x=300,y=410)

#Setting up database 
btn2=Button(window,text="Install Database",height=2,width=15,command=Install_Database)
btn2.place(x=400,y=410)

