import Metashape
import os

ruta_imagenes = r"C:\Users\eduar\videos\fotos_msi" # cambiar a su directorio 
ruta_proyecto = r"C:\Users\eduar\videos\proyecto.psx" # cambiar a su directorio

# Crear documento y agregar chunk
doc = Metashape.Document()
chunk = doc.addChunk()

# Agregar imágenes
imagenes = [os.path.join(ruta_imagenes, f) for f in os.listdir(ruta_imagenes)
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.tif'))]
chunk.addPhotos(imagenes)

# Guardar proyecto
doc.save(ruta_proyecto)

print("Paso 1 completado: Proyecto creado y fotos agregadas.")
