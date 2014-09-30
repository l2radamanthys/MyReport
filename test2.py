from src import parser
from src.parser import Document

parser.initialize()
doc = Document('test2.pdf')
doc.add_section('samples/font-text.svg', 'head')
doc.parse()
doc.draw()
doc.save()
