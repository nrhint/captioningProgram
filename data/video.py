import cv2
# from queue import Queue
import numpy
from time import time

class Video:
    def __init__(self, queue, send_video, sending_video_flag):
        print('starting video class...')
        self.queue = queue
        self.send_video = send_video
        self.cap = None
        self.fps = None
        self.frame_count = None
        self.duration = None
        self.width = None
        self.height = None
        self.frame_number = None
        self.filepath = None
        self.sending_video = sending_video_flag
        self.run()

    def run(self):
        print('video thread started...')
        while True:
            if not self.queue.empty():
                val = self.queue.get()
                if val is None:   # If you send `None`, the thread will exit.
                    return
                elif val == 'pause':
                    pass
                elif val == "play":
                    if not self.sending_video.is_set():
                        self.sending_video.set()
                    print(val)
                    self.play_video()
                elif type(val) != numpy.ndarray:#Try to see if the value is a file path
                    self.filepath = val
                    print(val)
                    self.open_video()
            if self.sending_video.is_set() == True:
                self.play_video()

    def print(self):
        print('-- Video Detail --')
        print('\tFPS:\t%.3f'%(self.fps))
        print('\tFrames:\t%s'%(self.frame_count))
        print('\tDuration (s):\t%.3f'%(self.duration))
        print('\tDuration (m:s):\t%s : %.3f'%(int(self.duration/60),self.duration%60))
        print('\tframe (W:H):\t%s : %s'%(self.width,self.height))

    def findDetail(self):
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.duration = self.frame_count / self.fps
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def open_video(self):
        try:
            self.cap = cv2.VideoCapture(self.filepath)
            self.frame_number = 0
        except FileNotFoundError:
            print('Unable to open file...')
    
    def next_frame(self):
        pass

    def play_video(self):
        if self.fps == None:
            self.findDetail()
        if self.send_video.empty():
            ret, frame = self.cap.read(self.frame_number)
            if ret == True:
                # print('sent frame number %s'%self.frame_number)
                # if self.frame_number != 0:
                #     self.send_video.put(frame)
                # else:
                self.send_video.put((self.fps, frame, time()))
                self.frame_number += 1