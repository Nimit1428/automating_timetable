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
        

    teams = ImageTk.PhotoImage(Image.open("./Logo/teams.png"),width="225",height="225")
    tms = Button(wingman, image = teams,command = lambda:LoginPage())
    tms.pack(side = "left", fill = "none", expand = "no")

    zoom = ImageTk.PhotoImage(Image.open("./Logo/zoom.png"),width="225",height="225")
    zm = Button(wingman, image = zoom)
    zm.pack(side = "left", fill = "none", expand = "no")

    stng = ImageTk.PhotoImage(Image.open("./Logo/settings.png"))
    sg = Button(wingman, image = stng,width="50",height="50",command = lambda:Settings())
    sg.pack(side = "right", fill = "none", expand = "no")

    '''upload=Button(wingman,text="Upload your \n time table",command = lambda:open_file())
    upload.pack(side = "left", fill = "none", expand = "no")'''

    '''
    teams = PhotoImage(file =r".\Logo\teams.png") 
    mic_teams=Button(wingman,image=teams)
    '''
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
        '''
        def butn():
            print(username_login_entry.get())
            print(password__login_entry.get())   
            print(type(username_login_entry))'''
        #login button

        Button(login_screen, text="Login",command=login_screen.destroy, width=10, height=1).pack()
        

        
        '''def open_file(): 
            tt = askopenfile(mode ='r', filetypes =[('PDF', '*.pdf')])  
            if tt is not None: 
                print("Hello")
        '''

        

        login_screen.mainloop()
        

    def Settings():
        print("hello")
        login_screen = Tk()


    '''
    class App():
        def __init__(self):
            login = Tk()
            login.geometry('500x500') 
            
            
            usernameLabel = Label(login, text="User Name").grid(row=0, column=0)
            username = StringVar()
            usernameEntry = Entry(login, textvariable=username).grid(row=0, column=1)  
            
            
            passwordLabel = Label(login,text="Password").grid(row=1, column=0)  
            password = StringVar()
            passwordEntry = Entry(login, textvariable=password, show='*').grid(row=1, column=1)  
            

            
            #loginButton = Button(login, text="Login", command=self.validateLogin).grid(row=4, column=0)  


            button_showinfo = Button(login, text="Login", command=self.validate_Login)
            button_showinfo.pack(fill='none')

            upload = Button(login,text="Upload your time table",command=self.open_file)
            upload.pack( fill = "x")
            
            button_close = Button(login, text="Close", command=login.destroy)
            button_close.pack(fill='x')
            
            validate_Login = partial(validate_Login, username, password)
            login.mainloop()

        def popup_window(self):
            window = Toplevel()

            label = Label(window, text="Hello World!")
            label.pack(fill='x', padx=50, pady=5)

            button_close = Button(window, text="Close", command=window.destroy)
            button_close.pack(fill='x')

        def popup_showinfo(self):
            showinfo("ShowInfo", "Hello World!")
        
        def open_file(self): 
            tt = askopenfile(mode ='r', filetypes =[('PDF', '*.pdf')]) 
            if tt is not None: 
                print("Hello")
                
        def validate_Login(username, password):
            print("username entered :", username.get())
            print("password entered :", password.get())'''
            
    wingman.mainloop()

WingMan()