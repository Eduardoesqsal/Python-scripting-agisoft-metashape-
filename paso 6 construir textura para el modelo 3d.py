import Metashape

ruta_proyecto = "C:/Users/eduar/videos/proyecto.psx"

doc = Metashape.Document()
doc.open(ruta_proyecto)
chunk = doc.chunk

# Construir UV sin argumentos
chunk.buildUV()

# Construir textura sin argumentos para evitar error
chunk.buildTexture()

doc.save()

print("Paso 6 completado: Textura construida.")
