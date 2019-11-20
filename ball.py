from direct.showbase.ShowBase import ShowBase
from twisted.internet.task import LoopingCall
from twisted.internet import reactor

from direct.stdpy import threading
from code import InteractiveConsole

 
class Ball(ShowBase):
 
    def __init__(self):
        ShowBase.__init__(self)
 
        self.ball = self.loader.loadModel("model/ball.stl")
        self.ball.setColor(255,0,0,0)
        self.ball.setScale(0.25, 0.25, 0.25)
        self.ball.setPos(-8, 42, 0)
        self.ball.reparentTo(self.render)
        self.floor = self.loader.loadModel("model/floor.stl")
        self.floor.setColor(0,255,0,0)
        self.floor.setScale(0.25, 0.25, 0.25)
        self.floor.setPos(-8, 42, 0)
        self.floor.reparentTo(self.render)

        # Apply scale and position transforms on the model.
        #self.scene.setScale(0.25, 0.25, 0.25)
        #self.scene.setPos(-8, 42, 0)
 
 
if __name__ == "__main__":

  ic = InteractiveConsole(globals())

  app = Ball()
  threading.Thread(target=ic.interact).start()
  app.run()
  # never reached
  type(app.scene)
  s = app.scene
  for x in dir(app.scene): print(x)
  l = s.find("**")



