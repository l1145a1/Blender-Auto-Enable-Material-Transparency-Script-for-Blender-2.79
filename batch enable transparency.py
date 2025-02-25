import bpy

# Ambil objek yang dipilih
selected_object = bpy.context.object

# Periksa apakah objek dipilih dan memiliki material
if selected_object and selected_object.type == 'MESH':
    for mat in selected_object.material_slots:
        # Dapatkan material
        material = mat.material
        
        if material:
            # Menggunakan Blender Internal: aktifkan transparansi
            if material.use_nodes:
                # Pastikan material menggunakan shader standar
                material.use_transparency = True
                material.transparency_method = 'Z_TRANSPARENCY'  # Atur ke transparansi Z
                material.alpha = 0  # Tentukan transparansi penuh (alpha 0)
                print("Transparansi diaktifkan pada material: {}".format(material.name))
            else:
                # Jika tidak menggunakan node, aktifkan transparansi secara langsung
                material.use_transparency = True
                material.transparency_method = 'Z_TRANSPARENCY'  # Atur ke transparansi Z
                material.alpha = 0  # Tentukan transparansi penuh (alpha 0)
                print("Transparansi diaktifkan pada material (tanpa node): {}".format(material.name))
else:
    print("Objek yang dipilih tidak valid atau tidak ada objek yang dipilih.")
