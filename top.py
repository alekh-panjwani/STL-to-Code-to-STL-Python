from build123d import *
import trimesh

mesh = trimesh.load("top.stl")
trimesh.repair.fix_normals(mesh)
trimesh.repair.fill_holes(mesh)
mesh.export("top_output.stl")