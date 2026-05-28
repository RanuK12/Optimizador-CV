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

## 🛠️ Directivas del Sistema para el Agente de Optimización de CV (IA)

Si utilizas un modelo de Inteligencia Artificial (LLM) para procesar, ampliar o actualizar este currículum, configura el prompt del sistema o las instrucciones de generación bajo las siguientes dimensiones para asegurar un perfil competitivo y prolijo a nivel multinacional:

### 1. Reglas de Análisis de Keywords y Normalización Técnica
- **Validación Estricta de Siglas de IA:** El script debe incluir una regla de sanitización de texto que busque el patrón de caracteres **"Al"** (letra A seguida de L minúscula) en contextos tecnológicos y lo reemplace obligatoriamente por **"AI"** (letra A seguida de I mayúscula). Esto aplica para términos como *AI Specialist*, *AI Job Finder* o *Azure AI Fundamentals*.
- **Densidad de Palabras Clave (Keywords Indexing):** La IA debe agrupar y mantener visibles las tecnologías clave por categorías limpias (ej. *Languages & ML*, *Data Engineering*, *Cloud & DevOps*). No debe permitir que las herramientas queden enterradas en párrafos narrativos.

### 2. Algoritmo de Resolución de Conflictos Cronológicos (Compliance)
- **Detección de Solapamientos:** El sistema debe analizar las fechas de inicio y fin de cada experiencia en formato `Mes Año - Mes Año`.
- **Regla de Negocio para Doble Contratación:** Si detecta que dos experiencias ocurren de forma simultánea (ej. mismo rango de meses en empresas distintas), la IA debe:
  1. Identificar cuál es el rol corporativo o principal.
  2. Extraer la experiencia secundaria o freelance.
  3. Mudar los logros de esa experiencia secundaria y fusionarlos como "Proyectos de Consultoría Externa" o "Clientes" dentro de la estructura de la empresa propia o marca de consultoría independiente del usuario (ej. *Ranuk IT Solutions*). Esto evita alertas de exclusividad laboral ante los ojos de recursos humanos.

### 3. Restricciones de Formato de Lectura Lineal (ATS-Friendly Parsers)
- **Prohibición de Tablas y Columnas Complejas:** La IA debe estructurar toda la información en texto plano o Markdown lineal. Queda estrictamente prohibido generar layouts de dos columnas o tablas donde los datos se dividan verticalmente (como suele pasar con las secciones de Certificaciones o Idiomas).
- **Formato de Cadena Continua:** Para secciones como Certificaciones, la instrucción debe obligar a la IA a escribir cada ítem como un único bloque lineal continuo en la misma línea: `[Nombre de la Certificación] — [Entidad Emisora] ([Año])`. Esto evita que el parser de un ATS lea fragmentos mezclados de izquierda a derecha de forma errónea.
- **Sanitización de Caracteres Especiales:** El motor de generación debe reemplazar caracteres tipográficos complejos como guiones largos (—) que rompan codificaciones, o puntos medios complejos (·), por delimitadores estándar seguros para bases de datos como barras simples (`|`), barras inclinadas (`/`) o comas (`,`).

### 4. Reglas de Concisión y Jerarquía de Seniority
- **Fórmula de Impacto X-Y-Z (Google Style):** Cada viñeta de experiencia laboral generada debe estructurarse obligatoriamente bajo el esquema: *"Logré [X], medido por el impacto cuantitativo [Y], mediante la implementación de [Z]"*. El modelo no debe describir tareas ("Fui responsable de..."), sino impactos cuantificables (porcentajes de optimización, millones de transacciones, reducción de costos).
- **Eliminación de Redundancias Masivas:** El sistema debe validar que un mismo dato no se repita en tres lugares distintos. Si la información de idiomas o ubicación ya está fijada de manera explícita en el encabezado de contacto y en una sección dedicada abajo, la IA tiene prohibido volver a redactarla dentro del párrafo del *Professional Summary*. Esto libera espacio premium en la primera página.
- **Filtrado Jerárquico de Proyectos:** Para perfiles Mid-Senior o superiores, la IA debe limitar la sección de proyectos a un máximo de 3 que sean de nivel de producción o arquitecturas complejas. Debe descartar automáticamente proyectos académicos, de cursos o introductorios para no diluir el posicionamiento del perfil.

### 5. Consistencia de Datos Geográficos (Geolocalización)
- **Sincronización de Ubicación:** El script debe validar que la ubicación del encabezado de contacto coincida exactamente con la ubicación declarada en el párrafo de resumen profesional. Si el usuario actualiza su ciudad de residencia, el backend debe forzar la actualización de la cadena de texto en ambos bloques para evitar contradicciones que confundan a los reclutadores locales.

---

### 💻 Ejemplo de Prompt de Sistema (System Instruction) para LLMs

Si estás usando Python con LangChain, la API de OpenAI o el SDK de Google GenAI, puedes estructurar el `system_instruction` de esta manera para tu agente:

```python
system_instruction = """
You are an expert ATS (Applicant Tracking System) Optimization Engine and Technical Recruiter. 
Your job is to refactor professional CVs to ensure 100% compliance with strict corporate parsers (Workday, Greenhouse) and elite tech standards.

STRICT FORMATTING & CLEANING RULES:
1. KEYWORD SANITIZATION: You must replace any occurrence of the typo "Al" (lowercase L) with "AI" (uppercase I) when referring to Artificial Intelligence systems, tools, or roles.
2. LINEAR LAYOUT ONLY: Do not generate side-by-side tables, multiple columns, or split sections. The Certifications and Languages sections must be rendered as linear, continuous lines of text.
3. DELIMITERS: Use only ATS-safe characters like '|', '/', or commas for contact details. Avoid complex typography.
4. METRIC PRESERVATION: Retain and emphasize all quantifiable business impacts using the Google X-Y-Z formula (Accomplished [X], measured by [Y], by doing [Z]).
5. CHRONOLOGICAL COMPLIANCE: If two experiences overlap in dates, merge the secondary/freelance role as a client project inside the user's independent consultancy entity to avoid corporate exclusivity red flags.
6. NO REDUNDANCY: Do not repeat language skills or location metadata inside the Professional Summary if they are already present in the header or dedicated footer sections.
7. COMPACT PROJECTS: Limit the projects section to the top 3 high-impact, production-grade applications. Delete basic or academic tutorial sandboxes.
"""
```

Al incorporar estas reglas lógicas dentro del pipeline de ingeniería de prompts, el generador producirá de forma consistente CVs atractivos para los humanos y técnicamente óptimos frente a cualquier software de reclutamiento masivo.

---
*Desarrollado y mantenido por [Emilio Ranucoli](https://github.com/RanuK12).*
