import Metashape

ruta_proyecto = "C:/Users/eduar/videos/proyecto.psx"

doc = Metashape.Document()
doc.open(ruta_proyecto)
chunk = doc.chunk

# Generar ortomosaico sin argumentos (más compatible)
chunk.buildOrthomosaic()

doc.save()

print("Paso 7 completado: Ortomosaico generado.")
