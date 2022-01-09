##Nathan Hinton
##This will change the caption format of a file from one thing to another
##Used

from util.file_util import write_file
import tkinter.filedialog

class Convert:
    def __init__(self, i = False):

        filename = tkinter.filedialog.askopenfile()
        self.file = filename.read()
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
        write_file('output', 'converted', 'srt', self.output)
        print("File written to ./output/converted.srt")
