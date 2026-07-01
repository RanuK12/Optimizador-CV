"""Generate ATS-optimized CV (DOCX + PDF) for Emilio Ranucoli — ML Engineer."""
from src.generate_cv import CVGenerator
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCX_PATH = os.path.join(OUT_DIR, "EmilioRanucoli_MLEngineer.docx")
PDF_PATH  = os.path.join(OUT_DIR, "EmilioRanucoli_MLEngineer.pdf")

if __name__ == "__main__":
    # Generar CV desde el ejemplo JSON
    generator = CVGenerator(template_path="templates/cv_template.docx")
    docx_path, pdf_path = generator.generate_from_json(
        json_path="data/cv_example.json",
        output_docx=DOCX_PATH,
        output_pdf=PDF_PATH
    )
    print(f"CV generado para Emilio Ranucoli: {docx_path} y {pdf_path}")