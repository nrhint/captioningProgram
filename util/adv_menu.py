##Nathan Hinton
##This will be the advanced menu for the program

from util.file_util import write_file


class AdvMenu:
    def __init__(self, config):
        self.config = config
        self.exit = False
    def run(self):
        while self.exit == False:
            i = int(input("""
            Options:
            (0): Exit the menu
            (1): Make a one time change to the configuration.
            (2): Update the configuration file.
            (3): Update this program.
            (4): Beta menu
            (5): Format converter (only vtt to srt supported as of now)
            (6): Batch format change

            """))
            if i == 0: #Exit the menu all the way
                print("Exiting the advanced menu...")
                self.exit = True
            elif i == 1 or i == 2: #Update the configuration
                up = False
                while up == False:
                    x = int(input("""
                    (0): Exit this menu.
                    (1): Change average closed caption length in characters.
                    (2): Change default output format.
                    (3): Change default file to open.
                    (4): Change if the program will automatically use the default file.

                    """))
                    if x == 0: #Exit
                        if i == 2:
                            generateConfigFile()
                            print("Configuration file updated!")
                            print("Reloading configuration...")
                            from data.config import Config
                            self.config = Config('config.cfg')
                        up = True
                    elif x == 1: #ccLength
                        self.config.ccLength = (int(input("New value in characters: ")))
                    elif x == 2: #Default format
                        z = int(input("1 = SRT, 2 = VTT    "))
                        if z == 1: #SRT
                            self.config.format = 'srt'
                        elif z == 2: #VTT
                            self.config.format = 'vtt'
                        else: #Error in input for the format option
                            print("Invalid option! Please try again.")
                    elif x == 3: #Default file to open
                        self.config.deafultCaptionFile = str(input("what is the new file name for the default file: "))
                        print("File changed!")
                    elif x == 4: #If the program auto opens the default file
                        z = input('Open automatically? (Y/n)  ')
                        if z == 'n':
                            self.config.autoOpenFile = 'False'
                            print("value set to False")
                        else:
                            self.config.autoOpenFile = 'True'
                            print("Value set tp True")
            elif i == 3: #Update the program
                from util.update import runUpdate
                runUpdate(self.config)
            elif i == 4:
                from util.beta_menu import betaMenu
                betaMenu(self.config)
            elif i == 5:
                from util.formatConverter import Convert
                Convert()
            elif i == 6:
                from util.formatConverter import Convert
                from os import walk, path
                paths = []
                folder = input('Folder to scan: ')
                for root, dirs, files in walk(folder, topdown=False):
                    for name in files:
                        if name[-3:] == 'vtt':
                            paths.append(path.join(root, name))
                print('found %s file(s) to convert'%len(paths))
                print(paths)
                for p in paths:
                    c = Convert(p)
            else:
                print("invalid option")
        return self.config
    
def generateConfigFile(config):
    data = """##This is the config file that will contain data for the program

#default ccLength
%s

#default optput format
%s

#default file to use:
%s

#Should I use the default file automatically
%s

#Default size
%s

#Default horizontal position
%s

#Default vertical position
%s

#Enable debugging:
%s

#Number of runs:
%s
"""%(config.ccLength, config.format, config.deafultCaptionFile, config.autoOpenFile, config.defaultSize, config.horizontalPosition, config.verticalPosition, config.saveDump, config.runNumber)
    from util.file_util import write_file
    write_file('.', 'config', 'cfg', data)    
