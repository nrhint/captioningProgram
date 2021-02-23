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
                if tend != 0:
                    tstart = tend
                tend = (div+1)*self.ccLength
                if tend > len(words):
                    tend = len(words)
                else:
                    while words[tend] != ' ':
                        tend -= 1
                #tstart = div*ccLength
                new_start_time = start + (smallDuration * div)
                new_end_time = start + (smallDuration * (div + 1))
                if div == divisions:# - 1:
                    captionText = words[tstart:]
                    new_end_time = end
                else:
                    captionText = words[tstart:tend]
                #convert the caption text from a list to a string
                finalCaptionText = ''
                for w in captionText:
                    finalCaptionText += str(w)+''
                #print("%s: %s %s"%(ind, tstart, tend))
                if finalCaptionText[1] == '\n':
                    finalCaptionText = finalCaptionText[2:]
                text += str(ccNumber)+'\n'
                text += str(convert_time(new_start_time))+' --> '+ str(convert_time(new_end_time))+'\n'
                text += str(finalCaptionText)+'\n'
                text += '\n'
                ccNumber += 1

        print(text)
        return text
    def generateVTT(self):
        print(self.data)
        print("Unfinished...")
        raise Exception