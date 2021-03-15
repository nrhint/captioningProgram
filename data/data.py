##Nathan Hinton
##This is the structure that will hold the text and timestmps

class Line:
    def __init__(self, text = None, startTime = None, endTime = None):
        self.text = text
        self.startTime = startTime
        self.endTime = endTime