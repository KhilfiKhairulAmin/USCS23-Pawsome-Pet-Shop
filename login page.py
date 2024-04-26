from tkinter import *
from tkinter import messagebox
from db import loadUsers, saveUsers
from catalogue import shopCatalogue

show = Tk()
users = loadUsers()

#screen
show.title('LOGIN PAGE')
show.geometry('1000x600+300+200')
show.configure(bg="white")
show.resizable(False,False)


#signup
def signin():
    username=user.get()
    password=passw.get()

    uid = -1
    valid_credentials = False
    for u in users:
        if u["username"] == username and u["password"] == password:
            valid_credentials = True
            uid = u["id"]
            break

    if valid_credentials:
        show.destroy()
        #app
        shopCatalogue(uid).mainloop()
        return

    elif username=="" or password=="":
        messagebox.showerror("Error","All fields are required")

    else:
        messagebox.showerror("Error","Invalid username or password")


#signup
def signup_command():
    window = Toplevel(show)

    window.title('SIGN UP PAGE')
    window.geometry('500x600+300+200')
    window.configure(bg="white")
    window.resizable(False,False)

    def signup():
        username= user.get()
        password=passw.get()
        cpassword=cpassw.get()

        if password==cpassword:
            users.append({"id": str(len(users)+1), "username": username, "password": password})
            saveUsers(users)
            messagebox.showinfo("Success","New user signed up successfully!")

        else:
            messagebox.showerror("Error","Passwords do not match")

    def sign():
        window.destroy()
        
    frame = Frame(window,width=700,height=700,bg="white")
    frame.place(x=80,y=70)

    heading = Label(frame,text='SIGN UP PAGE',fg='#57a1f8',bg='white',\
                font=('Microsoft YaHei UI Light',23,'bold' ))
    heading.place(x=70,y=45)

    #username
    def on_enter(e):
        user.delete(0,'end')
    
    def on_leave(e):
        name=user.get()
        if name=='':
             user.insert(0,'Username')
         
    user = Entry(frame,width=25,fg="black",bg="white",\
             font=('Microsoft YaHei UI Light',11))
    user.place(x=30,y=120)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=145)

    #password
    def on_enter(e):
        passw.delete(0,'end')

    def on_leave(e):
        name=passw.get()
        if name=='':
             passw.insert(0,'Password')
         
    passw = Entry(frame,width=25,fg="black",bg="white",\
             font=('Microsoft YaHei UI Light',11))
    passw.place(x=30,y=210)
    passw.insert(0,'Password')
    passw.bind('<FocusIn>',on_enter)
    passw.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=235)

    #confirm password
    def on_enter(e):
        cpassw.delete(0,'end')

    def on_leave(e):
        name=cpassw.get()
        if name=='':
             cpassw.insert(0,'Confirm Password')
         
    cpassw = Entry(frame,width=25,fg="black",bg="white",\
                   font=('Microsoft YaHei UI Light',11))
    cpassw.place(x=30,y=300)
    cpassw.insert(0,'Confirm Password')
    cpassw.bind('<FocusIn>',on_enter)
    cpassw.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=325)

    #button
    sign_up= Button(frame,width=20,pady=5,text='Sign up',bg='#57a1f8',fg='black',\
                    border=0,command=signup)
    sign_up.place(x=85,y=360)

    #sign in
    label= Label(frame,text="Already have an account?",fg='black',bg='white',\
                 font=('Microsoft YaHei UI Light',11))
    label.place(x=55,y=405)

    sign_up=Button(frame,width=6,text='Sign in',border=0,bg='white',\
                   cursor='hand2',fg='#57a1f8',command=sign)
    sign_up.place(x=240,y=405)


    window.mainloop()
    

#logo
img = PhotoImage(file="cat logo.png")
Label(show,image=img,bg='white').place(x=50,y=50)

#login frame
frame = Frame(show,width=700,height=700,bg="white")
frame.place(x=560,y=90)

#title
heading = Label(frame,text='LOG IN PAGE',fg='grey',bg='white',\
                font=('Microsoft YaHei UI Light',23,'bold' ))
heading.place(x=75,y=45)

         
#username
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
         user.insert(0,'Username')
         
user = Entry(frame,width=25,fg="black",bg="white",\
             font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=120)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=145) 

#password
def on_enter(e):
    passw.delete(0,'end')

def on_leave(e):
    name=passw.get()
    if name=='':
         passw.insert(0,'Password')
         
passw = Entry(frame,width=25,fg="black",bg="white",\
             font=('Microsoft YaHei UI Light',11))
passw.place(x=30,y=210)
passw.insert(0,'Password')
passw.bind('<FocusIn>',on_enter)
passw.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=235)


#sign in
sign_in= Button(frame,width=30,pady=5,text='Sign in',bg='#57a1f8',fg='black',\
       border=0,command=signin)
sign_in.place(x=65,y=270)

#sign up
label= Label(frame,text="Don't have an account?",fg='black',bg='white',\
             font=('Microsoft YaHei UI Light',11))
label.place(x=75,y=315)

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',\
               cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=245,y=320)


show.mainloop()
