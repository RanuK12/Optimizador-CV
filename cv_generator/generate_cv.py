#!/usr/bin/env python3
"""
generate_cv.py

Este script genera un Curriculum Vitae sencillo a partir de un archivo de
configuración externo en formato JSON o YAML.  La idea es separar los datos
hardcodeados del código, permitiendo que cualquier usuario pueda personalizar
su CV simplemente editando un archivo de configuración.

Uso:
    python generate_cv.py [ruta_al_archivo_de_configuración]

Si no se especifica ninguna ruta, se utilizará `sample_data.json` que se
encuentra en el mismo directorio del script.
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict

# PyYAML es opcional; si no está disponible, solo se admiten archivos JSON.
try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore


def load_config(config_path: Path) -> Dict[str, Any]:
    """
    Carga la configuración del CV desde un archivo JSON o YAML.

    Parameters
    ----------
    config_path: Path
        Ruta al archivo de configuración.

    Returns
    -------
    dict
        Diccionario con los datos del CV.
    """
    if not config_path.is_file():
        raise FileNotFoundError(f"Archivo de configuración no encontrado: {config_path}")

    ext = config_path.suffix.lower()
    with config_path.open("r", encoding="utf-8") as f:
        if ext == ".json":
            return json.load(f)
        elif ext in {".yaml", ".yml"}:
            if yaml is None:
                raise RuntimeError(
                    "PyYAML no está instalado. Instálalo con `pip install pyyaml` para usar archivos YAML."
                )
            return yaml.safe_load(f)
        else:
            raise ValueError(
                f"Extensión de archivo no soportada: {ext}. Use .json, .yaml o .yml"
            )


def render_markdown(cv_data: Dict[str, Any]) -> str:
    """
    Convierte los datos del CV a una cadena en formato Markdown.

    Parameters
    ----------
    cv_data: dict
        Diccionario con la información del CV.

    Returns
    -------
    str
        Representación del CV en Markdown.
    """
    lines = []

    # Información personal
    personal = cv_data.get("personal", {})
    name = personal.get("name", "Nombre Apellido")
    title = personal.get("title", "")
    lines.append(f"# {name}")
    if title:
        lines.append(f"_{title}_")
    lines.append("")
    contact_parts = [
        personal.get("email"),
        personal.get("phone"),
        personal.get("linkedin"),
    ]
    contact = " | ".join(filter(None, contact_parts))
    if contact:
        lines.append(contact)
        lines.append("---")
        lines.append("")

    # Educación
    education = cv_data.get("education", [])
    if education:
        lines.append("## Educación")
        for edu in education:
            degree = edu.get("degree", "")
            institution = edu.get("institution", "")
            year = edu.get("year", "")
            lines.append(f"**{degree}**, {institution} ({year})")
        lines.append("")

    # Experiencia
    experience = cv_data.get("experience", [])
    if experience:
        lines.append("## Experiencia")
        for exp in experience:
            position = exp.get("position", "")
            company = exp.get("company", "")
            period = exp.get("period", "")
            lines.append(f"**{position}**, {company} ({period})")
            details = exp.get("details", [])
            for detail in details:
                lines.append(f"- {detail}")
        lines.append("")

    # Habilidades
    skills = cv_data.get("skills", [])
    if skills:
        lines.append("## Habilidades")
        lines.append(", ".join(skills))
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    """
    Punto de entrada del script.
    """
    # Determinar la ruta del archivo de configuración
    if len(sys.argv) > 1:
        config_file = Path(sys.argv[1])
    else:
        # Ruta por defecto al archivo de ejemplo JSON incluido en el repositorio
        config_file = Path(__file__).with_name("sample_data.json")

    try:
        cv_data = load_config(config_file)
    except Exception as exc:
        sys.stderr.write(f"Error al cargar la configuración: {exc}\n")
        sys.exit(1)

    markdown_cv = render_markdown(cv_data)

    # Guardar el resultado en un archivo Markdown con el mismo nombre que el
    # archivo de configuración pero con extensión .md
    output_path = config_file.with_suffix(".md")
    output_path.write_text(markdown_cv, encoding="utf-8")
    print(f"CV generado correctamente: {output_path}")


if __name__ == "__main__":
    main()
