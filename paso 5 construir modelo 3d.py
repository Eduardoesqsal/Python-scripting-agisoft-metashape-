import Metashape

ruta_proyecto = "C:/Users/eduar/videos/proyecto.psx"

doc = Metashape.Document()
doc.open(ruta_proyecto)
chunk = doc.chunk

# Construir modelo 3D sin argumentos (método básico)
chunk.buildModel()

doc.save()

print("Paso 5 completado: Modelo 3D construido.")
