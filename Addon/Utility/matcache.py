import bpy


def backup_material_copy(slot):
    material = slot.material
    if "."+material.name.split("#:#")[1] + "_Original" in bpy.data.materials:
        print("Already backed up: " + material.name + ", skipping")
    else:
        print("Backing up material: "+material.name)
        dup = material.copy()
        dup.name = "." + material.name.split("#:#")[1] + "_Original"
        print("Backed up name: " + dup.name)


def backup_material_cache(slot, path):
    bpy.ops.wm.save_as_mainfile(filepath=path, copy=True)


def backup_material_cache_restore(slot, path):
    print("Restore cache")


def backup_material_restore(slot):
    material = slot.material
    if material.name.endswith("_Original"):
        if material.name[1:-9] in bpy.data.materials:
            slot.material = bpy.data.materials[original.name[1:-9]]
            print("Reset material to " + slot.material.name)
    elif "#:#" in material.name and material.name.split("#:#")[1] in bpy.data.materials:
        original = bpy.data.materials[
            material.name.split("#:#")[1]]
        slot.material = original
        material.name = material.name + "_temp"
        material.user_clear()
        bpy.data.materials.remove(material)
        # if original.name[1:-9] in bpy.data.materials:
        #    slot.material = bpy.data.materials[original.name[1:-9]]
        print("Reset material to " + slot.material.name)

    else:
        print("Couldn't find original for: " + material.name)
        pass
        # Check if material has nodes with lightmap prefix
