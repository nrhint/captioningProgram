from os import error
from util.time_util import convert_time

class GenerateCaptions:
    def __init__(self, data, config):
        self.data = data
        self.config = config
        self.ccLength = self.config.ccLength
    def generate(self):
        linesAndTimes = self.splitLines()
        if self.config.format == 'srt':
            print('Generate SRT format...')
            data = self.generateSRT(linesAndTimes)
        elif self.config.format == 'vtt':
            print('Generate VTT format...')
            data = self.generateVTT(linesAndTimes)
        else:
            print("Unknown caption format %s"%self.format)
            raise Exception
        return data
    def splitLines(self):
        text = ''
        data = []
        ind = 1
        for line in self.data:
            tstart = 0
            tend = 0
            words = line.text
            divisions = 1
            while len(words)/divisions > self.ccLength:
                divisions += 1
            ccLength = int(len(words)/divisions)#This will set the ccLength to a closer value to make it more consistent.
            #print('\n' + str(verse.number) + '\t' + verse.text)
            words = [char for char in line.text]
            ##Generate the times for this verse
            try:
                if line.startTime < 0:
                    line.startTime = 0
            except TypeError:
                print("Something went wrong in the caption generation. There may not be enough times for the program to use. This will result in a unfinished caption file where it will only have part of the data in it.")
                return text
            duration = int(line.endTime)-int(line.startTime)
            smallDuration = round(duration/divisions, 3)
            #print('%s\t%s\t%s\t%s\t%s'%(verse.id, verse.start_frame, verse.end_frame, smallDuration, divisions))
            ##Generate the lines for the file
            for div in range(0, divisions):
                #print(ind)
                if tend != 0:
                    tstart = tend
                tend = (div+1)*ccLength
                if tend >= len(words):
                    tend = len(words)-1
                else:
                    while words[tend] != ' ':
                        tend -= 1
                
                #tstart = div*ccLength
                new_start_time = line.startTime + (smallDuration * div)
                new_end_time = line.startTime + (smallDuration * (div + 1))
                if div == divisions - 1:
                    captionText = words[tstart:]
                    new_end_time = line.endTime
                else:
                    captionText = words[tstart:tend]
                #convert the caption text from a list to a string
                finalCaptionText = ''
                for w in captionText:
                    finalCaptionText += str(w)
                #print("%s: %s %s"%(ind, tstart, tend))
                data.append([str(ind), str(convert_time(new_start_time)), str(convert_time(new_end_time)), str(finalCaptionText)])
                text += str(ind)+'\n'
                text += str(convert_time(new_start_time))+' --> '+ str(convert_time(new_end_time))+'\n'
                text += str(finalCaptionText)+'\n'
                text += '\n'
                ind += 1
        return data
    def generateSRT(self, linesAndTimes):
        text = ''
        for line in linesAndTimes:
            text += line[0] +'\n'
            #text += '\n'
            text += line[1] + ' --> ' + line[2] + '\n'
            text += line[3] +'\n'
            text += '\n'
        return text

    def generateVTT(self, linesAndTimes):
        text = 'WEBVTT\n'
        for line in linesAndTimes:
            text += line[0] +'\n'
            text += '%s --> %s size:%s%% line:%s%% position:%s%\n'%(line[1], line[2], self.config.defaultSize, self.config.verticalPosition, self.config.horizontalPosition)
            text += line[3] +'\n'
            text += '\n'
        return text