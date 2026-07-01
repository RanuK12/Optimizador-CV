"""Tests for CVGenerator."""
import pytest
import os
import json
from src.generate_cv import CVGenerator

@pytest.fixture
def generator():
    return CVGenerator(template_path="templates/cv_template.docx")

def test_generate_from_json(generator):
    """Test that CV is generated from JSON."""
    json_path = "data/cv_example.json"
    docx_path, pdf_path = generator.generate_from_json(json_path)
    assert os.path.exists(docx_path), f"El DOCX no se generó en {docx_path}"
    assert os.path.exists(pdf_path), f"El PDF no se generó en {pdf_path}"

def test_cv_has_sections(generator):
    """Test that CV has expected sections."""
    json_path = "data/cv_example.json"
    docx_path, pdf_path = generator.generate_from_json(json_path)
    doc = generator.doc
    text = "\n".join([p.text for p in doc.paragraphs])
    assert "Experiencia Profesional" in text, "Falta sección 'Experiencia Profesional'"
    assert "Educación" in text, "Falta sección 'Educación'"
    assert "Habilidades Técnicas" in text, "Falta sección 'Habilidades Técnicas'"
    assert "Proyectos Relevantes" in text, "Falta sección 'Proyectos Relevantes'"
    assert "Idiomas" in text, "Falta sección 'Idiomas'"
    assert "Certificaciones" in text, "Falta sección 'Certificaciones'"

def test_ats_keywords(generator):
    """Test that CV includes ATS keywords."""
    json_path = "data/cv_example.json"
    docx_path, pdf_path = generator.generate_from_json(json_path)
    doc = generator.doc
    text = "\n".join([p.text for p in doc.paragraphs])
    # Palabras clave típicas de ATS
    keywords = ["Python", "SQL", "AWS", "ML", "Docker", "FastAPI", "PostgreSQL"]
    for kw in keywords:
        assert kw in text, f"Falta palabra clave ATS: {kw}"

def test_pdf_conversion_fallback(generator):
    """Test that PDF conversion works (with fallback)."""
    json_path = "data/cv_example.json"
    # Forzar fallback (simular error en docx2pdf)
    import subprocess
    original_run = subprocess.run
    def mock_run(cmd, *args, **kwargs):
        if "docx2pdf" in " ".join(cmd):
            raise subprocess.CalledProcessError(1, cmd)
        return original_run(cmd, *args, **kwargs)
    subprocess.run = mock_run
    try:
        docx_path, pdf_path = generator.generate_from_json(json_path)
        assert os.path.exists(docx_path), "DOCX no se generó ni con fallback"
        # Verificar que el PDF fallback existe
        fallback_pdf = pdf_path.replace(".pdf", "_fallback.docx")
        assert os.path.exists(fallback_pdf), "Fallback PDF no se creó"
    finally:
        subprocess.run = original_run