##Nathan Hinton
##This will be a thread where all of the captions will be placed

from data.data import Line
from time import time

class captions:
    def __init__(self, caption_queue, start_line_flag, end_line_flag, new_text_flag):
        print('loading capton class...')
        self.caption_queue = caption_queue
        self.start_line_flag = start_line_flag
        self.end_line_flag = end_line_flag
        self.new_text_flag = new_text_flag
        self.run()

    def run(self):
        print('captions thread started!')
        self.state = 'waiting for file name'
        while True:
            if self.state == 'waiting for file name':
                self.new_text_flag.wait()
                self.filename = self.caption_queue.get()
                self.fileData = open(self.filename, 'r').read()
                lines = self.fileData.split('\n')
                self.data = []
                for line in lines:
                    self.data.append(Line(text = line))
                self.index = 0
                self.state = 'waiting for actions'
            elif self.state == 'waiting for actions':
                self.new_text_flag.set()
                self.caption_queue.put(self.data[self.index].text)
                self.start_line_flag.wait()
                self.data[self.index].startTime = time()
                self.end_line_flag.wait()
                self.data[self.index].endTime = time()
                self.index += 1
                self.start_line_flag.clear()
                self.end_line_flag.clear()
                if self.index == len(self.data):
                    self.state = 'finished'
            elif self.state == 'finished':
                self.caption_queue.put('FINISHED ALL OF THE TEXT IN THE FILE')
                self.new_text_flag.set()
                self.state = 'waiting'
            
