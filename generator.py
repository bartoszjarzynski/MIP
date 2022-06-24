# Importing libraries
from hashlib import new
from tkinter import *
from tkinter import filedialog as fd
from pydicom import *
import glob
from PIL import Image, ImageTk
import os
import numpy as np
import SimpleITK as sitk
import fredtools as ft

# Object class
class Picture:
    # Initializing object
    def __init__(s):
        s.pix = []
        s.zdj = ImageTk
        s.canvas = Canvas(root)
        s.click = 1
        s.matrix = []

    # Rotate an image
    def rotate(s, pix):
        s.canvas.destroy()
        if len(pix) > 0:
            s.pix = np.rot90(pix, 1, (1,0))
            s.pix = np.rot90(s.pix, s.click, (2,0))
            width_ = 1024
            height_ = 512
            s.canvas = Canvas(root, width=width_, height=height_)
            s.canvas.pack(side='right')
            s.draw()

    # Drawing an image
    def draw(s):
        s.canvas.delete('all')
        s.zdj = ImageTk.PhotoImage(image=Image.fromarray(s.pix[100]))
        s.canvas.create_image(0, 0, anchor="nw", image=s.zdj)

    # Reading a path with image
    def load(s, path):
        pix = []
        if os.path.isdir(path):
            for file in glob.glob(path + '/*.dcm'):
                ds = dcmread(file)
                pix.append(ds.pixel_array)
        return pix

    # Rotating by 1
    def roll(s):
        s.click += 1
        
    def get_highest_value(s):
        #s.pic[511][199][511] - last picture and pixel   
        s.matrix = s.pix[0]
        
        for i in range(0, 511):
            for j in range(0, len(s.pix[i])):
                for k in range(0, len(s.pix[i][j])):

                    if s.pix[i][j][k] > s.matrix[j][k]:
                        s.matrix[j][k] = s.pix[i][j][k]
        print(s.matrix)    


root = Tk()
# The view of the window
root.state('normal')
root.title('MIP')

pole = Picture()

menu = Frame(root)
menu.pack(side='top', padx=30, pady=30)

title = Label(menu, text='MIP', font=('Arial', 25))
title.pack()

# Button for opening a file
button1= Button(menu, text='Choose a directory', command=lambda: pole.rotate(pole.load(fd.askdirectory())))
button1.pack()
# Button for rotating by 1
button2 = Button(menu, text='Rotate', command=lambda: pole.roll())
button2.pack()
# Button for highest value
button3 = Button(menu, text='Max value', command=lambda: pole.get_highest_value())
button3.pack()

button4 = Button(menu, text='Exit', command=lambda: exit())
button4.pack()

# TO DO: displaying new, the  brightest image button

# Looping the window
root.mainloop()