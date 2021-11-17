##Nathan Hinton
##When given a SRT file it will parse the file and return output that can be used

from data.data import Line

class SRT:
    def __init__(self, data):
        self.data = data
        counter = 1
        nextLineIsTime = False
        self.lines = []
        self.startTimes = []
        self.endTimes = []
        self.words = ''
        self.recentWords = ''
        for line in data.splitlines():
            if str(counter) == line:
                counter += 1
                nextLineIsTime = True
                justMadeLine = False#Now that it is a new line you can safely make a new line
            elif nextLineIsTime:#Prevent this from being checked if the line changes
                tmp = line.split(' --> ')
                self.startTimes.append(tmp[0])
                self.endTimes.append(tmp[1])
                nextLineIsTime = False
            elif line == '':
                if not justMadeLine:
                    self.lines.append(Line(text=self.recentWords, startTime=self.startTimes[-1], endTime=self.endTimes[-1]))
                    self.words += self.recentWords
                    justMadeLine = True
            else:
                self.recentWords += line
    def reloadTimes(self):
        counter = 0
        for line in self.lines:
            line.startTime = self.startTimes[counter]
            line.endTime = self.endTimes[counter]
            counter += 1



def writeFile(lines, filepath):
    data = ""
    counter = 1
    for line in lines:
        data += '%s\n'%counter
        data += '%s --> %s\n'%(line.startTime, line.endTime)
        data += '%s\n'%line.text
        data += '\n'
        counter += 1
    with open(filepath, 'w') as file:
        file.write(data)

