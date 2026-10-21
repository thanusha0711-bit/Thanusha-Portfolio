from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import HexColor
from pathlib import Path

OUT = Path('output/pdf/Thanusha_Shri_Internship_Resume.pdf')
OUT.parent.mkdir(parents=True, exist_ok=True)
NAVY = HexColor('#18324B')
TEAL = HexColor('#147D83')
TEXT = HexColor('#263442')
MUTED = HexColor('#5C6B78')
PALE = HexColor('#E8F2F3')

doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=16*mm, leftMargin=16*mm,
                        topMargin=12*mm, bottomMargin=12*mm,
                        title='S L Thanusha Shri - Internship Resume',
                        author='S L Thanusha Shri')
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Name', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=21,
    leading=24, textColor=NAVY, alignment=TA_LEFT, spaceAfter=2))
styles.add(ParagraphStyle(name='Contact', fontName='Helvetica', fontSize=8.2, leading=11,
    textColor=MUTED, spaceAfter=0))
styles.add(ParagraphStyle(name='Section', fontName='Helvetica-Bold', fontSize=9.8, leading=12,
    textColor=TEAL, spaceBefore=5, spaceAfter=3, uppercase=True))
styles.add(ParagraphStyle(name='BodyX', fontName='Helvetica', fontSize=8.55, leading=11.1,
    textColor=TEXT, spaceAfter=2))
styles.add(ParagraphStyle(name='SmallX', fontName='Helvetica', fontSize=8, leading=10,
    textColor=TEXT, spaceAfter=1))
styles.add(ParagraphStyle(name='Project', fontName='Helvetica-Bold', fontSize=8.8, leading=10.5,
    textColor=NAVY, spaceAfter=1))
styles.add(ParagraphStyle(name='Photo', fontName='Helvetica', fontSize=7.3, leading=9,
    textColor=MUTED, alignment=TA_CENTER))

P = lambda s, style='BodyX': Paragraph(s, styles[style])
story = []
header_left = [P('S L THANUSHA SHRI', 'Name'),
    P('Bengaluru, Karnataka  |  9972116892  |  <link href="mailto:thanusha0711@gmail.com" color="#147D83">thanusha0711@gmail.com</link>', 'Contact'),
    P('<link href="https://www.linkedin.com/in/s-l-thanusha-shri-3417b63a8" color="#147D83">LinkedIn</link>  |  <link href="https://github.com/thanusha0711-bit" color="#147D83">GitHub</link>  |  <link href="https://thanusha0711-bit.github.io/thanusha0711-github.io/" color="#147D83">Portfolio</link>', 'Contact')]
photo = Table([[P('PHOTO', 'Photo')]], colWidths=[25*mm], rowHeights=[30*mm])
photo.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.8,HexColor('#A9BAC4')),('BACKGROUND',(0,0),(-1,-1),HexColor('#F6F8F9')),('VALIGN',(0,0),(-1,-1),'MIDDLE')]))
hdr=Table([[header_left,photo]], colWidths=[doc.width-28*mm,28*mm])
hdr.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
story += [hdr, Spacer(1, 3)]

def section(title, content):
    story.append(P(title.upper(), 'Section'))
    if isinstance(content, list):
        story.extend(content)
    else:
        story.append(content)

section('Career Profile', P('Computer Science and Engineering student with hands-on experience building and deploying Flask web applications. Interested in Web Development, Python/Flask, Software Development, Frontend Development, and AI/ML internships. Comfortable working across Python, JavaScript, SQL, and core programming languages; currently developing practical ML and DSA skills.'))

section('Technical Skills', P('<b>Programming:</b> C, C++, Java (independent use); Python (project building)<br/><b>Web:</b> HTML, CSS, JavaScript, Flask (project building)<br/><b>Database &amp; tools:</b> SQL, MySQL (project building); Git/GitHub (independent use); Canva and Excel (basic)<br/><b>Currently learning:</b> Data Structures &amp; Algorithms, Machine Learning', 'SmallX'))

section('Projects', [
    P('Apartment Maintenance Management App  |  Python, Flask, HTML, CSS, JavaScript, SQL/MySQL', 'Project'),
    P('Built and deployed an apartment maintenance app for tracking maintenance amounts and expenses by category. Includes admin and resident user logins, a dashboard with charts, and PDF/Excel report exports. Developed with substantial use of AI/no-code tools.', 'SmallX'),
    Spacer(1,2),
    P('SubadrNari - Women\'s Safety App  |  Python, Flask, HTML, CSS, JavaScript', 'Project'),
    P('Collaborated with a team to build and deploy a women\'s safety app. Features include an SOS interface, emergency contact access, unsafe-area reporting, and a map interface for viewing safe routes.', 'SmallX'),
    Spacer(1,2),
    P('AI-Based Recipe Recommendation System (In Progress)  |  Python, Machine Learning', 'Project'),
    P('Team project in planning to recommend recipes from entered ingredients and from an uploaded food/ingredient image. Model and dataset selection are in progress; YOLO11 and KNN are proposed options, and implementation has not started.', 'SmallX')
])

section('Education', [
    P('B.E. Computer Science and Engineering  |  MVJ College of Engineering', 'Project'),
    P('5th semester  |  Current CGPA: 8.07/10  |  Expected graduation: 2028  |  No backlogs', 'SmallX'),
    Spacer(1,2),
    P('PUC (PCMC), St. Joseph\'s Indian Composite PU College  |  80.5%  |  Karnataka State Board', 'SmallX'),
    P('SSLC, SSB English High School  |  92.96%  |  Karnataka State Board', 'SmallX')
])

section('Additional Information', P('<b>Languages:</b> English, Kannada, Tamil  |  <b>Experience:</b> No formal internship yet', 'SmallX'))

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(HexColor('#D9E3E8'))
    canvas.setLineWidth(0.5)
    canvas.line(doc.leftMargin, 9*mm, A4[0]-doc.rightMargin, 9*mm)
    canvas.setFont('Helvetica', 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 6*mm, 'S L Thanusha Shri  |  Internship Resume')
    canvas.restoreState()

doc.build(story, onFirstPage=footer)
print(OUT.resolve())
