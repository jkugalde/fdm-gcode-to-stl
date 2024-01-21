# GCODE to STL

There are two scripts in this repository. The first one is a python script to extract all the extruded lines from a gcode file into a txt file. The second one is an openscad script where the txt must be pasted to generate an stl.This 3d model is built with all the extruded lines from the gcode, including the infill. 

The objective of this project is to simulate stress in parts with the actual characteristics of a 3d printed piece. The idea is to compare and tune the scripts and simulation to match real test data. It is expected to observe anisotropy.

In the python script you must introduce the layer height of your gcode file and also its name. The output will be filename+'gcodestl.txt'

In the openscad file, you must introduce the extruder diameter and layer height. You have to also select if you want that the extruded lines in the simulation have discs in its ends. This will increase computing time but will be more similar to reality, as an extrusion is the projection of a disc being slided. You can select how round is the disc at the ends. 

A cube stl, gcode and transformed stl is included. The gcode was processed using Cura.

# Future work

- To test specimens.
- To modify the lines to account for porosity and rounded sides.



