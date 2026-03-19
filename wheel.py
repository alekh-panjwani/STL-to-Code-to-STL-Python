from build123d import *
import trimesh

mesh = trimesh.load("wheel.stl")
trimesh.repair.fix_normals(mesh)
trimesh.repair.fill_holes(mesh)
mesh.export("wheel_output.stl")