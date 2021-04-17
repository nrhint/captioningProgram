##This will have the configuration data saved in it

from util.file_util import parse_config

class Config:
    def __init__(self, configFile):
        try:
            fileData = parse_config(open(configFile, 'r').read())
            versionFile = open('version', 'r').read()
        except FileNotFoundError:
            print("Configuration file was not found!!!")
            raise Exception
        self.rawConfigData = fileData
        self.version = versionFile
        self.ccLength = self.rawConfigData[0]
        self.deafultFormat = self.rawConfigData[1]
        self.format = self.deafultFormat
        self.deafultCaptionFile = self.rawConfigData[2]
        self.autoOpenFile = self.rawConfigData[3]
        self.defaultSize = self.rawConfigData[4]
        self.horizontalPosition = self.rawConfigData[5]
        self.verticalPosition = self.rawConfigData[6]
        self.saveDump = int(self.rawConfigData[7])
        self.runNumber = int(self.rawConfigData[8])