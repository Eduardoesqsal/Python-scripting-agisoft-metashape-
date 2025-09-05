# 🗺️ Automatización de Flujo para Generación de Orto­mosaicos en Agisoft Metashape

Este repositorio contiene un conjunto de **8 scripts en Python** diseñados para automatizar distintas etapas del flujo de trabajo en **Agisoft Metashape**, desde la creación del proyecto hasta el procesamiento avanzado de ortomosaicos.

---

## 🚀 Requisitos Previos

- **Agisoft Metashape** instalado (con acceso a la consola o al entorno Python integrado).  
- **Python 3.x** compatible con la API de Metashape.  
- Imágenes en formatos compatibles: `.jpg`, `.jpeg`, `.png` o `.tif`.  
- Mantener los scripts, el proyecto y las imágenes en la **misma carpeta** para facilitar la ejecución.  

---

## 📂 Estructura de Scripts

- `script1.py` – Creación del proyecto y carga de todas las imágenes.  
- `script2.py` a `script8.py` – Procesamiento progresivo sobre el proyecto ya inicializado, incluyendo:  
  - Alineación de fotos  
  - Generación de nube de puntos  
  - Construcción de mallas y texturizado  
  - Generación de ortomosaicos  
  - Exportación de resultados  

> ⚠️ Es importante ejecutar los scripts en **orden secuencial**, ya que cada uno depende del proyecto y los resultados generados por el script anterior.  

---

## ⚙️ Configuración de Rutas en los Scripts

Cada script contiene variables donde se definen rutas absolutas.  
Estas rutas deben ser actualizadas según tu entorno local antes de ejecutar los scripts:

```python
# Carpeta donde se encuentran las imágenes
ruta_imagenes = r"C:\Users\eduar\videos\fotos_msi"

# Ruta donde se guardará o abrirá el proyecto Metashape
ruta_proyecto = r"C:\Users\eduar\videos\proyecto.psx"
