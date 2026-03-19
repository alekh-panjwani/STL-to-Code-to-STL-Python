from build123d import *
import trimesh

mesh = trimesh.load("wheel_brace.stl")
trimesh.repair.fix_normals(mesh)
trimesh.repair.fill_holes(mesh)
mesh.export("wheel_brace_output.stl")