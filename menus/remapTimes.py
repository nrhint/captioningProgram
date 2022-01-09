##Nathan Hinton
##This will remap the times in a SRT file

from data.SRT import SRT, writeFile
from util import transformTime

def run(i = ''):
    if i == '':
        i = input("Enter filename: ")
        if i != 'e':
            try:
                with open(i, 'r') as file:
                    data = file.read()
            except FileNotFoundError:
                print("File not found try again or input e to exit")
                run()
    else:
        with open(i, 'r') as file:
            data = file.read()
    if i != 'e':
        data = SRT(data)
        time = input("enter the number of milliseconds you want this to be changed by: ")
        try:
            time = int(time)
        except ValueError:
            print("Please enter a valid time to change by...")
            run(i)
        data.startTimes = transformTime.shiftTimes(data.startTimes, time)
        data.endTimes = transformTime.shiftTimes(data.endTimes, time)
        data.reloadTimes()
        writeFile(data.lines, i)
        print("Remaped!")

print("Loaded module remapTimes")