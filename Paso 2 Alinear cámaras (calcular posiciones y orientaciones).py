import Metashape

ruta_proyecto = r"C:\Users\eduar\videos\proyecto.psx"

doc = Metashape.Document()
doc.open(ruta_proyecto)
chunk = doc.chunk

# Llamada simple sin argumentos
chunk.matchPhotos()
chunk.alignCameras()

doc.save()

print("Paso 2 completado: Cámaras alineadas con configuración por defecto.")
