
import mysql.connector
from tkinter import *

#Acts as a buffer to close former window and start new window.
def buffer(st1,obj):
      if st1=="reg":
         obj.destroy()
         register()
      elif st1=="log":
         obj.destroy()
         login()

      elif st1=="main":
         obj.destroy()
         main()

def main():
   root=Tk()
   root.geometry('650x700')
   root.title("Welcome")
   root.configure(bg='royal blue')

   #Welcome label
   lab=Label(root,text="Welcome",bg='royal blue')
   lab.place(x=180,y=250)
   lab.configure(font='Algerian 50 bold')

   #Register Window Button
   but=Button(root,text="Register",height=3,width=10,command=lambda: buffer("reg",root))
   but.place(x=190,y=400)
   but.configure(bg='green')

   but=Button(root,text="Setup",height=3,width=10,command=Setup_Database)
   but.place(x=400,y=400)
   but.configure(bg='green')

   #Login Window Button
   but1=Button(root,text="Login",height=3,width=10,command=lambda: buffer("log",root))
   but1.place(x=300,y=400)
   but1.configure(bg='green')
   #root.destroy()
   root.mainloop()

  
def Setup_Database():
     try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
        cursor=mydb.cursor()
        x=open("Server.sql","r")
        query = " ".join(x.readlines())
        cursor.execute(query)
     except:
        print("Database Already Exists!")

def login():
   log=Tk()
   log.title("Login page")
   log.geometry("650x700")
   log.configure(bg='royal blue')

   def check():
      records=mysql.connector.connect(host='localhost',user='root',passwd='root',database='server')
      cursors=records.cursor()
      val=str(box.get())
      cursors.execute('select Password from record where Email=%s;',(val,))
      pwd=cursors.fetchall()
      pwd1=box1.get()
      l=[(pwd1,)]
      if pwd==l:
         log.destroy()
         pro=Tk()
         pro.title("Profile page")
         pro.geometry("650x700")
         pro.configure(bg='royal blue')

         def searchdata():
            records=mysql.connector.connect(host='localhost',user='root',passwd='root',database='server')
            cursors=records.cursor()
            val=str(box2.get())
            cursors.execute('select * from record where Email=%s;',(val,))
            ent=cursors.fetchall()
            res.insert(END,ent)
         

         #Label for search
         lbl=Label(pro,text="Search Email:")
         lbl.configure(bg='royal blue',fg='black',font='Arial 15 bold')
         lbl.place(x=10,y=50)

         #Box for search
         box2=Entry(pro,width=40)
         box2.configure(font='Arial 15 bold')
         box2.place(x=100,y=50)

         #Submit button
         but=Button(pro,text="Search results",command=searchdata)
         but.place(x=200,y=100)

         #Result box
         res=Text(pro,height=15,width=65)
         res.place(x=100,y=150)

         
      else:
         pro=Tk()
         pro.title("Error occurred")
         pro.geometry("300x300")
         pro.configure(bg='royal blue')
      
   

   #Email id label
   lbl=Label(log,text="Email:")
   lbl.configure(font='Arial 20 bold',bg='royal blue')
   lbl.place(x=65,y=50)

   #Email box
   box=Entry(log,width=30)
   box.configure(font='Arial 20 bold')
   box.place(x=170,y=50)

   #PWD Label
   lbl1=Label(log,text="Password:")
   lbl1.configure(font='Arial 20 bold',bg='royal blue')
   lbl1.place(x=10,y=100)

   #PWD Box
   box1=Entry(log,width=30)
   box1.configure(font='Arial 20 bold')
   box1.place(x=170,y=100)

   #Submit button
   but=Button(log,text='Submit',height=3,width=10,command=check)
   but.place(x=190,y=150)

   #Back Button
   btn1=Button(log,text='Back',height=3,width=10,command=lambda: buffer("main",log))
   btn1.place(x=320,y=150)
   


def register():
   def record():
      records=mysql.connector.connect(host='localhost',user='root',passwd='root',database='server')
      cursors=records.cursor()
      val=(str(txt.get()),str(txt1.get()),str(txt2.get()),str(txt3.get()),str(txt4.get()),str(pwd1.get()))
      cursors.execute("insert into record values(%s,%s,%s,%s,%s,%s)",val)
      records.commit()
      txt.delete(0,END)
      txt1.delete(0,END)
      txt2.delete(0,END)
      txt3.delete(0,END)
      txt4.delete(0,END)
      pwd1.delete(0,END)
      pwd3.delete(0,END)
      buffer("main",window)

   def clean():
       txt.delete(0,END)
       txt1.delete(0,END)
       txt2.delete(0,END)
       txt3.delete(0,END)
       txt4.delete(0,END)
       pwd1.delete(0,END)
       pwd3.delete(0,END)


   window=Tk()
   window.geometry('650x700')
   window.configure(bg='royal blue')
   window.title("Registration Form")



   #Name Label
   lbl=Label(window,text="Name:")
   lbl.configure(bg='royal blue',fg='black',font='Arial 15 bold')
   lbl.place(x=90,y=50)

   #Name textbox
   txt=Entry(window,width=30)
   txt.place(x=220,y=50)
   txt.configure(font=('Arial',15))
       

   #E-mail Label
   lbl1=Label(window,text="E-mail:")
   lbl1.configure(bg='royal blue',fg='black',font='Arial 15 bold')
   lbl1.place(x=90,y=100)

   #E-mail textbox
   txt1=Entry(window,width=30)
   txt1.place(x=220,y=100)
   txt1.configure(font=('Arial',15))

   #Phone no Label
   lbl2=Label(window,text="Phone Number:")
   lbl2.configure(bg='royal blue',fg='black',font='Arial 15 bold')
   lbl2.place(x=30,y=150)

   #Phone textbox
   txt2=Entry(window,width=20)
   txt2.place(x=220,y=150)
   txt2.configure(font=('Arial',15))

   #Address Label
   lbl2=Label(window,text="Address line 1:")
   lbl2.configure(bg='royal blue',fg='black',font='Arial 15 bold')
   lbl2.place(x=40,y=200)

   #Address textbox
   txt3=Entry(window,width=30)
   txt3.place(x=220,y=200)
   txt3.configure(font=('Arial',15))

   #Address Label2
   lbl2=Label(window,text="Address line 2:")
   lbl2.configure(bg='royal blue',fg='black',font='Arial 15 bold')
   lbl2.place(x=40,y=250)

   #Address textbox2
   txt4=Entry(window,width=30)
   txt4.place(x=220,y=250)
   txt4.configure(font=('Arial',15))

   #Password Label
   pwd=Label(window,text="Password:")
   pwd.configure(bg='royal blue',fg='black',font='Arial 15 bold')
   pwd.place(x=70,y=310)

   #Password textbox
   pwd1=Entry(window,show='*',width=30)
   pwd1.place(x=220,y=310)
   pwd1.configure(font=('Arial',15))

   #Confirm Password Label
   pwd2=Label(window,text="Confirm Password:")
   pwd2.configure(bg='royal blue',fg='black',font='Arial 15 bold')
   pwd2.place(x=5,y=360)

   #Confirm Password textbox
   pwd3=Entry(window,show='*',width=30)
   pwd3.place(x=220,y=360)
   pwd3.configure(font=('Arial',15))

   """#Show textbox
   txt5=Text(window,height=12,width=50)
   txt5.place(x=220,y=465)"""

   #Submit Button
   btn=Button(window,text='Submit',height=2,width=10,command=record)
   btn.place(x=220,y=410)

   #Reset Button
   btn1=Button(window,text='Reset',height=2,width=10,command=clean)
   btn1.place(x=330,y=410)

   
   """btn2=Button(window,text='Quit',height=2, width=10,command=window.destroy)
   btn2.place(x=490,y=410)"""

   #Back Button
   btn1=Button(window,text='Back',height=2,width=10,command=lambda: buffer("main",window))
   btn1.place(x=450,y=410)
   

   window.mainloop()


#Program Starts Here
main()

  
              
