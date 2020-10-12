import bpy
import numpy as np 

#environment
bpy.context.scene.eevee.use_ssr = True
bpy.context.scene.eevee.use_ssr_halfres = False
bpy.context.scene.eevee.use_ssr_refraction = True
#bpy.context.space_data.shading.use_scene_world_render = False


#DO MANUALLY SET SPACE SHADING

#initiate nucleus
#pos = 10*(np.random.rand(3)-0.5)
pos = np.zeros(3)
bpy.ops.mesh.primitive_cube_add(location=(pos[0],pos[1],pos[2]))
bpy.context.object.name = 'Nucleus'
bpy.ops.object.subdivision_set(level=5, relative=False)
bpy.context.object.modifiers["Subdivision"].render_levels = 5
bpy.ops.object.mode_set(mode='OBJECT')

#Set surface form
tex = bpy.data.textures.new("Voronoi", 'VORONOI')
tex.distance_metric = 'DISTANCE_SQUARED'
modifier = bpy.context.object.modifiers.new(name="Displace", type='DISPLACE')
modifier.texture = bpy.data.textures['Voronoi']
modifier.texture.distance_metric = 'DISTANCE_SQUARED'
modifier.strength = -0.3

#smoothen out
bpy.ops.object.shade_smooth()

#color 
a = np.array([0.0.191202, 0.0908417, 0.327778, 1])

#Material specifications
bpy.data.materials["Material"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = a
#bpy.data.materials["Material"].node_tree.nodes["Principled BSDF"].inputs[15].default_value = 1
bpy.data.materials["Material"].roughness = 0.1
#bpy.data.materials["Material"].blend_method = 'BLEND'
#bpy.data.materials["Material"].use_screen_refraction = True

#define this material for our object
activeObject = bpy.context.active_object
mat = bpy.data.materials["Material"]
activeObject.data.materials.append(mat)

#duplicate core and rename as membrane
bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0,0,0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
bpy.ops.transform.resize(value=(1.5,1.5,1.5), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.context.object.name = 'Membrane'

#define different surface form 
bpy.context.object.modifiers["Displace"].strength = 0.2


#define this material for our object\

bpy.context.scene.objects["Membrane"].select_set(True)

bpy.context.object.active_material_index = 0 #select the top material
bpy.ops.object.material_slot_remove() #delete it

activeObject = bpy.context.active_object
mat2 = bpy.data.materials.new(name="MaterialMembrane")
mat2.use_nodes = True

bpy.data.materials["MaterialMembrane"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = a
bpy.data.materials["MaterialMembrane"].blend_method = 'BLEND'
bpy.data.materials["MaterialMembrane"].node_tree.nodes["Principled BSDF"].inputs[15].default_value = 1
bpy.data.materials["MaterialMembrane"].roughness = 0.1
bpy.data.materials["MaterialMembrane"].use_screen_refraction = True


activeObject.data.materials.append(mat2)

#bpy.data.materials["MaterialMembrane"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8, 0.230292, 0.525171, 1)



================================================================================================

bpy.ops.object.subdivision_set(level=5, relative=False)
bpy.context.space_data.context = 'MODIFIER'
bpy.context.area.ui_type = 'INFO'
bpy.context.object.modifiers["Subdivision"].render_levels = 3
bpy.context.object.modifiers["Subdivision"].render_levels = 4
bpy.context.object.modifiers["Subdivision"].render_levels = 5
bpy.ops.object.modifier_add(type='DISPLACE')
bpy.ops.texture.new()
bpy.data.textures["Texture"].name = "Texture"
bpy.data.textures["Texture"].type = 'VORONOI'
bpy.data.textures["Texture"].distance_metric = 'DISTANCE_SQUARED'
bpy.ops.object.shade_smooth()
bpy.context.space_data.context = 'MODIFIER'
bpy.context.object.modifiers["Displace"].strength = 0.9
bpy.context.object.modifiers["Displace"].strength = 0.8
bpy.context.object.modifiers["Displace"].strength = 0.7
bpy.context.object.modifiers["Displace"].strength = 0.6
bpy.context.object.modifiers["Displace"].strength = 0.5
bpy.context.object.modifiers["Displace"].strength = 0.4
bpy.context.object.modifiers["Displace"].strength = 0.3
bpy.context.object.modifiers["Displace"].strength = 0.2
bpy.context.object.modifiers["Displace"].strength = 0.0999999
bpy.context.object.modifiers["Displace"].strength = -6.33299e-08
bpy.context.object.modifiers["Displace"].strength = -0.1
bpy.context.object.modifiers["Displace"].strength = -0.2
bpy.context.object.modifiers["Displace"].strength = -0.3
bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_resize={"value":(2.17622, 2.17622, 2.17622), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "center_override":(0, 0, 0), "release_confirm":False, "use_accurate":False})
bpy.context.object.modifiers["Displace"].strength = -0.2
bpy.context.object.modifiers["Displace"].strength = -0.1
bpy.data.textures["Texture"].name = "Texture"
bpy.data.textures["Texture"].type = 'STUCCI'
bpy.context.space_data.shading.type = 'RENDERED'
bpy.context.space_data.context = 'RENDER'
bpy.context.scene.eevee.use_ssr = True
bpy.context.scene.eevee.use_ssr_halfres = False
bpy.context.scene.eevee.use_ssr_refraction = True
bpy.context.scene.eevee.use_shadow_high_bitdepth = True
bpy.context.area.ui_type = 'ShaderNodeTree'
bpy.ops.node.select(wait_to_deselect_others=True, mouse_x=1011, mouse_y=72, extend=False, deselect_all=True)
bpy.ops.node.select_box(tweak=True, xmin=1011, xmax=1034, ymin=72, ymax=116)
bpy.ops.outliner.item_activate(extend=False, deselect_all=True)
bpy.ops.outliner.item_rename()
bpy.ops.outliner.item_activate(extend=False, deselect_all=True)
bpy.ops.outliner.item_rename()
bpy.data.materials["Material"].node_tree.nodes["Principled BSDF"].inputs[16].default_value = 1
bpy.data.materials["Material"].node_tree.nodes["Principled BSDF"].inputs[15].default_value = 1
bpy.data.materials["Material"].node_tree.nodes["Principled BSDF"].inputs[16].default_value = 0
bpy.context.space_data.context = 'TEXTURE'
bpy.context.space_data.context = 'MATERIAL'
bpy.context.object.active_material.blend_method = 'CLIP'
bpy.context.object.active_material.use_screen_refraction = True
bpy.ops.outliner.item_activate(extend=False, deselect_all=True)
bpy.ops.object.material_slot_add()
bpy.ops.material.new()
bpy.context.object.active_material_index = 0
bpy.context.object.active_material.name = "Membrane"
bpy.context.object.active_material_index = 1
bpy.context.object.active_material.name = "Nucleus"
bpy.ops.object.editmode_toggle()
bpy.ops.object.material_slot_assign()
bpy.ops.node.select(wait_to_deselect_others=True, mouse_x=835, mouse_y=246, extend=False, deselect_all=True)
bpy.data.materials["Nucleus"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8, 0.147511, 0.758692, 1)
bpy.data.materials["Nucleus"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8, 0.147511, 0.758692, 1)
bpy.ops.node.select(wait_to_deselect_others=True, mouse_x=1087, mouse_y=111, extend=False, deselect_all=True)
bpy.data.materials["Nucleus"].node_tree.nodes["Principled BSDF"].inputs[7].default_value = 0.0818182
bpy.context.object.active_material_index = 0
bpy.data.materials["Membrane"].node_tree.nodes["Principled BSDF"].inputs[7].default_value = 0
bpy.ops.outliner.item_activate(extend=False, deselect_all=True)
bpy.ops.outliner.item_activate(extend=False, deselect_all=True)
bpy.ops.outliner.item_activate(extend=False, deselect_all=True)
bpy.ops.outliner.item_activate(extend=False, deselect_all=True)
bpy.ops.node.select(wait_to_deselect_others=True, mouse_x=953, mouse_y=269, extend=False, deselect_all=True)
bpy.ops.object.editmode_toggle()
bpy.ops.transform.resize(value=(0.673563, 0.673563, 0.673563), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.context.space_data.context = 'MATERIAL'
bpy.context.object.active_material.refraction_depth = 0.2
bpy.context.object.active_material.refraction_depth = 0.1
bpy.context.object.active_material.refraction_depth = 0
bpy.context.object.active_material.refraction_depth = 0.1
bpy.context.object.active_material.refraction_depth = 0.2
bpy.context.object.active_material.refraction_depth = 0.3
bpy.context.object.active_material.refraction_depth = 0.4
bpy.context.object.active_material.refraction_depth = 0.3
bpy.context.object.active_material.refraction_depth = 0.2
bpy.context.object.active_material.refraction_depth = 0.1
bpy.context.space_data.shading.use_scene_world_render = False
bpy.context.space_data.shading.use_scene_world_render = True
bpy.context.space_data.shader_type = 'WORLD'
bpy.ops.node.select(wait_to_deselect_others=False, mouse_x=550, mouse_y=214, extend=False, deselect_all=True)
bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (1, 1, 1, 1)
bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (1, 1, 1, 1)
bpy.context.space_data.shading.use_scene_world_render = False
bpy.context.space_data.shading.use_scene_world_render = True
bpy.ops.outliner.item_activate(extend=False, deselect_all=True)
bpy.ops.outliner.item_activate(extend=False, deselect_all=True)
bpy.context.object.active_material_index = 1
bpy.context.object.active_material_index = 0
bpy.context.object.active_material_index = 1
bpy.data.materials["Nucleus"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8, 0.0742883, 0.66872, 1)
bpy.data.materials["Nucleus"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8, 0.127669, 0.62184, 1)
bpy.data.materials["Nucleus"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8, 0.127669, 0.62184, 1)
bpy.data.materials["Nucleus"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.158961, 0.102242, 0.291771, 1)
bpy.data.materials["Membrane"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.219526, 0.0953075, 0.304987, 1)
bpy.data.materials["Membrane"].node_tree.nodes["Principled BSDF"].inputs[0].default_value[3] = 0.392857
bpy.data.materials["Membrane"].node_tree.nodes["Principled BSDF"].inputs[0].default_value[3] = 1
bpy.data.materials["Membrane"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.219526, 0.0953075, 0.304987, 1)
bpy.ops.transform.resize(value=(1.57065, 1.57065, 1.57065), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.data.materials["Membrane"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.327638, 0.139883, 0.457531, 1)
bpy.data.materials["Membrane"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.327638, 0.139883, 0.457531, 1)
bpy.context.space_data.context = 'TEXTURE'
bpy.data.textures["Texture"].type = 'VORONOI'
bpy.context.space_data.context = 'MODIFIER'
bpy.context.object.modifiers["Displace"].strength = -0.2
bpy.context.object.modifiers["Displace"].strength = -0.1
bpy.context.object.modifiers["Displace"].strength = -8.56817e-08
bpy.context.object.modifiers["Displace"].strength = 0.0999999
bpy.context.object.modifiers["Displace"].strength = 0.2
bpy.ops.transform.resize(value=(1.26559, 1.26559, 1.26559), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.context.space_data.context = 'TEXTURE'
bpy.data.textures["Texture"].type = 'MAGIC'
bpy.data.textures["Texture"].type = 'CLOUDS'
bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (1, 1, 1, 1)
bpy.ops.node.select(wait_to_deselect_others=False, mouse_x=578, mouse_y=227, extend=False, deselect_all=True)
bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (0.552011, 0.323143, 0.491021, 1)
