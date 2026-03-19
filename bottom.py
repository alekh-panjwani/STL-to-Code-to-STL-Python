from build123d import *
import trimesh

mesh = trimesh.load("bottom.stl")
trimesh.repair.fix_normals(mesh)
trimesh.repair.fill_holes(mesh)
mesh.export("bottom_output.stl")