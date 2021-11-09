##Nathan Hinton
##This will controll the menu for converting from keypresses into srt files

##THERE IS AN ERROR WHERE THE LAST CAPTION IS CUT OFFs

from util.formatConverter import Convert

v = True

def run():
    i = input("Please enter filename: ")
    try:
        with open(i, 'r') as file:
            fileData = file.read()
    except FileNotFoundError:
        print("File was not found. Would you like to try again? (Y/n):")
        i = input()
        if i == 'n':
            pass
        else:
            run()
    Convert(i)

if v:print("Loaded module formatConverter")