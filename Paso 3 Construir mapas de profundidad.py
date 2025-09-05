import Metashape

project_path = "C:/Users/eduar/videos/proyecto.psx"
doc = Metashape.Document()
doc.open(project_path)
chunk = doc.chunk

# Construir mapas de profundidad con parámetros por defecto
chunk.buildDepthMaps()

doc.save()
print("Mapas de profundidad construidos con parámetros por defecto.")
