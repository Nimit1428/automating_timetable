from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from functools import partial


def WingMan():

    wingman = Tk()
    wingman.title("WingMan")
    wingman.geometry('700x500')
    '''
    backgorund_image = PhotoImage(file = "./Logo/bg.png")
    background_label = Label(wingman, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    '''

    teams = ImageTk.PhotoImage(Image.open(
        "./Logo/teams.png"), width="225", height="225")
    tms = Button(wingman, image=teams, command=lambda: LoginPage())
    tms.pack(side="left", fill="none", expand="no")

    zoom = ImageTk.PhotoImage(Image.open(
        "./Logo/zoom.png"), width="225", height="225")
    zm = Button(wingman, image=zoom)
    zm.pack(side="left", fill="none", expand="no")

    '''upload=Button(wingman,text="Upload your \n time table",command = lambda:open_file())
    upload.pack(side = "left", fill = "none", expand = "no")'''

    '''
    teams = PhotoImage(file =r".\Logo\teams.png") 
    mic_teams=Button(wingman,image=teams)
    '''

    def LoginPage():

        login_screen = Tk()
        login_screen.title("Login")
        login_screen.geometry("300x250")

        Label(login_screen, text="Please enter login details").pack()
        Label(login_screen, text="").pack()
        Label(login_screen, text="Username").pack()

        # username label and text entry box
        username_login_entry = Entry(login_screen, textvariable="username")
        username_login_entry.pack()

        Label(login_screen, text="").pack()
        Label(login_screen, text="Password").pack()

        # password label and password entry box
        password__login_entry = Entry(
            login_screen, textvariable="password", show='*')
        password__login_entry.pack()

        Label(login_screen, text="").pack()
        Button(login_screen, text="Upload your time table",
               command=lambda: open_file(), width=20, height=1).pack()

        def butn():
            print(username_login_entry.get())
            print(password__login_entry.get())
            print(type(username_login_entry))
            return [username_login_entry.get(), password__login_entry.get()]

        li = butn()
        username = li[0]
        password = li[1]
        # login button
        Button(login_screen, text="Login",
               command=butn, width=10, height=1).pack()

        def open_file():
            tt = askopenfile(mode='r', filetypes=[('PDF', '*.pdf')])
            if tt is not None:
                print("Hello")

        login_screen.mainloop()
    wingman.mainloop()
    loginStatus = 0
    return [loginStatus, username, password]


print(WingMan())
