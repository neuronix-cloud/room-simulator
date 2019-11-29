from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from math import pi
 
class MyApp(ShowBase):

    def left(self):
        #print(self.scene.set)
        h = app.scene.getH()+1
        app.scene.setH(h)
        print("left", h)

    def right(self):
        h = app.scene.getH()-1
        app.scene.setH(h)
        print("right", h)

    def forward(self):
        p = app.scene.getP()-1
        app.scene.setP(p)
        print("forward", p)

    def backward(self):
        p = app.scene.getP()+1
        app.scene.setP(p)
        print("backward", p)

    def up(self):
        r = app.scene.getR()+1
        app.scene.setR(r)
        print("up")

    def down(self):
        r = app.scene.getR()-1
        app.scene.setR(r)
        print("backward", r)

    def status(self):
        print(self.scene.getHpr())
        print(app.scene.getPos())
 
    def __init__(self):
        ShowBase.__init__(self)
 
        # Load the environment model.
        self.scene = self.loader.loadModel("LivingRoom.egg")
        #self.scene = self.loader.loadModel("models/environment")

        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(1, 1, 1)
        self.scene.setPos(-1, -1, .05)
        self.scene.setHpr(30,30,0)

        plight = PointLight('plight')
        plight.setColor(VBase4(1, 1, 1, 1))
        #plight.setAttenuation((1, 0, 1))
        plnp = self.render.attachNewNode(plight)
        plnp.setPos(0,0,1)
        self.render.setLight(plnp)

        self.accept("arrow_up", self.forward)
        self.accept("arrow_down", self.backward)
        self.accept("arrow_left", self.left)
        self.accept("arrow_right", self.right)
        self.accept("page_up", self.up)
        self.accept("page_down", self.down)

        self.accept("space", self.status)

# interactive console
from direct.stdpy import threading
from code import InteractiveConsole
ic = InteractiveConsole(globals())
threading.Thread(target=ic.interact).start()

# start
app = MyApp()
app.run()

#not reached
app.scene
print("\n".join(dir(app.scene)))
