import bpy

bl_info = {
    "name" : "Add Pose Copy Buttons",
    "author" : "Syler, leokaze",
    "version": (0, 2),
    "description": "Adds Pose Copy Buttons To Header",
    "blender" : (2, 80, 0),
    "category" : "3D view"
}

class CopyPasteFlipPoseOP(bpy.types.Operator):
    """Copy and paste de flipped current pose for selected bones"""
    bl_idname = "copypaste.flipped_pose"
    bl_label = "Copy Paste Flipped Pose"
    bl_options = {'UNDO', 'REGISTER'}

    def execute(self, context):
        bpy.ops.pose.copy()
        bpy.ops.pose.paste(flipped=True)
        return {'FINISHED'}


def menu_func(self, context):
    if bpy.context.mode == 'POSE':
        row = self.layout.row(align=True)
        row.separator()
        row.operator("pose.copy", text="", icon='COPYDOWN')
        row.operator("pose.paste", text="", icon='PASTEDOWN').flipped = False
        row.operator("pose.paste", text="", icon='PASTEFLIPDOWN').flipped = True
        row.operator("copypaste.flipped_pose", text="", icon='ARROW_LEFTRIGHT')
        

classes = [
]


def register():
    bpy.utils.register_class(CopyPasteFlipPoseOP)
    for c in classes:
        bpy.utils.register_class(c)

    # ------------------------------------------------------------------------------------------------------------
    # Append Register stuff
    # ------------------------------------------------------------------------------------------------------------
    bpy.types.VIEW3D_MT_editor_menus.append(menu_func)


def unregister():
    bpy.utils.unregister_class(CopyPasteFlipPoseOP)
    for c in classes:
        bpy.utils.unregister_class(c)

    # ------------------------------------------------------------------------------------------------------------
    # Append Unregister stuff
    # ------------------------------------------------------------------------------------------------------------

    bpy.types.VIEW3D_MT_editor_menus.remove(menu_func)

    
if __name__ == "__main__":
    register()
