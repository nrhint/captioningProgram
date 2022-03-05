##Nathan Hinton
##This will change the caption format of a file from one thing to another
##Used

from util.file_util import write_file
import tkinter.filedialog

class Convert:
    def __init__(self, i = False):

        filename = tkinter.filedialog.askopenfilename()
        self.file = open(filename, 'r').read()
        self.output = ''
        #Search for the start of the file:
        index = 0
        lines = self.file.splitlines()
        while lines[index] == '' or lines[index][0] != '0':
            index +=1
        lines = lines[index:]
        counter = 1
        for line in lines:
            print(line)
            if line == '': #If it was a new line:
                self.output += '\n'
            elif line[2] == ':' and (line[5] == '.' or line[5] == ':'):
                self.output += '%s\n'%counter
                self.output += line[:23]+'\n' #Used to be 29
                counter += 1
            else:
                self.output += line + '\n'
            # Recurse up the filepath as to generate a new filename
        for x in range(len(filename), 0, -1):
            if filename[0:x][-1] == '/':
                path = filename[0:x-1]
                break
        write_file(path, 'converted', 'srt', self.output)
