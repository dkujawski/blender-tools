from pathlib import Path
import re

import bpy

# the last 3 digit number before the extension(s)
FILENAME_VERSION_PAT = re.compile(r"^.*(\d{3})\..+$")


def scene_setup(self, context):
    """Scene setup"""
    # Scene and unit setup for precision
    context.scene.unit_settings.system = "METRIC"
    context.scene.unit_settings.scale_length = 1
    context.scene.unit_settings.length_unit = "MILLIMETERS"
    # Clear existing mesh objects
    bpy.ops.object.select_all(action="DESELECT")
    bpy.ops.object.select_by_type(type="MESH")
    bpy.ops.object.delete()


def export_stl():
    """Export scene data into an stl file for printing"""

    sp = Path(bpy.context.blend_data.filepath)

    # look for any existing versioned stl files
    versions = [
        int(FILENAME_VERSION_PAT.match(stl).group(1))
        for stl in sorted(sp.parent.glob(f"{sp.stem}*.stl"))
        if FILENAME_VERSION_PAT.match(stl)
    ]
    if len(versions) > 0:
        # assume 3 digit zero pad version as last number before ext
        # increment to next version
        version = f"{max(versions) + 1}:03"

    filepath = sp.with_name(f"{sp.stem}{version}").with_suffix(".stl")
    bpy.ops.export_mesh.stl(filepath=filepath, use_scene_unit=True, global_scale=1.0)
