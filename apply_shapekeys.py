import bpy
import json

# shape_key_index = 0 is Basis
#total_shape_keys = bpy.data.shape_keys.keys()
#total_shape_keys = bpy.context.object.data.shape_keys

# total length of All shapekeys for Selected Item
totalShapeKeys = len(bpy.context.object.data.shape_keys.key_blocks)

src_obj = bpy.context.active_object

#new_obj = src_obj.copy()
#bpy.context.collection.objects.link(new_obj) #link object to scene
#bpy.ops.object.make_single_user(object=True, obdata=True, material=False, animation=False) #unlink shapekeys of dup from main object

new_obj = bpy.context.active_object.copy()
new_data = bpy.context.active_object.data.copy()
new_obj.data = new_data
bpy.context.collection.objects.link(new_obj)

print(totalShapeKeys)
