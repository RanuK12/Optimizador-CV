# Optimizador de CV — Emilio Ranucoli

Este repositorio contiene el script en Python desarrollado para generar un currículum vitae (CV) moderno, profesional y **altamente optimizado para sistemas ATS (Applicant Tracking Systems)**. 

El script genera automáticamente el CV en formato `.docx` y realiza la conversión a `.pdf` manteniendo la consistencia de estilos y un diseño impecable.

## 🚀 Características del CV Optimizado
- **Alineación ATS:** Estructura limpia y jerarquizada que permite una lectura fluida por los algoritmos de escaneo de candidatos (ATS).
- **Tipografía y Colores Curados:** Uso de la fuente *Calibri* con tamaños de fuente perfectamente balanceados y una paleta de colores profesional (Azul Marino y Negro carbón).
- **Hipervínculos Interactivos:** Enlaces directos a Correo, LinkedIn, GitHub y sitio web personal.
- **Formato de Margen Profesional:** Márgenes de 1.2 cm arriba/abajo y 1.6 cm a los lados para maximizar el uso del espacio sin sobrecargar la lectura.
- **Configurable por Archivo JSON:** Todo el contenido del CV se carga desde un archivo JSON externo, permitiendo fácil personalización sin modificar el código.

## 📁 Estructura del Proyecto
- `build_cv.py`: Script principal de Python que construye la estructura del documento con la biblioteca `python-docx` y genera el PDF.
- `cv_config.json`: Archivo de configuración JSON con los datos del CV.
- `example_config.json`: Plantilla de ejemplo para crear tu propio archivo de configuración.
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
1. Lee las especificaciones de formato y el contenido del CV desde `cv_config.json`.
2. Crea e inserta los estilos, márgenes, hipervínculos, secciones y tablas requeridas.
3. Guarda el archivo `.docx` localmente.
4. Llama a la herramienta `docx2pdf` para exportar la versión en `.pdf`.

## 📝 Personalización del CV

Para crear tu propio CV:

1. **Copia el archivo de configuración:**
   ```bash
   cp example_config.json my_cv_config.json
   ```

2. **Edita `my_cv_config.json`** con tus datos personales, experiencia, educación y habilidades.

3. **Ejecuta el script:**
   ```bash
   python build_cv.py
   ```

### Estructura del archivo de configuración JSON:

- **Información personal:** name, title, email, phone, linkedin, github
- **Resumen profesional:** summary (opcional)
- **Experiencia laboral:** experience (array con company, title, dates, description)
- **Educación:** education (array con degree, institution, dates)
- **Habilidades:** skills (array de strings)

## 🛠️ Directivas del Sistema para el Agente de Optimización de CV (IA)

Si utilizas un modelo de Inteligencia Artificial (LLM) para procesar, ampliar o actualizar este currículum, configura el prompt del sistema o las instrucciones de generación bajo las siguientes dimensiones para asegurar un perfil competitivo y prolijo a nivel multinacional:

### 1. Reglas de Análisis de Keywords y Normalización Técnica
- **Validación Estricta de Siglas de IA:** El script debe incluir una regla de sanitización de texto que busque el patrón de caracteres **"Al"** (letra A seguida de L minúscula) en contextos tecnológicos y lo reemplace obligatoriamente por **"AI"** (letra A seguida de I mayúscula). Esto aplica para términos como *AI Specialist*, *AI Job Finder* o *Azure AI Fundamentals*.
- **Densidad de Palabras Clave (Keywords Indexing):** La IA debe agrupar y mantener visibles las tecnologías clave por categorías limpias (ej. *Languages & ML*, *Data Engineering*, *Cloud & DevOps*). No debe permitir que las herramientas queden enterradas en párrafos narrativos.

### 2. Reglas de Estructuración Jerárquica para ATS
- **Encabezados Estándar:** Solo usar los encabezados definidos en el código (Summary, Experience, Education, Skills).
- **Formato de Fechas:** Fechas consistentes en formato "YYYY - YYYY" o "YYYY - Presente".
- **Jerarquía Visual:** Títulos de empresa en negrita, seguidos del cargo y fechas en formato normal.
- **Párrafos con Sangría:** Descripciones de experiencia con sangría de 0.5 cm para mejorar la legibilidad.

### 3. Reglas de Optimización de Contenido para Human Readers
- **Verbos de Impacto:** Usar verbos de acción al inicio de cada punto logro (ej. *Desarrollé*, *Implementé*, *Optimicé*).
- **Métricas Cuantificables:** Incluir números y porcentajes siempre que sea posible (ej. *Reducí los tiempos de procesamiento en un 35%*).
- **Logros sobre Responsabilidades:** Enfocarse en logros y resultados en lugar de solo listar responsabilidades.

### 4. Reglas de Diseño y Formato Visual
- **Paleta de Colores:** Solo usar los colores definidos en el código (NAVY y BLACK).
- **Tipografía:** Solo usar Calibri para todos los elementos del texto.
- **Espaciado:** Márgenes de 1.2 cm (arriba/abajo) y 1.6 cm (izquierda/derecha).
- **Longitud Máxima:** Mantener el CV en 1-2 páginas máxime.

## 🔧 Próximos Pasos de Desarrollo

El proyecto se encuentra en fase activa de desarrollo. Los siguientes pasos están planificados:

1. **Plantillas Múltiples:** Implementar diferentes plantillas de CV según la industria (ej. tech, consultoría, académico).
2. **Validación Automática:** Agregar validación de contenido para asegurar que todos los campos requeridos estén presentes.
3. **Integración con LinkedIn:** Permitir importación de datos desde LinkedIn para facilitar la actualización del CV.
4. **Soporte Multi-idioma:** Agregar soporte para generar CVs en diferentes idiomas.
5. **Exportación a Formatos Adicionales:** Soporte para HTML y LaTeX.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para sugerir mejoras o reportar bugs.