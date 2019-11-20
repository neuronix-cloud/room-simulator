OSC=/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD 

.PHONY: all
all: ball.stl floor.stl

ball.stl: ball-in-room.scad
	$(OSC) -DP=1 $< -o $@

floor.stl: ball-in-room.scad
	$(OSC) -DP=2 $< -o $@
