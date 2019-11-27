import bpy
from mathutils import Vector 
import os

C = bpy.context 
D = bpy.data 
R = bpy.ops.render 
O = D.objects

cam = D.objects['Camera']
ball = D.objects['Ball']

bloc = Vector([0,0,0.11])
cloc = Vector([0,-0.5, 0.05])

cam.location = cloc
ball.location = bloc

