from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter.filedialog import askopenfile

wingman = Tk()
wingman.title("WingMan")
wingman.geometry('1000x500') 
'''
backgorund_image = PhotoImage(file = "./Logo/bg.png")
background_label = Label(wingman, image=background_image)
background_label.place(relwidth=1, relheight=1)
'''
def open_file(): 
    tt = askopenfile(mode ='r', filetypes =[('PDF', '*.pdf')]) 
    if tt is not None: 
        print("Hello")


teams = ImageTk.PhotoImage(Image.open("./Logo/teams.png"),width="225",height="225")
tms = Button(wingman, image = teams)
tms.pack(side = "left", fill = "none", expand = "no")

zoom = ImageTk.PhotoImage(Image.open("./Logo/zoom.png"),width="225",height="225")
zm = Button(wingman, image = zoom)
zm.pack(side = "left", fill = "none", expand = "no")


upload=Button(wingman,text="Upload your \n time table",command = lambda:open_file())
upload.pack(side = "left", fill = "none", expand = "no")

'''
teams = PhotoImage(file =r".\Logo\teams.png") 
mic_teams=Button(wingman,image=teams)
'''

wingman.mainloop()