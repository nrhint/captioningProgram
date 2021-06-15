import cv2
# from queue import Queue
from time import time, sleep

class Video:
    def __init__(self, queue, send_video, sending_video_flag, ready_for_next_frame, generate, fps_ready, fps_queue):
        print('loading video class...')
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
        self.ready_for_next_frame = ready_for_next_frame
        self.generate = generate
        self.fps_ready_flag = fps_ready
        self.fps_queue = fps_queue
        self.state = 'idle'
        self.run()

    def run(self):
        print('video thread started!')
        while True:
            if not self.queue.empty() and self.generate.is_set():
                val = self.queue.get()
                if val == 'pause':
                    self.state = 'pause'
                    self.frame_number -= 2
                    self.sending_video.clear()
                    self.ready_for_next_frame.clear()
                    self.sending_video.clear()

                elif val == "play":
                    self.state = 'play'
                    self.sending_video.set()
                    self.ready_for_next_frame.set()
                else:#Try to see if the value is a file path
                    print(val)
                    if val[0] != '':
                        self.filepath = val[0]
                        self.width = val[1]
                        self.height = val[2]
                        print('trying to open video at path %s'%val[0])
                        self.open_video()
                    else:
                        pass
            if self.sending_video.is_set() == True:
                if self.send_video.qsize() < 2:
                    self.play_video()
                else:
                    #print('queue maxed out...')
                    self.ready_for_next_frame.wait()
            if self.generate.is_set():
                print('added fps in video queue')
                self.fps_queue.put((self.fps))
                self.state = 'pause'
                self.fps_ready_flag.set()


    def print(self):
        print('-- Video Detail --')
        print('\tFPS:\t%.3f'%(self.fps))
        print('\tFrames:\t%s'%(self.frame_count))
        print('\tDuration (s):\t%.3f'%(self.duration))
        print('\tDuration (m:s):\t%s : %.3f'%(int(self.duration/60),self.duration%60))
        print('\tframe (W:H):\t%s : %s'%(self.width,self.height))

    def findDetail(self):
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.fpsInSeconds = 1/self.fps
        self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.duration = self.frame_count / self.fps
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def open_video(self):
        try:
            self.cap = cv2.VideoCapture(self.filepath)
            self.frame_number = 0
            self.findDetail()
            self.print
        except FileNotFoundError:
            print('Unable to open file...')
    
    def next_frame(self):
        pass

    def play_video(self):
        timeForNextFrame = (time()+self.fpsInSeconds)
        if self.fps == None:
            self.findDetail()
        ret, frame = self.cap.read(self.frame_number)
        if ret == True:
            #frame = cv2.resize(frame, (self.width, self.height))
            self.send_video.put((timeForNextFrame, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), self.frame_number))
            self.frame_number += 1
            self.ready_for_next_frame.clear()