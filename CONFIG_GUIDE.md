# Guía de Configuración para el Generador de CV

Este proyecto ahora soporta configuraciones en formato JSON y YAML, permitiendo una personalización más flexible de tu currículum.

## 📁 Archivos de Configuración

### 1. Formatos Soportados
- **JSON**: Formato estándar para configuraciones
- **YAML**: Formato más legible y humano

### 2. Archivos de Ejemplo
- `example_config.json`: Plantilla en formato JSON
- `example_config.yaml`: Plantilla en formato YAML

## 🚀 Cómo Usar

### Opción 1: Usar el archivo de ejemplo
```bash
# Copiar el archivo de ejemplo
cp example_config.yaml my_cv.yaml

# Editar con tus datos
# ...

# Generar el CV
python3 build_cv.py my_cv.yaml
```

### Opción 2: Crear tu propio archivo
```bash
# Crear archivo YAML desde cero
# my_cv.yaml
name: "Tu Nombre"
title: "Tu Título"
email: "tu@email.com"
phone: "+XX XXX XXX XXXX"
linkedin: "https://linkedin.com/in/tuperfil"
github: "https://github.com/tuperfil"

summary: "Breve resumen profesional..."

experience:
  - company: "Empresa Actual"
    title: "Tu Cargo"
    dates: "YYYY - Presente"
    description: "Descripción de tu experiencia..."

education:
  - degree: "Tu Grado"
    institution: "Tu Universidad"
    dates: "YYYY - YYYY"

skills:
  - "Habilidad 1"
  - "Habilidad 2"
  - "Habilidad 3"
```

## 📝 Estructura del Archivo de Configuración

### Campos Obligatorios
- `name`: Tu nombre completo
- `title`: Tu título profesional
- `email`: Tu correo electrónico
- `phone`: Tu número de teléfono

### Campos Opcionales
- `linkedin`: URL de tu perfil de LinkedIn
- `github`: URL de tu perfil de GitHub
- `summary`: Resumen profesional (1-2 párrafos)

### Secciones
- `experience`: Array de experiencias laborales
  - `company`: Nombre de la empresa
  - `title`: Tu cargo
  - `dates`: Periodo de tiempo
  - `description`: Descripción de tus responsabilidades y logros

- `education`: Array de formación académica
  - `degree`: Título o grado
  - `institution`: Institución educativa
  - `dates`: Periodo de tiempo

- `skills`: Array de habilidades técnicas y profesionales

## 🔧 Características Adicionales

### Sanitización Automática
El sistema reemplaza automáticamente "Al" por "AI" en textos para mantener consistencia en terminología de IA.

### Validación de Campos
El script verifica que todos los campos obligatorios estén presentes antes de generar el CV.

## 💡 Consejos para un CV Optimizado

1. **Usa verbos de acción** al inicio de cada punto logro
2. **Incluye métricas cuantificables** siempre que sea posible
3. **Enfócate en logros** en lugar de solo responsabilidades
4. **Mantén la longitud** entre 1-2 páginas
5. **Usa palabras clave** relevantes para tu industria

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.