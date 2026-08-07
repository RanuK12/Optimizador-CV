"""Generate ATS-optimized CV (DOCX + PDF) using configuration data."""
import argparse
import json
import os
import sys
from typing import Dict, Any

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

from config_loader import load_config

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

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


def main():
    parser = argparse.ArgumentParser(
        description="Generate ATS-optimized CV (DOCX) from a JSON config file."
    )
    parser.add_argument(
        "config",
        nargs="?",
        default="cv_config.json",
        help="Path to JSON config file (default: cv_config.json)"
    )
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Output filename (without extension). Default: uses name from config"
    )
    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)
    
    # Determine output filename
    if args.output:
        base_name = args.output
    else:
        # Use name from config or default to "CV"
        base_name = config.get('name', 'CV').replace(' ', '_')
    
    DOCX_PATH = os.path.join(OUT_DIR, f"{base_name}.docx")
    PDF_PATH  = os.path.join(OUT_DIR, f"{base_name}.pdf")
    
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