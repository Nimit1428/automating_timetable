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
        login_screen.maxsize(300,250)
        login_screen.minsize(300,250)

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

        Button(login_screen, text="Login",command=lambda:handleLogin(self), width=20, height=1).pack()
        login_screen.bind('<Return>',handleLogin)

        login_screen.mainloop()

    def start_without_login(self):
        self.wingman.destroy()

    def homescreen(self):
        self.wingman = Tk()
        self.wingman.iconbitmap('./exe/gui.ico')
        self.wingman.title("WingMan")
        self.wingman.geometry('400x449')
        self.wingman.maxsize(400,449)
        self.wingman.minsize(400,449)
        
        bgg_image =ImageTk.PhotoImage(file='./logo/bg3.jpg')
        bgg_label=Label(self.wingman,image=bgg_image)
        bgg_label.place(x=0,y=0,relwidth=1,relheight=1)
        
        #self.wingman.configure(background='./Logo/bg.png')
        #self.wingman.configure(background = image1)
        
        teams = ImageTk.PhotoImage(Image.open("./Logo/teams2.jpg"),)
        tms = Button(self.wingman, image=teams, width="225", height="225",border=3)
        tms.pack(pady=10)
        
        with_login = Button(self.wingman,command = self.login,text="Join Meeting with Login Info",font=("Helvetica", 10, "bold italic"),border=0,width="30", height="3",activeforeground = "#ffffff",activebackground = "#202020", bg='#1c2e4a', fg='#ffffff')
        with_login.pack(pady=10)
        
        without_login = Button(self.wingman,text="Join meeting without Login info",font=("Helvetica", 10, "bold italic"),border=0,command=self.start_without_login,width="30", height="3",activeforeground = "#ffffff",activebackground = "#202020",bg='#1c2e4a', fg='#ffffff')
        without_login.pack(pady=10)
        


        self.wingman.mainloop()
    
    def returnDetails(self):
        return [self.loginStatus,self.email,self.password]

obj=WingMan()
obj.homescreen()
user_details=obj.returnDetails()
print(user_details)