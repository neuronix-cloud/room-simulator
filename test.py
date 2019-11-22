import bpy

print("rendering")
bpy.context.scene.render.filepath='ball-in-room.png'
bpy.ops.render.render(write_still=True)
print("done")
