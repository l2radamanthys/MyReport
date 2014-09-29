from src.parser import Document


doc = Document('test2.pdf')
doc.add_section('samples/portada.svg', 'head')
doc.parse()
doc.draw()
doc.save()
