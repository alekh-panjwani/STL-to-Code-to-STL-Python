from build123d import *
import trimesh

mesh = trimesh.load("thumb_b.stl")
trimesh.repair.fix_normals(mesh)
trimesh.repair.fill_holes(mesh)
mesh.export("thumb_b_output.stl")