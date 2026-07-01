from docx import Document
from docx.shared import Cm

def create_template(path):
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Calibri'
    
    for section in doc.sections:
        section.top_margin = Cm(1.2)
        section.bottom_margin = Cm(1.2)
        section.left_margin = Cm(1.6)
        section.right_margin = Cm(1.6)
    
    doc.save(path)

if __name__ == "__main__":
    template_path = '/Users/emilioranucoli/Desktop/Oficina_Ranuk/Optimizador-CV/templates/cv_template.docx'
    create_template(template_path)
    print(f"Plantilla creada en {template_path}")