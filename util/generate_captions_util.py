from os import error
from util.time_util import convert_time

class GenerateCaptions:
    def __init__(self, data, config):
        self.data = data
        self.config = config
        self.ccLength = self.config[0]
    def genreate(self):
        if self.config[1] == 'srt':
            self.generateSRT()
        elif self.config[1] == 'vtt':
            self.generateVTT()
        else:
            print("Unknown caption format %s"%self.format)
            raise Exception
    def generateSRT(self):
        text = ''
        ccNumber = 0
        for caption in self.data:
            lineOfText = caption[2]
            start = caption[0]
            if start < 0:
                start = 0
            end = caption[1]
            words = lineOfText.count(' ')
            divisions = (words//self.ccLength)+1
            words = lineOfText.split(' ')
            duration = end-start
            smallDuration = duration/divisions
            for div in range(0, divisions):
                tend = (div+1)*self.ccLength
                tstart = div*self.ccLength
                if div == divisions:
                    captionText = words[tstart:]
                else:
                    captionText = words[tstart:tend]
                finalCaptionText = ''
                for w in captionText:
                    finalCaptionText += str(w)+' '
                text += str(ccNumber)+'\n'
                text += convert_time(start+(smallDuration*div))+' --> '+convert_time(start+(smallDuration*(div+1)))+'\n'
                text += str(finalCaptionText)+'\n'
                print(finalCaptionText)
                text += '\n'
                ccNumber += 1
        print(text)
        return text
    def generateVTT(self):
        print(self.data)
        print("Unfinished...")
        raise Exception