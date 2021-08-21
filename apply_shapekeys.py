import bpy

# shape_key_index = 0 is Basis
#total_shape_keys = bpy.data.shape_keys.keys()
#total_shape_keys = bpy.context.object.data.shape_keys

# total length of All shapekeys for Selected Item
total_shape_keys = len(bpy.context.object.data.shape_keys.key_blocks)

print(total_shape_keys)
