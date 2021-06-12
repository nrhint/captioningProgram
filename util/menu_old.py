##Nathan Hinton
##This will controll all of the menus for doing things

##Nathan Hinton. This program takes code from the pynput project found at: https://github.com/moses-palmer/pynput

from util.file_util import open_file, write_file
from util.adv_menu import generateConfigFile
from data.data import Line

class Menu:
    def __init__(self, configuration):
        self.config = configuration
        self.error = False
        ################# Print startup message:
        print("Welcome to the manual captioning version %s!"%self.config.version)
        self.startingMenu()
    def startingMenu(self):
        if self.config.runNumber > 10:
            print("check for updates?")
            u = input('Y/n')
            if u != 'n':
                self.config.runNumber = 0
                from util.update import runUpdate
                runUpdate(self.config)
        else:
            self.config.runNumber += 1
        generateConfigFile(self.config)
        i = input('try to auto run ?(y/N)  ')
        if self.config.autoOpenFile == 'True' and self.error == False and i == 'y':
            self.dataFile = self.config.deafultCaptionFile
        else:
            self.error = False
            self.dataFile = input("""
Enter a for the advanced menu. This will take a text file that you have 
generated and it will turn it into captions! Please enter where you file 
is saved including the extension. For example: example.txt This will tell 
the program where to look for your file where you have typed the captions. 
Please type the file name then press enter:  """)
            if self.dataFile == 'advanced' or self.dataFile == 'a':
                self.advancedMenu()
            else:
                pass
        if self.dataFile[-4:] == '.txt':
            self.fileData = open_file('.', self.dataFile[:-4], 'txt')
        else:
            self.fileData = open_file('.', self.dataFile, 'txt')
        if self.fileData == 'Error':
            self.error = True
        if self.error:
            print("Error in startingMenu... Restarting operation")
            self.startingMenu()
        lines = self.fileData.split('\n')
        self.data = []
        for line in lines:
            self.data.append(Line(text = line))
        self.keyloggingMenu()
    def advancedMenu(self):
        from util.adv_menu import AdvMenu
        advancedMenu = AdvMenu(self.config)
        advancedMenu.run()
    def keyloggingMenu(self):
        print('Starting the keylogging to track the timestamps of the keypresses...')
        from util.log_keys import trackTimes
        self.data = trackTimes(self.data)
        if self.data != 'leaveMenu':
            self.generateCaptions()
        else:
            self.startingMenu()
    def generateCaptions(self):
        if self.config.saveDump:
            from pickle import dump
            dump(self.data, open('lastDump.pk', 'wb'))
            print('data successfully dumped to "lastDump.pk"')
        from util.generate_captions_util import GenerateCaptions
        generator = GenerateCaptions(self.data, self.config)
        dataToWrite = generator.generate()
        write_file('output', 'captions', 'srt', dataToWrite)
        self.startingMenu()