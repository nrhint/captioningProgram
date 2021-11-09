##Nathan Hinton
##This menu file will allow you to convert between different formats of captions

v = True

from data.config import Config
from util.file_util import write_file
from util.generate_captions_util import GenerateCaptions
from data.data import Line
from util.log_keys import trackTimes
from pickle import dump

config = Config('config.cfg')

def run():
    i = input("Please enter filename: ")
    try:
        with open(i, 'r') as file:
            fileData = file.read()
        data = []
        for line in fileData.splitlines():
            data.append(Line(text = line))
    except FileNotFoundError:
        print("File was not found. Would you like to try again? (Y/n):")
        i = input()
        if i == 'n':
            pass
        else:
            run()
    data = trackTimes(data)
    if data != 'leaveMenu':
        if v:
            dump(data, open('lastDump.pk', 'wb'))
            print('data successfully dumped to "lastDump.pk"')
        generator = GenerateCaptions(data, config)
        dataToWrite = generator.generate()
        write_file('output', 'captions', 'srt', dataToWrite)
    elif data == 'leaveMenu':
        print("Menu was left")
    else:
        print("There was an unknown error...")

if v:print("Loaded module srtFromKeys")