from bpy.props import IntProperty, StringProperty
from bpy.types import FloatProperty, PropertyGroup


class DkProps(PropertyGroup):
    grid_fn: StringProperty(
        name="func",
        description="Name of the python function to use for creating the object",
        default="bpy.ops.mesh.primitive_ico_sphere_add",
        maxlen=1024,
        subtype="BYTE_STRING",
    )

    grid_count: IntProperty(
        name="count",
        description="Number times to run the set function",
        min=1,
        subtype="UNSIGNED",
    )

    grid_start: FloatProperty(
        name="start",
        description="Iteration start value",
    )

    grid_end: FloatProperty(
        name="end",
        description="Iteration end value",
    )

    grid_step: FloatProperty(
        name="step",
        description="Increment value for each iteration",
        default=1.0,
    )

    grid_pad: FloatProperty(
        name="pad",
        description="spacing value between each object",
        default=20.0,
    )
