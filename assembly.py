from build123d import *
import trimesh

parts = [
    trimesh.load("bottom.stl"),
    trimesh.load("top.stl"),
    trimesh.load("thumb_a.stl"),
    trimesh.load("thumb_b.stl"),
    trimesh.load("wheel.stl"),
    trimesh.load("wheel_brace.stl"),
]

assembly = trimesh.util.concatenate(parts)
assembly.export("assembly_output.stl")