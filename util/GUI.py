##Nathan Hinton
##This will controll all of the menus for doing things

##Nathan Hinton. This program takes code from the pynput project found at: https://github.com/moses-palmer/pynput

##Making a GUI for all of this
v = True
if v:print('loading...')

import tkinter as tk
from tkinter import filedialog
import threading
from data import video
from queue import Queue
from PIL import Image, ImageTk
import cv2
from time import time

if v:print('loading the window...')

#Start the window
window = tk.Tk()
window.geometry("800x600")
video_update_rate = 1000

if v:print("loading modules and starting threads...")
sending_video = threading.Event()
threads = []
if v:print("loading video thread")
video_queue = Queue()
video_frame_queue = Queue()
video_thread = threading.Thread(target = video.Video, args=(video_queue, video_frame_queue, sending_video))
video_thread.start()

window.grid_columnconfigure(0, minsize=100, weight = 1)
window.grid_columnconfigure(1, minsize=100, weight = 1)
window.grid_columnconfigure(2, minsize=100, weight = 1)
window.grid_columnconfigure(3, minsize=100, weight = 1)
window.grid_columnconfigure(4, minsize=100, weight = 1)
window.grid_columnconfigure(5, minsize=100, weight = 1)
window.grid_columnconfigure(6, minsize=100, weight = 1)
window.grid_columnconfigure(7, minsize=100, weight = 1)

window.grid_rowconfigure(0, minsize=100, weight = 1)
window.grid_rowconfigure(1, minsize=100, weight = 1)
window.grid_rowconfigure(2, minsize=100, weight = 1)
window.grid_rowconfigure(3, minsize=100, weight = 1)
window.grid_rowconfigure(4, minsize=100, weight = 1)
window.grid_rowconfigure(5, minsize=100, weight = 1)

blankload = cv2.imread('images/blank.png')
image = Image.fromarray(blankload)
image = ImageTk.PhotoImage(image)

def select_video_file():
    filetypes = (('All files', '*.*'), ('video files', '*.mp4'))
    filename = filedialog.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    video_queue.put(filename)

options_frame = tk.Frame(master = window)
video_frame = tk.Frame(master = window)
captions_frame = tk.Frame(master = window)
captions_edit_frame = tk.Frame(master = window)

optionText = tk.Label(options_frame, text = 'Options', borderwidth=5)
openFile = tk.Button(options_frame, text = 'Open video file', command=select_video_file)
play = tk.Button(options_frame, text = 'Play', command=lambda: video_queue.put('play'))

display_image = tk.Label(video_frame, image = image)

captionsText = tk.Label(captions_frame, text = 'Captions', borderwidth=5)

captionsEditText = tk.Label(captions_edit_frame, text = 'Captions editor', borderwidth=5)


optionText.pack()
openFile.pack()
play.pack()
display_image.pack()
captionsText.pack()
captionsEditText.pack()

options_frame.grid(column=0, row=0, sticky='n', columnspan=2, rowspan=3)
captions_edit_frame.grid(column=0, row=3, sticky='n', columnspan=2, rowspan=3)
video_frame.grid(column=2, row=0, sticky='n', columnspan=6, rowspan=4)
captions_frame.grid(column=2, row=4, sticky='n', columnspan=6, rowspan=2)

def updateVideoPanel():
##    if low_frame_rate:
##        print('low frame rate...')
    video_update_rate = 1000
    if sending_video.is_set():
        if not video_frame_queue.empty():
            val = video_frame_queue.get()
            # if len(val) == 2: #If there is another value in adition to the image which would be the FPS
            image = Image.fromarray(val[1])
            image = ImageTk.PhotoImage(image)
            display_image.configure(image = image)
            display_image.image = image
            if int((1000/val[0])+((val[2]-time())*1000)) < 10:
                low_frame_rate = True
                video_update_rate = 20
            else:
                low_frame_rate = False
                video_update_rate = int((1000/val[0])+((val[2]-time())*1000))
            # print("Updated screen")
    # else:
    #     print('nothing to update...')
    window.after(video_update_rate, updateVideoPanel)

window.after(video_update_rate, updateVideoPanel)
window.mainloop()
