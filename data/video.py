import cv2
from queue import Queue
import numpy

class Video:
    def __init__(self, queue, send_video):
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
        self.run()

    def run(self):
        print('video thread started...')
        while True:
            val = self.queue.get()
            if type(val) == numpy.ndarray:
                pass
            elif val is None:   # If you send `None`, the thread will exit.
                return
            elif val == "play":
                print(val)
                self.play_video()
            elif val == 'pause':
                pass
            elif type(val) != numpy.ndarray:#Try to see if the value is a file path
                self.filepath = val
                print(val)
                self.open_video()

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
        ret, frame = self.cap.read(self.frame_number)
        if ret == True:
            self.queue.put(frame)
