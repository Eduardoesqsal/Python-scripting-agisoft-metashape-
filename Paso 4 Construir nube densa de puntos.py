import Metashape

ruta_proyecto = "C:/Users/eduar/videos/proyecto.psx"
doc = Metashape.Document()
doc.open(ruta_proyecto)
chunk = doc.chunk

# Construir nube densa de puntos
chunk.buildPointCloud()

# Guardar proyecto
doc.save()

print("Nube densa construida y proyecto guardado.")
