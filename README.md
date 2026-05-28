# Optimizador de CV — Emilio Ranucoli

Este repositorio contiene el script en Python desarrollado para generar un currículum vitae (CV) moderno, profesional y **altamente optimizado para sistemas ATS (Applicant Tracking Systems)**. 

El script genera automáticamente el CV en formato `.docx` y realiza la conversión a `.pdf` manteniendo la consistencia de estilos y un diseño impecable.

## 🚀 Características del CV Optimizado
- **Alineación ATS:** Estructura limpia y jerarquizada que permite una lectura fluida por los algoritmos de escaneo de candidatos (ATS).
- **Tipografía y Colores Curados:** Uso de la fuente *Calibri* con tamaños de fuente perfectamente balanceados y una paleta de colores profesional (Azul Marino y Negro carbón).
- **Hipervínculos Interactivos:** Enlaces directos a Correo, LinkedIn, GitHub y sitio web personal.
- **Formato de Margen Profesional:** Márgenes de 1.2 cm arriba/abajo y 1.6 cm a los lados para maximizar el uso del espacio sin sobrecargar la lectura.
- **Portabilidad:** Rutas relativas que permiten ejecutar el script desde cualquier directorio o máquina.

## 📁 Estructura del Proyecto
- `build_cv.py`: Script principal de Python que construye la estructura del documento con la biblioteca `python-docx` y genera el PDF.
- `EmilioRanucoli_MLEngineer.docx`: CV generado en formato Microsoft Word.
- `EmilioRanucoli_MLEngineer.pdf`: CV final convertido a formato PDF.
- `.gitignore`: Configuración para evitar subir archivos temporales de oficina o caché de Python.

## 🛠️ Requisitos e Instalación

Para ejecutar el generador localmente, necesitas tener instalado Python 3 y las siguientes dependencias:

1. **Instalar dependencias:**
   ```bash
   pip install python-docx docx2pdf
   ```

2. *(Opcional)* **docx2pdf:** Esta biblioteca utiliza la API de Microsoft Word para realizar la conversión a PDF con total fidelidad visual. Requiere que Microsoft Word esté instalado en el sistema operativo (compatible con Windows y macOS).

## 💻 Instrucciones de Uso

Para regenerar tu CV con cualquier modificación que hagas en la información o el formato, simplemente ejecuta el script desde tu terminal:

```bash
python build_cv.py
```

### Flujo del script:
1. Lee las especificaciones de formato y el contenido del CV redactado en el código.
2. Crea e inserta los estilos, márgenes, hipervínculos, secciones y tablas requeridas.
3. Guarda el archivo `.docx` localmente.
4. Llama a la herramienta `docx2pdf` para exportar la versión en `.pdf`.

---
*Desarrollado y mantenido por [Emilio Ranucoli](https://github.com/RanuK12).*
