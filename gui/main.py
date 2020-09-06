from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from functools import partial

wingman = Tk()
wingman.title("WingMan")
wingman.geometry('700x500')  

teams = ImageTk.PhotoImage(Image.open("./Logo/teams.png"),width="225",height="225")
tms = Button(wingman, image = teams,command = lambda:LoginPage())
tms.pack(side = "left", fill = "none", expand = "no")

#zoom = ImageTk.PhotoImage(Image.open("./Logo/zoom.png"),width="225",height="225")
zm1 = Button(wingman, text="Join Meeting with Login info",command = lambda:LoginPage())
zm1.pack(side = "left", fill = "none", expand = "no")

zm1 = Button(wingman, text="Join Meeting without Login info")
zm1.pack(side = "left", fill = "none", expand = "no")


def LoginPage():
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.geometry("300x500")
     
    Label(login_screen, text="Please enter login details").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username").pack()
    
    #username label and text entry box
    username_login_entry = Entry(login_screen, textvariable="username")
    username_login_entry.pack()

    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack()
    
    #password label and password entry box
    password__login_entry = Entry(login_screen, textvariable="password", show= '*')
    password__login_entry.pack()
    
    Label(login_screen, text="").pack()
    #Button(login_screen,text="Upload your time table",command=lambda:open_file(), width=20, height=1).pack()

    print(type(username_login_entry))
    def butn():
           ussr=username_login_entry.get()
           pas=password__login_entry.get()  
           typ=type(username_login_entry)
           return ussr,pas,typ
    
    
    #login button
    Button(login_screen, text="Login",command=butn, width=10, height=1).pack()
    login_screen.mainloop()
wingman.mainloop()