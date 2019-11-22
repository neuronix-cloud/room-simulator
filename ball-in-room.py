import trimesh
import pyrender

ball = trimesh.load("ball-in-room.stl")
ball1 = pyrender.Mesh.from_trimesh(ball)

scene = pyrender.Scene()
scene.add(ball1)
pyrender.Viewer(scene, use_raymond_lighting=True)