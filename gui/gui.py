from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from functools import partial


class WingMan:
    def __init__(self):
        self.loginStatus=False
        self.email=''
        self.password=''

    def login(self):
        login_screen = Tk()
        login_screen.title("Login")
        login_screen.geometry("300x250")

        Label(login_screen, text="Please enter login details").pack()
        Label(login_screen, text="").pack()
        Label(login_screen, text="Email").pack()

        # email label and text entry box
        email_login_entry = Entry(login_screen, textvariable="email")
        email_login_entry.pack()

        Label(login_screen, text="").pack()
        Label(login_screen, text="Password").pack()

        # password label and password entry box
        password_login_entry = Entry(
            login_screen, textvariable="password", show='*')
        password_login_entry.pack()
        
        Label(login_screen, text="").pack()

        #handle button click
        def handleLogin(e):
            self.email=email_login_entry.get()
            self.password=password_login_entry.get()
            self.loginStatus=True
            login_screen.destroy()
            self.wingman.destroy()
            self.returnDetails()

        Button(login_screen, text="Login",
               command=handleLogin, width=20, height=1).pack()
        login_screen.bind('<Return>',handleLogin)
        login_screen.bind('<Return>',handleLogin)

        login_screen.mainloop()

    def start_without_login(self):
        self.wingman.destroy()

    def homescreen(self):
        self.wingman = Tk()
        self.wingman.title("WingMan")
        self.wingman.geometry('700x500')

        teams = ImageTk.PhotoImage(Image.open(
        "./Logo/teams.png"), width="225", height="225")
        tms = Button(self.wingman, image=teams)
        tms.pack(side="left", fill="none", expand="no")
        
        with_login = Button(self.wingman, text="Join Meeting with Login info",command = self.login)
        with_login.pack(side = "left", fill = "none", expand = "no")

        without_login = Button(self.wingman, text="Join Meeting without Login info",command=self.start_without_login)
        without_login.pack(side = "left", fill = "none", expand = "no")

        self.wingman.mainloop()
    
    def returnDetails(self):
        return [self.loginStatus,self.email,self.password]

obj=WingMan()
obj.homescreen()
user_details=obj.returnDetails()
print(user_details)