##Nathan Hinton
##This will render a specific frame of the video along with the text that goes with it.

from data.video import Video
import cv2

class RenderFrame:
    def __init__(self, config, textData):
        self.config = config
        print("requires openVC")
        c = False
        while c == False:
            self.videoPath = input('video file path: ')
            self.captionPath = input('caption file path: ')
            try:
                open(self.videoPath, 'r')
                c = True
            except FileNotFoundError:
                print("File not found...")
        self.textData = textData
        self.frame = None
        self.video = Video()
        print(self.videoPath)
        self.video.cap = cv2.VideoCapture(self.videoPath)
        self.video.findDetail()
        self.video.print()

    def loadFrameFromNumber(self, frameNumber = False):
        if not frameNumber:
            self.frameNumber = int(input('Enter the frame number: '))
        else:
            self.frameNumber = frameNumber
        self.video.cap.set(1, self.frameNumber)
        ret, frame = self.video.cap.read()
        if ret:
            self.frame = frame
        else:
            print('ret returned false. This may be because the frame number was invalid...')
            return False
    def loadFrameFromCaption(self):
        from util.time_util import secondsToFrame
        self.captionNumber = int(input('Enter the line number you want to show: '))
        line = self.textData[self.captionNumber]
        frameNumber = secondsToFrame(line.startTime, self.video.fps)
        self.loadFrameFromNumber(frameNumber)
    def showFrame(self):
        
        scaleX = 0.4
        scaleY = 0.4
        # Reduce the image to 0.6 times the original
        scaleDown = cv2.resize(self.frame, None, fx= scaleX, fy= scaleY, interpolation= cv2.INTER_LINEAR)

        cv2.imshow('rendered image', scaleDown)
        cv2.waitKey(0)
        cv2.destroyAllWindows