##Nathan Hinton
##This will change the caption format of a file from one thing to another

from util.file_util import open_file, write_file

class Convert:
    def __init__(self, i = False):
        if i == False:
            self.i = input('Enter the file name: ')
            self.raw = False
        else:
            self.i = i
            self.raw = True
        if self.i[-3:] == 'vtt':
            print('vtt format')
            self.vttToSrt()
            print("PAH!")
        elif self.i[-3:] == 'srt':
            print('srt format')
        else:
            print('the file format is unsupported. Exiting the converter...')
    def vttToSrt(self):
        if not self.raw:
            self.file = open_file('.', self.i[:-4], self.i[-3:])
        else:
            self.file = open(self.i, 'r').read()
        self.output = ''
        #Search for the start of the file:
        index = 0
        while self.file[index] != '0':
            index +=1
        if self.file[index:index+2] == '00':
            print('Start found!')
        else:
            print("Failed")
            from time import sleep
            sleep(5)
            raise Exception
        self.file = self.file[index:]
        lines = self.file.split('\n')
        counter = 1
        for line in lines:
            print(line)
            if line[0:2] == '00':
                self.output += '%s\n'%counter
                self.output += line[:29]+'\n'
                counter += 1
            elif line == '': #If it was a new line:
                self.output += '\n'
            else:
                self.output += line + '\n'
        if self.raw:
            self.finishedData = self.output
        else:
            write_file('output', 'converted', 'srt', self.srtFormattedFile)
            print("File written to ./output/converted.srt")
