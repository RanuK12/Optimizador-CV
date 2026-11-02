# Optimizador CV - Generador de CV Optimizados para ATS

Un sistema para generar currículums profesionales optimizados para sistemas de seguimiento de candidatos (ATS) a partir de archivos de configuración JSON/YAML.

## Características

- ✅ Generación automática de CV en formato DOCX
- ✅ Validación de configuración antes de generar
- ✅ Diseño optimizado para sistemas ATS
- ✅ Formato profesional con tipografía Calibri
- ✅ Soporte para múltiples secciones (experiencia, educación, habilidades, etc.)
- ✅ Generación de PDF opcional

## Requisitos

```bash
pip install -r requirements.txt
```

O instalar manualmente:
```bash
pip install python-docx PyYAML PyPDF4 docx2pdf
```

## Uso Rápido

1. **Crea un archivo de configuración** (ejemplo: `mi_cv.json`):
```json
{
  "name": "Tu Nombre",
  "title": "Tu Título Profesional",
  "email": "tu@email.com",
  "phone": "+54 9 11 1234-5678",
  "linkedin": "https://linkedin.com/in/tuperfil",
  "github": "https://github.com/tuusuario",
  "summary": "Profesional con experiencia en...",
  "experience": [
    {
      "company": "Empresa X",
      "title": "Posición",
      "dates": "2020 - Presente",
      "description": "Descripción de responsabilidades y logros..."
    }
  ],
  "education": [
    {
      "degree": "Título",
      "institution": "Universidad",
      "dates": "2015 - 2019"
    }
  ],
  "skills": ["Python", "Machine Learning", "Data Science"]
}
```

2. **Genera tu CV**:
```bash
python build_cv.py mi_cv.json --output-pdf
```

3. **Usa el demo** para ver un ejemplo completo:
```bash
python demo.py
```

## Estructura del Proyecto

- `build_cv.py`: Script principal para generar CV
- `config_loader.py`: Carga y validación de archivos de configuración
- `cv_validator.py`: Validación detallada de la estructura del CV
- `demo.py`: Demostración completa con ejemplo
- `requirements.txt`: Dependencias del proyecto
- `example_config.yaml`: Configuración de ejemplo en formato YAML
- `example_config.json`: Configuración de ejemplo en formato JSON

## Formatos Soportados

- **Entrada**: JSON y YAML
- **Salida**: DOCX y PDF (opcional)

## Contribución

Este proyecto fue creado por Emilio Ranucoli y está diseñado para ser utilizado como herramienta profesional de generación de CV.

## Licencia

Este proyecto es parte de los desarrollos de Ranuk IT Solutions.