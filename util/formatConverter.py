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
        lastNewLine = False
        for line in lines:
            #print(line)
            if line == '' and lastNewLine == False: #If it was a new line and there was not a new line before it:
                pass
                self.output += '\n'
                lastNewLine = True
            elif line == '' and lastNewLine == True: #Do not add anything because there is already a gap
                pass
            ##This section needs to be improved. Some files are done with hh:mm:ss.mmm which results in a line length of 29 while others are mm:ss.mmm which results in a line length of 23
            elif '-->' in line: #Add the line number and timestamp
                self.output += '%s\n'%counter
                if line[5] == '.': #timestamp format is mm:ss.mmm
                    self.output += '00:'+line[0:14]+'00:'+line[14:23]+'\n' #Used to be 29
                else: #timestamp format is hh:mm:ss.mmm
                    self.output += line[:29]+'\n'
                counter += 1
                lastNewLine = False
            else:
                self.output += line + ' \n'
                lastNewLine = False
        # Recurse up the filepath as to generate a new filename
        for x in range(len(filename), 0, -1):
            if filename[0:x][-1] == '/':
                path = filename[0:x-1]
                break
        write_file(path, 'converted', 'srt', self.output)
