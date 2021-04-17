##Nathan Hinton
##This will be the menu for beta testing if people want to try out new features that may or may not be working.

class betaMenu:
    def __init__(self, config, textData):
        self.config = config
        self.textData = textData
        print('checking for updates...')
        from util.update import runUpdate
        runUpdate(self.config)
        self.betaMenu()
    def betaMenu(self):
        from util.render_frame import RenderFrame
        render = RenderFrame(self.config, self.textData)
        render.loadFrameFromCaption()
        render.showFrame()
        print("Pause")

