##Nathan Hinton
##This will controll all of the menus for doing things

##Nathan Hinton. This program takes code from the pynput project found at: https://github.com/moses-palmer/pynput

from util.file_util import open_file, write_file
from data.data import Line

class Menu:
    def __init__(self, configuration):
        self.config = configuration
        self.error = False
        ################# Print startup message:
        print("Welcome to the manual captioning version %s!"%self.config.version)
        self.startingMenu()
    def startingMenu(self):
        if self.config.autoOpenFile == 'True' and self.error == False:
            self.dataFile = self.config.deafultCaptionFile
        else:
            self.error = False
            self.dataFile = input("""
Press enter if you have entered your text into '%s' otherwise: This will take a
text file that you have generated and it will turn it into captions! Please 
enter where you file is saved including the extension. For example: example.txt
This will tell the program where to look for your file where you have typed the 
captions. Please type the file name then press enter:  """%(self.config.deafultCaptionFile))
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
        pass
    def keyloggingMenu(self):
        print('Starting the keylogging to track the timestamps of the keypresses...')
        from util.log_keys import trackTimes
        self.data = trackTimes(self.data)
        self.generateCaptions()
    def generateCaptions(self):
        from util.generate_captions_util import GenerateCaptions
        generator = GenerateCaptions(self.data, self.config)
        dataToWrite = generator.generate()
        write_file('output', 'captions', 'srt', dataToWrite)
        self.startingMenu()


# from pynput import keyboard

# from util.file_util import open_file, parse_config, write_file
# from util.generate_captions_util import GenerateCaptions

# from time import time

# pressed = ''
# def on_press(key):
#     global pressed
#     try:
#         pressed = key.char
#     except AttributeError:
#         pass

# def on_release(key):
#     global pressed
#     pressed = ''
#     if key == keyboard.Key.esc:
#         # Stop listener
#         print("listener stopped")
#         return False

# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()

# ##Print out the instructions:

# state = 'init'

# while state != False:
#     if state == 'init':
#         i = input('What is the name of the text file? ')
#         try:
#             text = open(i, 'r').read()
#             state = 'parse'
#         except FileNotFoundError:
#             print("File not found. Please try again...")
#             print()
#         data = []
#     elif state == 'parse':
#         text = text.split('\n')
#         print("""
# The file is ready, to use this program please read the instructions then press the 'g' key.

# When someone starts to talk press the t key. This will make the program print the line
# of text that it is captioning. When the speaker has finished the pronted line release
# the 't' key and wait for the next line to start t be spoken. The program will record
# the start and end of when you press and release the 't' key. When the video is finished
# playing then press the 'e' key to end the program. If at any time you want to restart
# press the 'r' key and it will restart the captioning section.""")
#         state = 'waitForGo'
#     elif state == 'waitForGo':
#         if pressed == 'g':
#             lineIndex = 0
#             baseTime = time()
#             state = 'wait'
#     elif state == 'wait':
#         if pressed == 't':
#             state = 'listen'
# #        elif pressed == '':
# #            state = 'released'
#         elif pressed == 'e':
#             state = 'end'
#             print(state)
#         elif pressed == 'r':
#             print("Restarting!")
#             state = 'init'
#     elif state == 'listen':
#         try:
#             line = text[lineIndex]
#             print('You are captioning: %s'%line)
#             wait = True
#             p = False
#             while wait:
#                 if pressed == 't' and not p:
#                     timeStart = time()
#                     p = True
#                 elif pressed != 't' and p:
#                     timeEnd = time()
#                     wait = False
#             timeEnd = time()
#             data.append([timeStart, timeEnd, line])
#             lineIndex += 1
#             if lineIndex> len(text):
#                 print("That was the last line in the file. Please press 'e'")
#             state = 'wait'
#         except IndexError:
#             state = 'whoops'
#     elif state == 'end':
#         print("Ending...")
#         state = False
#     elif state == 'whoops':
#         print("""
#         AAH! You seem to have run out of lines. If you accidentally pressed the
#         't key onw too many times simply press the e key. If your video is
#         still going and you have more text to caption please check the format
#         of the text file with your captions. Remember that every time there is
#         an enter in that file you get to press the 't' key once. This message
#         was caused by there not being enough lines in the file to complete the
#         action you requested.""")
#         print('\nY/n continue and generate the captions with the data that I have?')
#         i = input()
#         if i.lower() == 'y':
#             print("Okay! will do!")
#             state = 'end'
#         elif i.lower() == 'n':
#             print("Okay. this program will now restart and wait until you give it instructions.")
#             state = 'init'
#         else:
#             print("Invalid option... repeating instructions.")
#     else:
#         print("STATE ERROR")
#         print("State = %s"%state)
#         print("Restarting program this was caused by an internal error...")
#         state = 'init'

# #Zero out the timestamps

# for time in data:
#     time[0] = int(time[0])-baseTime
#     time[1] = int(time[1])-baseTime

# configData = open_file('.', 'config', 'cfg')
# configData = parse_config(configData)

# captioner = GenerateCaptions(data, configData)
# data_to_write = captioner.generate()

# try:
#     write_file('output', 'captions', 'srt', data_to_write)
# except:
#     print(data_to_write)
#     print('Generate test unsuccess.')
    
# print('File saved in %s/%s.%s'%('output', 'captions', 'srt'))
# input("Press the 'Enter' key to finish")
