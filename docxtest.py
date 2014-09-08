from docx import *

document = Document()

document.add_heading('Document Title', 0)

document.save('demo.docx')