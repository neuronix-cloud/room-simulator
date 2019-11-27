import bpy
from mathutils import Vector 
import os
import math

# objects in blender
C = bpy.context 
D = bpy.data 
R = bpy.ops.render 
O = D.objects

# degree to radiants
D2R = math.pi / 180

#for k in O.keys():
#    print(k)

cam = D.objects['Camera']
ball = D.objects['Ball']

bloc = Vector([0,0,0.11])
cloc = Vector([0,-0.5, 0.05])

cam.location = cloc
ball.location = bloc


def snap(dir):
    cx = int(cam.location.x*10)
    cy = int(cam.location.y*10)
    rz = int(cam.rotation_euler.z / D2R)
    bx = int(ball.location.x*10)
    by = int(ball.location.y*10)
    file = "%s/ball%dx%dcam%dx%dr%d.png"% (dir, bx, by, cx, cy, rz)
    print("rendering", file)
    C.scene.render.filepath= file
    R.render(write_still=True)
    print("done")

def rotateCam(dir):
    for i in range(0, 360, 10):
        cam.rotation_euler.z = i*D2R
        snap(dir)

def generate(dir):
    os.makedirs(dir, exist_ok=True)
    for j in [-1, -.75, -.5, -.25, 0, .25, .5, .75, 1]:
        for i in [0, .25, .5, .75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 3]:
            ball.location.x = j
            cam.location.y = -.5 - i
            rotateCam(dir)

ball.hide_render = False
generate("rotgen/ok")
ball.hide_render = True
generate("rotgen/ko")
