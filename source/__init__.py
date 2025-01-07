import importlib

import bpy
from bpy.props import PointerProperty
from bpy.utils import register_class, unregister_class

from . import helpers
from .operators.grid import ToGrid
from .scene_props import DkProps

importlib.reload(helpers)

classes = [DkProps, ToGrid]


def register():
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.dk_tools = PointerProperty(type=DkProps)


def unregister():
    for cls in classes:
        unregister_class(cls)

    del bpy.types.Scene.dk_tools
