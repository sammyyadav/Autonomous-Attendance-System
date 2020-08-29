import tkinter as tk
from tkinter import *
import tkinter.font as font
import sys
sys.path.append('~/.local/lib/python3.5/site-packages')
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import PIL
from PIL import Image, ImageTk


global crew
crew=[]
DATADIR = '/home/sammy-ros/attendance_facial/attendace_data'
CATEGORY = []
for L in os.listdir(DATADIR): 
    CATEGORY.append(L)
#print(CATEGORY)

def open_img(crew):

	if crew == []: return 0
	img_array = Image.open(os.path.join(crew[0]) )
	global img_array							
	photo = ImageTk.PhotoImage(img_array)
	print(photo)
	global panel
	panel =Label(frame_2, text = 'Click Me !' ,image = photo)
	panel.image = photo
	panel.grid(row = 4, column = 0)
	

def save_file():
	fp=  '/home/sammy-ros/attendance_facial/datasets/' + entry_2.get() 
	print(fp)
	import random
	if not os.path.exists(fp):
	            os.makedirs(fp)
	fn = fp +'/' + entry_1.get() + str(random.randint(0,999))+".jpg"
	img_array.save(fn)

def next_file():
	panel.grid_forget()
	if len(crew)!=0:
		crew.pop(0)
	
	open_img(crew)
	



top = Tk()

top.title("Unknown Faces Management")

frame  =Frame(master = top, width = 1000)
frame.grid(row=0,column = 0)
frame.rowconfigure(0, weight = 1, minsize = 50)
for x in range(2):frame.columnconfigure(x ,weight = 1 , minsize = 450)


label = tk.Label(master = frame, text = "Select a Date", bg = "lightblue", fg = 'red')
label['font'] = font.Font(family = "Times",size = 20)
label.grid(row = 0, column = 0, sticky = "news")

tkvar = StringVar(top)
tkvar.set("Choose a Date")

popup = OptionMenu(frame , tkvar, *CATEGORY)
popup['font'] = font.Font(family = "Times",size = 20)
popup.grid(row = 0, column =1,sticky = "snew")


global date,unk_fol_path
date,unk_fol_path='',''


def change_drop(*args):
	date = tkvar.get()
	print(date)
	unk_fol_path = '/home/sammy-ros/attendance_facial/attendace_data/'+date+"/unknown_faces/" 
	for img in tqdm(os.listdir(unk_fol_path)):crew.append(unk_fol_path+img)
	open_img(crew)


tkvar.trace("w",change_drop)



frame_2 = tk.Frame(top,width  = 1900, height = 100 , bg = "lightblue")
frame_2.grid(row=1,column = 0)

frame_2.columnconfigure(0 ,weight = 1 , minsize = 900)
for x in range(4):
	frame_2.rowconfigure(x,weight = 1 , minsize = 50)

label_1 = tk.Label(master = frame_2, text = "Enter the Name:", bg = "lightblue", fg = 'red')
label_1['font'] = font.Font(size = 15)
label_1.grid(row = 0, column = 0,sticky = "ws", padx = 50)


label_2 = tk.Label(master = frame_2, text = "Enter the Roll Number:", bg = "lightblue", fg = 'red')
label_2['font'] = font.Font(size = 15)
label_2.grid(row = 2, column = 0 ,sticky = "ws", padx = 50)



entry_1 = tk.Entry(master = frame_2 )
entry_1['font'] = font.Font(size = 15)
entry_1.grid(row = 1, column = 0,sticky = "news",padx = 50)


entry_2 = tk.Entry(master = frame_2 )
entry_2['font'] = font.Font(size = 15)
entry_2.grid(row = 3, column = 0,sticky = "news",padx = 50)




frame_4 = tk.Frame(top,width  = 900, height = 100 , bg = "lightblue")
frame_4.grid(row=2,column = 0)
for x in range(3):
	frame_4.columnconfigure(x,weight = 1 , minsize = 300)
frame_4.rowconfigure(0,weight = 1 , minsize = 100)

A = tk.Button(master = frame_4, text = 'Save',cursor = "fleur",bg = "lightblue" , fg = "blue" ,command =  save_file)
B = tk.Button(master = frame_4, text = 'Ignore',cursor = "fleur",bg = "lightblue" , fg = "blue",command =  next_file )

A['font'] = font.Font(size = 18)
B['font'] = font.Font(size = 18)

A.grid(row=  0,column = 0, sticky = "nsew", padx = 15, pady = 15)
B.grid(row=  0,column = 1, sticky = "nsew", padx = 15, pady = 15)


C= tk.Button(master = frame_4, text = 'Exit',cursor = "fleur",bg = "lightblue" , fg = "blue",command =  sys.exit )
C['font'] = font.Font(size = 18)
C.grid(row=  0,column = 2, sticky = "nsew", padx = 15, pady = 18)



top.mainloop()

