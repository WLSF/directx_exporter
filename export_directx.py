import bpy
import math
import mathutils
# ExportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ExportHelper, orientation_helper
from bpy.props import StringProperty
from bpy.types import Operator

bl_info = {
    "name": "Export to DirectX (.x) file",
    "author": "WLSF",
    "version": (0, 0, 1),
    "blender": (4, 0),
    "category": "Import-Export",

}

@orientation_helper(axis_forward='-Z', axis_up='Y')
class ExportDirectXData(Operator, ExportHelper):
    """Exports object to DirectX file .x extension"""
    bl_idname = "export.directx"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Export DirectX (.x)"

    # ExportHelper mix-in class uses this.
    filename_ext = ".x"

    filter_glob: StringProperty(
        default="*.x",
        options={'HIDDEN'}
    )

    def execute(self, context):
        return {'FINISHED'}


# Only needed if you want to add into a dynamic menu
def menu_func_export(self, context):
    self.layout.operator(ExportDirectXData.bl_idname, text=ExportDirectXData.bl_label)


# Register and add to the "file selector" menu (required to use F3 search "Text Export Operator" for quick access).
def register():
    bpy.utils.register_class(ExportDirectXData)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ExportDirectXData)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()