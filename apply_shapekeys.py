import bpy

# shape_key_index = 0 is Basis
#totalShapeKeys = bpy.data.shape_keys.keys()
#totalShapeKeys = bpy.context.object.data.shape_keys

# total length of All shapekeys for Selected Item
totalShapeKeys = len(bpy.context.object.data.shape_keys.key_blocks)

print(totalShapeKeys)
