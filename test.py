

from src.parser import Document

#ejemplo documento cabecera
doc = Document('test.pdf')
doc.add_section('samples/portada.svg', 'header')
doc.add_section('samples/list-body.svg', 'body', paginate=True)
#print doc.sections
doc.parse()

#informacion para organizar contenido
index = ['field1', 'field2', 'field3']
end_id = 'end'
link = [('field1', 0), ('field2', 1), ('field3', 2)]
#generar datos de ejemplo
data = []
for i in range(500):
    data.append(['data contenido {0}'.format(i), 'data {0}'.format(i), 'data field {0}'.format(i)])

doc.section_paginate('body', data, index, link, end_id)
doc.draw()
doc.save()
