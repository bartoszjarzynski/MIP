# Importing libraries
from tkinter import *
from tkinter import filedialog as fd
from pydicom import *
import glob
from PIL import Image, ImageTk
import os
import numpy as np


class obraz:
    def __init__(s):
        s.pix = []
        s.zdj = ImageTk
        s.canvas = Canvas(root)
        s.click = 1

    def fun(s, pix):
        s.canvas.destroy()
        if len(pix) > 0:
            s.pix = np.rot90(pix, s.click, (1,0))
            s.pix = np.rot90(s.pix, s.click, (2,0))
            print(s.pix)
            szerokosc = 1024
            wysokosc = 512
            s.canvas = Canvas(root, width=szerokosc, height=wysokosc)
            s.canvas.pack(side='right')
            s.rys()

    def rys(s):
        s.canvas.delete('all')
        s.zdj = ImageTk.PhotoImage(image=Image.fromarray(s.pix[1]))
        s.canvas.create_image(0, 0, anchor="nw", image=s.zdj)

    def wczytaj(s, path):
        pix = []
        if os.path.isdir(path):
            for file in glob.glob(path + '/*.dcm'):
                ds = dcmread(file)
                pix.append(ds.pixel_array)
        return pix

    def obrot(s):
        s.click += 1
        
    def get_highest_value(s):
        all_arrays = np.array_split(s.pix, 512)
        for i in range(len(all_arrays)):
            try:
                print(np.max(all_arrays[i]))
            except ValueError: # empty sequence
                pass

root = Tk()
root.state('zoomed')
root.title('MIP')

pole = obraz()

menu = Frame(root)
menu.pack(side='left', padx=20, pady=20)

title = Label(menu, text='MIP', font=('Arial', 20))
title.pack()

button1 = Button(menu, text='Choose a directory', command=lambda: pole.fun(pole.wczytaj(fd.askdirectory())))
button1.pack()

button2 = Button(menu, text='Rotate', command=lambda: pole.obrot())
button2.pack()

button3 = Button(menu, text='Max value', command=lambda: pole.get_highest_value())
button3.pack()

root.mainloop()