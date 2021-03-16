##Nathan Hinton
##This will be the advanced menu for the program

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
            (3): update this program.

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
                            self.generateConfigFile()
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
                print("Unfinished...")
            else:
                print("invalid option")
        return self.config
    
    def generateConfigFile(self):
        data = """##This is the config file that will contain data for the program

#default ccLength
%s

#default optput format
%s

#default file to use:
%s

#Should I use the default file automatically
%s
"""%(self.config.ccLength, self.config.format, self.config.deafultCaptionFile, self.config.autoOpenFile)
        from util.file_util import write_file
        write_file('.', 'config', 'cfg', data)
        print("Configuration file updated!")
        print("Reloading configuration...")
        from data.config import Config
        self.config = Config('config.cfg')
