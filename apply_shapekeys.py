import pdb
import bpy

# total length of All shapekeys for Selected Item
totalShapeKeys = len(bpy.context.object.data.shape_keys.key_blocks)

src_obj = bpy.context.active_object
src_obj
bpy.context.object.modifiers

copied_objects = []
# for shapekey in bpy.context.object.data.shape_keys.key_blocks:
for shapekey in src_obj.data.shape_keys.key_blocks:
    new_obj = bpy.context.active_object.copy()
    new_data = bpy.context.active_object.data.copy()
    new_obj.data = new_data
    bpy.context.collection.objects.link(new_obj)

    for new_shapekey in new_obj.data.shape_keys.key_blocks:
        if new_shapekey.name != shapekey.name:
            new_obj.shape_key_remove(new_shapekey)
    copied_objects.append(new_obj)

for i in range(len(copied_objects)):
    print(i)
    copied_objects[i].shape_key_clear()
    # bpy.context.view_layer.objects.active = copied_objects[i]   
    # bpy.context.object.modifier_apply(modifier="Mirror")

    # copied_objects[i].modifier_apply(modifier="Mirror")
    # if i != 0:
    #     copied_objects[0].join_shapes(copied_objects[i])

print(totalShapeKeys)
