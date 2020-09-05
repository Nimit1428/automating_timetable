
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter.filedialog import askopenfile
from functools import partial

wingman = Tk()

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        teams = ImageTk.PhotoImage(Image.open("./Logo/teams.png"),width="225",height="225")
        tk.Button(self, image=teams ,command=lambda: master.switch_frame(PageOne)).pack()
        


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()
wingman = SampleApp()
wingman.mainloop()