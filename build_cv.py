"""Generate ATS-optimized CV (DOCX + PDF) using configuration data."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import json
import os
import sys
from typing import Dict, Any

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCX_PATH = os.path.join(OUT_DIR, "EmilioRanucoli_MLEngineer.docx")
PDF_PATH  = os.path.join(OUT_DIR, "EmilioRanucoli_MLEngineer.pdf")

NAVY  = RGBColor(0x1A, 0x36, 0x5D)
BLACK = RGBColor(0x11, 0x11, 0x11)

doc = Document()

style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(10.5)
style.font.color.rgb = BLACK

for section in doc.sections:
    section.top_margin = Cm(1.2)
    section.bottom_margin = Cm(1.2)
    section.left_margin = Cm(1.6)
    section.right_margin = Cm(1.6)

def add_hyperlink(paragraph, url, text, size=10):
    part = paragraph.part
    r_id = part.relate_to(url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True)
    hyperlink = OxmlElement('w:hyperlink')
    hyperlink.set(qn('r:id'), r_id)
    new_run = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    color = OxmlElement('w:color'); color.set(qn('w:val'), '1A365D'); rPr.append(color)
    u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); rPr.append(u)
    rFonts = OxmlElement('w:rFonts'); rFonts.set(qn('w:ascii'), 'Calibri'); rFonts.set(qn('w:hAnsi'), 'Calibri'); rPr.append(rFonts)
    sz = OxmlElement('w:sz'); sz.set(qn('w:val'), str(int(size*2))); rPr.append(sz)
    new_run.append(rPr)
    t = OxmlElement('w:t'); t.text = text; new_run.append(t)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)

def heading(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(7)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.0
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(14)
    run.font.color.rgb = NAVY
    run.font.bold = True
    return p

def load_config_data(config_path: str = "cv_config.json") -> Dict[str, Any]:
    """
    Load CV configuration from a JSON file with error handling.
    
    Args:
        config_path: Path to the JSON configuration file
        
    Returns:
        Dictionary containing CV configuration data
    """
    try:
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # Validate required fields
        required_fields = ['name', 'title', 'email', 'phone']
        missing_fields = [field for field in required_fields if field not in config]
        
        if missing_fields:
            raise ValueError(f"Missing required fields in configuration: {', '.join(missing_fields)}")
        
        return config
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please create a cv_config.json file with your CV data.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in configuration file: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """Main function to generate CV from configuration."""
    # Load configuration
    config = load_config_data()
    
    # Add header section
    heading(config['name'])
    p = doc.add_paragraph()
    run = p.add_run(config['title'])
    run.font.size = Pt(11)
    run.font.color.rgb = NAVY
    run.font.bold = True
    
    # Contact information
    p = doc.add_paragraph()
    contact_info = f"{config['email']} | {config['phone']}"
    if 'linkedin' in config:
        contact_info += f" | {config['linkedin']}"
    if 'github' in config:
        contact_info += f" | {config['github']}"
    p.add_run(contact_info)
    
    # Add sections from config
    if 'summary' in config:
        heading("Summary")
        p = doc.add_paragraph(config['summary'])
        p.paragraph_format.space_after = Pt(6)
    
    if 'experience' in config:
        heading("Experience")
        for exp in config['experience']:
            p = doc.add_paragraph()
            p.add_run(exp['company']).bold = True
            p.add_run(f" | {exp['title']} | {exp['dates']}")
            p.paragraph_format.space_after = Pt(3)
            
            if 'description' in exp:
                desc = doc.add_paragraph(exp['description'])
                desc.paragraph_format.left_indent = Cm(0.5)
                desc.paragraph_format.space_after = Pt(3)
    
    if 'education' in config:
        heading("Education")
        for edu in config['education']:
            p = doc.add_paragraph()
            p.add_run(edu['degree']).bold = True
            p.add_run(f" | {edu['institution']} | {edu['dates']}")
            p.paragraph_format.space_after = Pt(3)
    
    if 'skills' in config:
        heading("Skills")
        skills_text = ", ".join(config['skills'])
        p = doc.add_paragraph(skills_text)
        p.paragraph_format.space_after = Pt(6)
    
    # Save document
    doc.save(DOCX_PATH)
    print(f"CV generated successfully: {DOCX_PATH}")

if __name__ == "__main__":
    main()