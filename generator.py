# Importing libraries
from hashlib import new
from tkinter import *
from tkinter import filedialog as fd
from pydicom import *
import glob
from PIL import Image, ImageTk
import os
import numpy as np
import pandas as pd

# Object class
class obraz:
    # Initializing object
    def __init__(s):
        s.pix = []
        s.zdj = ImageTk
        s.canvas = Canvas(root)
        s.click = 1

    # Rotate an image
    def fun(s, pix):
        s.canvas.destroy()
        if len(pix) > 0:
            s.pix = np.rot90(pix, 1, (1,0))
            s.pix = np.rot90(s.pix, s.click, (2,0))
            szerokosc = 1024
            wysokosc = 512
            s.canvas = Canvas(root, width=szerokosc, height=wysokosc)
            s.canvas.pack(side='right')
            s.rys()
            #print(s.pix)           ### PRINT ALL THE PIXELS VALUES
            #print(s.pix[0][0])     ### PRINT FIRST PIXEL VALUE

    # Drawing an image
    def rys(s):
        s.canvas.delete('all')
        s.zdj = ImageTk.PhotoImage(image=Image.fromarray(s.pix[1]))
        s.canvas.create_image(0, 0, anchor="nw", image=s.zdj)

    # Reading a path with image
    def wczytaj(s, path):
        pix = []
        if os.path.isdir(path):
            for file in glob.glob(path + '/*.dcm'):
                ds = dcmread(file)
                pix.append(ds.pixel_array)
        return pix

    # Rotating by 1
    def obrot(s):
        s.click += 1
        
    def get_highest_value(s):
        #s.pix[picture_number]
        #s.pix[0][0] - first picture
        #s.pic[0][0][0] - first pixel
        
        for i in range (0, len(s.pix)-1):
            for j in range (0, len(s.pix[i])):
                for k in range (0, len(s.pix[i][j])):
                    
                    if s.pix[i+1][j][k] > s.pix[i][j][k]:
                        s.pix[i][j][k] = s.pix[i+1][j][k]
            
        print(s.pix[0][0])
        
    # Getting the highest value in an array
    # def get_highest_value(s):
        
    #     all_arrays = np.array_split(s.pix, 512)
    #     new_image_arr = []
        
    #     for i in range(len(all_arrays)):
    #         try:
    #             highestarrays = np.max(all_arrays[i])
    #             # highestarrays = int(highestarrays)
    #         except ValueError: # empty sequence
    #             pass

    #     new_image_arr.append(highestarrays)
    #     print(new_image_arr)

root = Tk()
root.state('zoomed')
root.title('MIP')

pole = obraz()

menu = Frame(root)
menu.pack(side='left', padx=20, pady=20)

title = Label(menu, text='MIP', font=('Arial', 20))
title.pack()

# Button for opening a file
button1 = Button(menu, text='Choose a directory', command=lambda: pole.fun(pole.wczytaj(fd.askdirectory())))
button1.pack()
# Button for rotating by 1
button2 = Button(menu, text='Rotate', command=lambda: pole.obrot())
button2.pack()
# Button for highest value
button3 = Button(menu, text='Max value', command=lambda: pole.get_highest_value())
button3.pack()

button4 = Button(menu, text='Display new image *TO DO*', command=lambda: pole.fun(pole.wczytaj(fd.askdirectory())))
button4.pack()

# Looping the window
root.mainloop()