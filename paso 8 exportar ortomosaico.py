import Metashape

ruta_proyecto = "C:/Users/eduar/videos/proyecto.psx"
ruta_ortomosaico = "C:/Users/eduar/videos/ortomosaico.tif"

doc = Metashape.Document()
doc.open(ruta_proyecto)
chunk = doc.chunk

# Exportar ortomosaico sin especificar formato ni raster_type
chunk.exportRaster(ruta_ortomosaico)

print(f"Paso 8 completado: Ortomosaico exportado en {ruta_ortomosaico}")
