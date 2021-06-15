##Nathan Hinton
##This will controll all of the menus for doing things

##Nathan Hinton. This program takes code from the pynput project found at: https://github.com/moses-palmer/pynput

##Making a GUI for all of this
v = True
if v:print('Starting...')

import tkinter as tk
from tkinter import filedialog
import threading
from data import video, captions
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
ready_for_frame = threading.Event()
threads = []
if v:print("starting video thread")
video_queue = Queue()
video_frame_queue = Queue()
video_thread = threading.Thread(target = video.Video, args=(video_queue, video_frame_queue, sending_video, ready_for_frame))
video_thread.start()
if v:print('starting caption thread...')
caption_queue = Queue()
start_line_flag = threading.Event()
end_line_flag = threading.Event()
new_text_flag = threading.Event()
caption_thread = threading.Thread(target = captions.captions, args=(caption_queue, start_line_flag, end_line_flag, new_text_flag))
caption_thread.start()

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

def select_text_file():
    filetypes = (('text file', '*.txt'), ('All files', '*.*'))
    filename = filedialog.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    caption_queue.put(filename)
    new_text_flag.set()
    pressToTrack.configure(text='press to key caption')

def endLine(garbage):
    end_line_flag.set()
    # pressToTrack.configure(text='press to key caption')
def startLine():
    start_line_flag.set()
    # pressToTrack.configure(text='press to key out caption')

options_frame = tk.Frame(master = window)
video_frame = tk.Frame(master = window)
captions_frame = tk.Frame(master = window)
captions_edit_frame = tk.Frame(master = window)

optionText = tk.Label(options_frame, text = 'Video options:', borderwidth=5)
openFile = tk.Button(options_frame, text = 'Open video file', command=select_video_file)
play = tk.Button(options_frame, text = 'Play', command=lambda: video_queue.put('play'))
pause = tk.Button(options_frame, text = 'Pause', command=lambda: video_queue.put('pause'))

display_image = tk.Label(video_frame, image = image)

captionsText = tk.Label(captions_frame, text = 'Captions editor', borderwidth=5)
currentLine = tk.Label(captions_frame, text = 'No file loaded', )

captionsEditText = tk.Label(captions_edit_frame, text = 'Captions options', borderwidth=5)
openCaptions = tk.Button(captions_edit_frame, text = 'open caption file', command=select_text_file)
pressToTrack = tk.Button(captions_edit_frame, text = 'No file loaded...', command=startLine)
pressToTrack.bind("<ButtonRelease>", endLine)

optionText.pack()
openFile.pack()
play.pack()
pause.pack()

display_image.pack()

#For some reason this needs to be backwards.
captionsEditText.pack()
openCaptions.pack()
pressToTrack.pack()

captionsText.pack()
currentLine.pack()

options_frame.grid(column=0, row=0, sticky='n', columnspan=2, rowspan=3)
captions_edit_frame.grid(column=0, row=3, sticky='n', columnspan=2, rowspan=3)
video_frame.grid(column=2, row=0, sticky='n', columnspan=6, rowspan=4)
captions_frame.grid(column=2, row=4, sticky='n', columnspan=6, rowspan=2)

def updateVideoPanel():
    video_update_rate = 1000
    if sending_video.is_set():
        ready_for_frame.set()
        if not video_frame_queue.empty():
            val = video_frame_queue.get()
            image = Image.fromarray(val[1])
            image = ImageTk.PhotoImage(image)
            display_image.configure(image = image)
            display_image.image = image
            # if int((time()-val[0])*100) < 10:
            #     # print('low frame rate... %s ms behind'%int((1000/val[0])+((val[2]-time())*1000)))
            #     window.update_idletasks()
            #     window.update()
            #     video_update_rate = 0
            # else:
            video_update_rate = int((time()-val[0])*100)
            if v:print("Updated screen with %s ms extra time"%video_update_rate)
    # else:
    #     print('nothing to update...')
    window.after(video_update_rate, updateVideoPanel)

def updateText():
    if new_text_flag.is_set():
        currentLine.configure(text=caption_queue.get())
        new_text_flag.clear()
    window.after(100, updateText)


window.after(video_update_rate, updateVideoPanel)
window.after(1000, updateText)
window.mainloop()
