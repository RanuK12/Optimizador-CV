"""Generate ATS-optimized CV (DOCX + PDF) for Emilio Ranucoli — ML Engineer."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

import os

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
    r = p.add_run(text.upper())
    r.bold = True; r.font.size = Pt(11.5); r.font.color.rgb = NAVY
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'),'single'); bottom.set(qn('w:sz'),'6'); bottom.set(qn('w:space'),'1'); bottom.set(qn('w:color'),'1A365D')
    pBdr.append(bottom); pPr.append(pBdr)

def bullet(text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r = p.add_run(text); r.font.size = Pt(10.5)

def line(text, bold=False, size=10.5, color=BLACK, space_after=2, italic=False, align=None):
    p = doc.add_paragraph()
    if align is not None: p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    r = p.add_run(text)
    r.bold = bold; r.italic = italic; r.font.size = Pt(size); r.font.color.rgb = color
    return p

def role_header(title, company, location, dates, client=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(f"{title}"); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NAVY
    r = p.add_run(f"   |   {company}"); r.bold = True; r.font.size = Pt(11)
    if client:
        r = p.add_run(f"  ({client})"); r.italic = True; r.font.size = Pt(10)
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(f"{location}   ·   {dates}"); r.italic = True; r.font.size = Pt(9.5); r.font.color.rgb = NAVY

# ===================== HEADER =====================
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(0)
r = p.add_run("EMILIO RANUCOLI")
r.bold = True; r.font.size = Pt(20); r.font.color.rgb = NAVY

line("Machine Learning Engineer | Python Developer | Data & AI Specialist",
     size=11, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)

line("Barcelona, Spain | Italian Citizen - EU Work Authorization (no sponsorship required)",
     size=10, color=NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)
line("Open to Remote EU & Hybrid | Trilingual: English (Fluent), Spanish (Native), Italian (Native)",
     size=10, color=NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(0)
r = p.add_run("+39 344 5721753 | "); r.font.size = Pt(10)
add_hyperlink(p, "mailto:ranucoliemilio@gmail.com", "ranucoliemilio@gmail.com")
r = p.add_run(" | "); r.font.size = Pt(10)
add_hyperlink(p, "https://linkedin.com/in/emilio-ranucoli", "linkedin.com/in/emilio-ranucoli")
r = p.add_run(" | "); r.font.size = Pt(10)
add_hyperlink(p, "https://github.com/RanuK12", "github.com/RanuK12")
r = p.add_run(" | "); r.font.size = Pt(10)
add_hyperlink(p, "https://ranuk.dev", "ranuk.dev")

# ===================== SUMMARY =====================
heading("Professional Summary")
line(
    "Machine Learning Engineer and Python Developer based in Barcelona, Spain, with hands-on experience "
    "building production ML systems, ETL data pipelines and microservices for Booking.com, Accenture and "
    "enterprise clients across the EU. Specialized in Python, Scikit-learn, XGBoost, TensorFlow, FastAPI "
    "and AWS, with a strong record of measurable impact (12% lift in promotional targeting accuracy at "
    "Booking.com, 15% supply-chain cost reduction at Accenture, 2M+ daily transactions processed via "
    "near-real-time ETL). Expertise spans end-to-end MLOps pipeline construction, scalable AI/LLM integrations "
    "and robust system architecture. Founder of Ranuk IT Solutions, delivering custom software and ML products "
    "to clients in 4 countries. Italian citizen with full EU work authorization (no sponsorship required).",
    size=10.5, space_after=3
)

p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(2)
r = p.add_run('"Combines technical rigor with an uncommon ability to understand the problem before writing code. Recommended 100%."')
r.italic = True; r.font.size = Pt(10); r.font.color.rgb = NAVY
r = p.add_run(" - Delfina Bugliotti, Product Manager @ Booking.com")
r.font.size = Pt(9.5); r.italic = True

# ===================== TECHNICAL SKILLS =====================
heading("Technical Skills")
stack = [
    ("Languages & ML",          "Python (Pandas, NumPy, Scikit-learn, TensorFlow, Keras, XGBoost, PyTorch), SQL, JavaScript / TypeScript, C#"),
    ("Machine Learning",        "Supervised & Unsupervised Learning, Deep Learning, Neural Networks, NLP, Sentiment Analysis, Time Series Forecasting, MLOps"),
    ("Data Engineering",        "ETL Pipelines, Data Wrangling, Data Modeling, Data Warehouse, RESTful APIs, JSON, Kafka, Streaming Data"),
    ("Backend & Web",           "FastAPI, Flask, Node.js, React, Tailwind CSS, HTML5 / CSS3, Microservices, GraphQL"),
    ("BI & Visualization",      "Power BI (PL-300 Certified), DAX, Tableau, Looker, Grafana, Streamlit, Plotly"),
    ("Databases",               "PostgreSQL, MongoDB, MySQL, SQL Server, SAP"),
    ("Cloud & DevOps",          "AWS (Cloud Practitioner Certified), Microsoft Azure (AI Fundamentals), GCP, Docker, Kubernetes, Git / GitHub, CI/CD"),
    ("Testing & Methodologies", "JUnit, TDD, REST, SOAP, Agile / Scrum, Code Reviews"),
]
for label, val in stack:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.2)
    r = p.add_run(f"{label}:  "); r.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = NAVY
    r = p.add_run(val); r.font.size = Pt(10.5)

# ===================== EXPERIENCE =====================
heading("Professional Experience")

# 1. BOOKING.COM
role_header("Machine Learning Engineer (Contract)",
            "Booking.com", "Amsterdam, Netherlands", "May 2025 - Oct 2025")
bullet("Led the development of a dynamic pricing optimization system, deploying Machine Learning models (Python, Scikit-learn, XGBoost, neural networks) for real-time price adjustments based on demand, competition and customer behavior.")
bullet("Analyzed 5M+ historical booking records to identify patterns that improved customer segmentation and promotional campaign effectiveness across multiple markets.")
bullet("Integrated production ML models into Booking.com's AWS environment with continuous monitoring, ensuring scalability and reproducibility of predictions.")
bullet("Built a GraphQL backend layer to reduce API latency and serve cached features to downstream services.")
bullet("Contributed to a 12% improvement in promotional targeting accuracy by mastering internal forecasting tools and tuning model features.")

# 2. RANUK IT SOLUTIONS
role_header("Founder & Lead Engineer",
            "Ranuk IT Solutions", "Barcelona, Spain (Remote)", "2024 - Present")
bullet("Founded and operate a tech consultancy delivering custom software and applied Machine Learning solutions to clients in Argentina, Spain, Italy, and the United States.")
bullet("Delivered 28+ in-house projects across web, backend, automation, and ML, owning the full lifecycle from product discovery to deployment and continuous support.")
bullet("Eurobrico S.p.A. (Major Italian DIY Retail Chain / External Consultancy, Nov 2024 - Apr 2025): Deployed Python inventory management applications and data integration workflows, automating retail operations and reducing manual errors; executed a complete UX/UI web redesign and front-end prototype to modernize the customer journey.")
bullet("NOT A ROBOT (Audiovisual Production): Designed and built the full web platform powering their brand presence and client showcase.")
bullet("Bahay Design (Architecture Studio, Italy): Delivered a high-end responsive website with same-day iteration cycles requested directly by the client.")
bullet("GARYCIO: Built a production-ready backend service with WhatsApp bot integration, PostgreSQL persistence, and automated PDF report generation.")
bullet("ranuk.dev (Personal Engineering Brand): Features an interactive, in-browser Neural Network Lab with configurable learning rates, epochs, and hidden neurons showing real-time decision-boundary visualization.")
bullet("Core stack: TypeScript, React, Node.js, Python, PostgreSQL, Scikit-learn, XGBoost, TensorFlow, PyTorch, MLOps.")

# 3. ACCENTURE ROMA
role_header("Python Developer - Supply Chain Integration (Main role)",
            "Accenture", "Rome, Italy (On-site)", "Nov 2024 - Apr 2025")
bullet("Designed and built Python microservices to integrate supply-chain data between SAP, Oracle and legacy ERPs for a major logistics client.")
bullet("Engineered automated ETL pipelines processing 2M+ daily transactions, reducing data latency from 24 hours to near real-time.")
bullet("Developed REST APIs for inventory synchronization across warehouses, achieving 99.7% data consistency across 50+ locations.")
bullet("Implemented Grafana dashboards and alerting systems for pipeline health monitoring and SLA compliance tracking.")
bullet("Stack: Python, FastAPI, SAP, Oracle, PostgreSQL, Docker, Grafana, REST APIs.")

# 4. ACCENTURE ARGENTINA
role_header("Data Science Analyst / Sr. Analyst - Supply Chain & Operations",
            "Accenture", "Argentina (Remote)", "Jun 2024 - Nov 2024")
bullet("Developed predictive and optimization models for supply-chain operations using Python, SQL and Power BI.")
bullet("Implemented Machine Learning models for demand forecasting and inventory optimization, achieving a 15% operational cost reduction.")
bullet("Built interactive dashboards in Tableau and Power BI to visualize critical KPIs and support data-driven decision-making.")
bullet("Worked with multidisciplinary global teams under Agile / Scrum methodologies.")

# 5. GOVERNMENT OF CORDOBA
role_header("Data Analyst & Power BI Specialist",
            "Government of Córdoba", "Córdoba, Argentina", "Nov 2023 - Jun 2024")
bullet("Designed and maintained 15+ Power BI dashboards tracking KPIs for public works and infrastructure programs.")
bullet("Performed data cleaning and modeling on 200K+ record datasets, improving report accuracy by 30%.")
bullet("Automated certification reporting workflows, reducing manual effort by 40% and freeing analyst time for higher-value work.")

# 6. FARMASUT - condensed
role_header("Purchasing & Inventory Analyst",
            "Farmasut", "Córdoba, Argentina", "Nov 2015 - Oct 2023")
bullet("Conducted inventory audits and sales analysis with Tableau, reducing expiration losses by 15%.")
bullet("Optimized delivery routes through data analysis, decreasing logistics costs and improving fulfillment SLAs.")

# ===================== KEY PROJECTS =====================
heading("Key Projects")

def project(title, stack_line, desc, url=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(title); r.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = NAVY
    if url:
        r = p.add_run("   |   "); r.font.size = Pt(10)
        add_hyperlink(p, url, url.replace("https://",""))
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(f"Stack: "); r.bold = True; r.italic = True; r.font.size = Pt(9.5)
    r = p.add_run(stack_line); r.italic = True; r.font.size = Pt(9.5)
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
    r = p.add_run(desc); r.font.size = Pt(10.5)

project("GARYCIO - WhatsApp Backend Bot",
        "TypeScript, Node.js, WhatsApp API, PostgreSQL, PDF Generation",
        "Production-grade backend service with WhatsApp integration and automated PDF reporting deployed for an international enterprise client.",
        "https://github.com/RanuK12")

project("Crypto Analysis Dashboard",
        "Python, Streamlit, Plotly, Binance API, Machine Learning, Telegram Bot",
        "Cryptocurrency market analysis platform with real-time data ingestion, algorithmic trading strategy backtesting and a modern interactive web interface.",
        "https://github.com/RanuK12")

project("JobConnect - AI Job Finder",
        "Flask, NLP, Web Scraping, Tailwind CSS",
        "Web platform that uses NLP to match candidate CVs with job openings across multiple platforms, ranking results by semantic fit.",
        "https://github.com/RanuK12")

# ===================== EDUCATION =====================
heading("Education")
p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1)
r = p.add_run("Systems Engineering"); r.bold = True; r.font.size = Pt(10.5)
r = p.add_run("  -  Universidad Tecnológica Nacional (UTN), Argentina"); r.font.size = Pt(10.5)

# ===================== CERTIFICATIONS =====================
heading("Certifications")
certs = [
    "Microsoft Power BI Data Analyst (PL-300) — Microsoft (2024)",
    "AWS Cloud Practitioner — Amazon Web Services (2024)",
    "Microsoft Azure AI Fundamentals (AI-900) — Microsoft (2024)",
    "Machine Learning with Python — IBM (2025)",
    "Deep Learning Fundamentals — IBM (2025)",
    "Deep Learning with TensorFlow — IBM (2025)",
    "Intermediate Machine Learning — Kaggle (2024)",
]
for c in certs:
    bullet(c)

# ===================== LANGUAGES =====================
heading("Languages")
p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(0)
r = p.add_run("English: "); r.bold = True; r.font.size = Pt(10.5)
r = p.add_run("Fluent (Professional Working Proficiency)     "); r.font.size = Pt(10.5)
r = p.add_run("Spanish: "); r.bold = True; r.font.size = Pt(10.5)
r = p.add_run("Native     "); r.font.size = Pt(10.5)
r = p.add_run("Italian: "); r.bold = True; r.font.size = Pt(10.5)
r = p.add_run("Native"); r.font.size = Pt(10.5)

# ===================== PUBLICATIONS =====================
heading("Publications")
p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(0)
r = p.add_run('"Y asi voy tejiendo mi camino"'); r.italic = True; r.bold = True; r.font.size = Pt(10.5)
r = p.add_run("  -  Memoir, self-published 2024. Available on Kindle."); r.font.size = Pt(10.5)

doc.save(DOCX_PATH)
print("DOCX OK:", DOCX_PATH)

try:
    from docx2pdf import convert
    convert(DOCX_PATH, PDF_PATH)
    print("PDF OK:", PDF_PATH)
except Exception as e:
    print("PDF FAIL:", e)
