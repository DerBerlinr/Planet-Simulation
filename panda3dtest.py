from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")
# config variables are here: https://docs.panda3d.org/1.10/python/programming/configuration/list-of-all-config-variables

from direct.showbase.ShowBase import ShowBase

class myGame(ShowBase):
    def __init__(self):
        super().__init__()

        box = self.loader.loadModel("models/box")
        box.setPos(0, 10, 0)
        box.reparentTo(self.render)

game = myGame()
game.run()